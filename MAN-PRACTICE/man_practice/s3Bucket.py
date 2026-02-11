from aws_cdk import (
    Stack,
    aws_s3 as s3
)

from constructs import Construct



class S3BucketTest(Stack):
    
    def __init__(self,scope: Construct ,construct_id: str, **kwargs):
       super().__init(scope, construct_id, **kwargs )

       bucket = s3.Bucket(
           self,
           "testBucket",
           bucket_name = "testBucket",
           versioned = True,
           removel_policy = RemovalPolicy.DESTROY,

       )
    





