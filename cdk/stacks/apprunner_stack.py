
from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_apprunner as apprunner
from aws_cdk import aws_ec2 as ec2
from aws_cdk import aws_iam as iam
from aws_cdk import aws_dynamodb as dynamodb
from aws_cdk import aws_ecr as ecr
from .config import APPRUNNER_CONFIG


class AppRunnerStack(Stack):
    def __init__(
        self,
        scope: Construct,
        id: str,
        vpc: ec2.Vpc,
        ecr_repo: ecr.Repository,
        dynamo_table: dynamodb.Table,
        service_role: iam.Role,
        **kwargs,
    ):
        super().__init__(scope, id, **kwargs)

        # ✅ Public placeholder image
        placeholder_image = "public.ecr.aws/nginx/nginx:latest"

        apprunner.CfnService(
            self,
            "AppRunnerService",
            service_name=APPRUNNER_CONFIG["service_name"],
            source_configuration={
                "imageRepository": {
                    "imageIdentifier": placeholder_image,
                    "imageRepositoryType": "ECR_PUBLIC",
                    "imageConfiguration": {
                        "port": "80"
                    },
                },
                # 🚨 IMPORTANT:
                # ❌ authenticationConfiguration MUST NOT be present for ECR_PUBLIC
                "autoDeploymentsEnabled": False,
            },
            instance_configuration={
                "cpu": "1024",
                "memory": "2048",
            },
            tags=[
                {
                    "key": "deployment-mode",
                    "value": "placeholder",
                }
            ],
        )
