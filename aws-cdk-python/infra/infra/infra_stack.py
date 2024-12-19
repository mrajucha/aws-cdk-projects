from aws_cdk import (
    # Duration,
    Stack,
)
from constructs import Construct
import aws_cdk.aws_cloudwatch as cloudwatch
import aws_cdk.aws_lambda as lambdaFunction
import infra.lambda_function as lfn
import infra.cloudwatch_dashboard as cld


class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        lambda_fn = lfn.lambdaFunctionforMetric(self, "lambdaFunctionforMetric")

        clwatch_dashboard = cld.CloudWatchDashboard(self, "CloudWatchDashboard")
     

     

   
       