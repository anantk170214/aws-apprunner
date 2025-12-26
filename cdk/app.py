import aws_cdk as cdk
from dotenv import load_dotenv
from stacks.config import AWS_ACCOUNT, AWS_REGION
from stacks.network_stack import NetworkStack
from stacks.data_stack import DataStack
from stacks.iam_stack import IamStack
from stacks.apprunner_stack import AppRunnerStack

load_dotenv()

app = cdk.App()

env = cdk.Environment(
    account=AWS_ACCOUNT,
    region=AWS_REGION,
)

network = NetworkStack(app, "NetworkStack", env=env)
data = DataStack(app, "DataStack", env=env)
iam = IamStack(app, "IamStack", dynamo_table=data.table, env=env)

AppRunnerStack(
    app,
    "AppRunnerStack",
    vpc=network.vpc,
    ecr_repo=data.repository,
    dynamo_table=data.table,
    service_role=iam.app_runner_role,
    env=env,
)

app.synth()
