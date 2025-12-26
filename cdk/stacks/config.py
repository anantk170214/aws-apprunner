import os

PROJECT_NAME = "ddb-apprunner-example"
ENVIRONMENT = "dev"

AWS_ACCOUNT = os.getenv("CDK_DEFAULT_ACCOUNT")
AWS_REGION = os.getenv("CDK_DEFAULT_REGION")

VPC_CONFIG = {
    "cidr": "10.0.0.0/16",
    "max_azs": 2,
}

ECR_REPOSITORY_NAME = f"{PROJECT_NAME}-repo"

DYNAMODB_TABLE = {
    "name": f"{PROJECT_NAME}-table",
    "partition_key": "id",
    "sort_key": None,
}

APPRUNNER_CONFIG = {
    "service_name": f"{PROJECT_NAME}-service",
    "port": 8080,
}
