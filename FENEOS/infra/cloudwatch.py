from aws_cdk import Stack
#import aws_cdk.aws_cloudwatch as cw 
from aws_cdk.aws_cloudwatch import Dashboard, Metric
from constructs import Construct



class CloudWatchDashboard(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs ):
        super().__init(scope,construct_id,**kwargs):



