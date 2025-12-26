
from constructs import Construct
from aws_cdk import Stack, RemovalPolicy
from aws_cdk import aws_ecr as ecr
from aws_cdk import aws_dynamodb as dynamodb
from .config import ECR_REPOSITORY_NAME, DYNAMODB_TABLE

class DataStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # ✅ ECR repository (RESTORED)
        self.repository = ecr.Repository(
            self,
            "EcrRepository",
            repository_name=ECR_REPOSITORY_NAME,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_images=True,   # 👈 REQUIRED
        )

        # ✅ DynamoDB table (SAFE creation)
        table_kwargs = {
            "table_name": DYNAMODB_TABLE["name"],
            "partition_key": dynamodb.Attribute(
                name=DYNAMODB_TABLE["partition_key"],
                type=dynamodb.AttributeType.STRING,
            ),
            "billing_mode": dynamodb.BillingMode.PAY_PER_REQUEST
        }

        if DYNAMODB_TABLE.get("sort_key"):
            table_kwargs["sort_key"] = dynamodb.Attribute(
                name=DYNAMODB_TABLE["sort_key"],
                type=dynamodb.AttributeType.STRING,
            )


        self.table = dynamodb.Table(
            self,
            "DynamoTable",
            table_name=DYNAMODB_TABLE["name"],
            partition_key=dynamodb.Attribute(
                name=DYNAMODB_TABLE["partition_key"],
                type=dynamodb.AttributeType.STRING,
            ),
            billing_mode=dynamodb.BillingMode.PAY_PER_REQUEST,
            removal_policy=RemovalPolicy.DESTROY,
        )
