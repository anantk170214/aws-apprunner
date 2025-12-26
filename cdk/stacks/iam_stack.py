from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_iam as iam
from aws_cdk import aws_dynamodb as dynamodb

class IamStack(Stack):
    def __init__(self, scope: Construct, id: str, dynamo_table: dynamodb.Table, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.app_runner_role = iam.Role(
            self,
            "AppRunnerRole",
            assumed_by=iam.ServicePrincipal("tasks.apprunner.amazonaws.com"),
        )

        dynamo_table.grant_read_write_data(self.app_runner_role)

        self.app_runner_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name(
                "AmazonEC2ContainerRegistryReadOnly"
            )
        )
