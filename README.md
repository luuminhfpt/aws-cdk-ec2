
# Welcome to the CDK Construct Library for AWS::EC2

This project provides a CDK construct to create an EC2 Instance, development with Python language.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project. The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

Copy .env.example to .env to config your aws acount id and region

```
$ CDK_DEFAULT_ACCOUNT=xxx
$ CDK_DEFAULT_REGION=xxx
```

Use the cdk bootstrap command to bootstrap AWS environments

```
$ cdk bootstrap
```

To deploy this stack to your default AWS account/region

```
$ cdk deploy
```

Or you can using the script file in scripts folder to deploy to specific environments

```
$ ./cdk-deploy-to.sh 123457689 us-east-1 "$@"
```

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation