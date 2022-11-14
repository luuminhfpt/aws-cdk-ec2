from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
)
from constructs import Construct

class AwsCdkEc2PythonStack(Stack):

    instance_name = "MinhLuuInstance"
    vps = None
    security_group = None
    key_pair = None
    user_data = None

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.getVPC()
        instance_type = ec2.InstanceType.of(
            ec2.InstanceClass.T2,
            ec2.InstanceSize.MICRO,
        )
        machine_image = ec2.AmazonLinuxImage(
            generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            storage = ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )
        self.getSecurityGroup()
        self.getKeyPair()
        self.getUserData()

        ec2.Instance(
            self, 
            self.instance_name,
            vpc = self.vpc,
            instance_type = instance_type,
            machine_image = machine_image,
            key_name = self.key_pair.key_name,
            user_data = self.user_data
        )

    def getVPC(self):
        self.vpc = ec2.Vpc.from_lookup(self, "MinhLuuDefaultVPC", is_default=True)
        # or create new VPC if you want

    def getSecurityGroup(self):
        # create Security Group for the Instance
        security_group_name = self.instance_name + "-SG"

        security_group = ec2.SecurityGroup(
            self, 
            security_group_name, 
            vpc = self.vpc,
            allow_all_outbound = True
        )

        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(80),
            'allow HTTP traffic from anywhere',
        )

        security_group.add_ingress_rule(
            ec2.Peer.any_ipv4(),
            ec2.Port.tcp(443),
            'allow HTTPS traffic from anywhere',
        )

        security_group.add_ingress_rule(
            ec2.Peer.ipv4("3.1.15.39/32"),
            ec2.Port.tcp(22),
            'allow SSH access from vpn bigin',
        )

        security_group.add_ingress_rule(
            ec2.Peer.ipv4("3.214.249.149/32"),
            ec2.Port.tcp(22),
            'allow SSH access from bigin gitlap runner',
        )

        self.security_group =  security_group

    def getKeyPair(self):
        key_name = self.instance_name + "-key"
        self.key_pair = ec2.CfnKeyPair(
            self, 
            key_name,
            key_name = key_name,
            key_type="rsa"
        )

    def getUserData(self):
        multipart_user_data = ec2.MultipartUserData()

        commands_user_data = ec2.UserData.for_linux()
        commands_user_data.add_commands("sudo yum update -y && sudo amazon-linux-extras install docker -y && sudo service docker start && sudo usermod -a -G docker ec2-user")

        multipart_user_data.add_user_data_part(commands_user_data, ec2.MultipartBody.SHELL_SCRIPT, True)

        self.user_data = multipart_user_data