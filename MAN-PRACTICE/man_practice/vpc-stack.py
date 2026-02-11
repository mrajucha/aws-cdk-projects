from aws_cdk import (
    Stack,
    aws_ec2 as ec2

)
from constructs import Construct

class TestVpcStack(Stack):
    def __init__(self,scope: Construct, cunstruct_id: str, **kwargs):
        super.__init__(scope,construct_id, **kwargs )

        testVpc = ec2.Vpc(

            self,
            "testVpc",
            vpcName = "testVPC",
            ip_addresses= ec2.IpAddress.cidr(cidr),
            maxAzs = 2,
            natGateway =1,

            subnet_configuration =[
                ec2.subnet_configuration(
                    name = "publice-subnet",
                    type = ec2.subnetType.PUBLIC,
                    cidr_mask = 24 
                )
            ]

        )

        testvpc = ec2.Vpc(
           self,
           "testVPC",
           vpcName = "my-test_vpc",
           ip_addresses = ec2.IpAdresses.cidr(cidr),
           maxazs= 2,
           
           subnet_configuration= [
               ec2.subnet_configuration(
                   
               )
           ]


        )
