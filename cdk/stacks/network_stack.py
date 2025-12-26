from constructs import Construct
from aws_cdk import Stack
from aws_cdk import aws_ec2 as ec2
from .config import VPC_CONFIG

class NetworkStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        self.vpc = ec2.Vpc(
            self,
            "Vpc",
            cidr=VPC_CONFIG["cidr"],
            max_azs=VPC_CONFIG["max_azs"],
            nat_gateways=1,
        )

