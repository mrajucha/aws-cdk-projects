from aws_cdk import (

    Stack,
    aws_sqs as sqs,
    Duration
)

from constructs import Construct


class testSQSQueue(Stack):
    def __init__(self, scope: Construct, constructs_id: str, **kwargs):
        super.__init__(self,constructs_id,**kwargs)

        testQueue= sqs.Queue(
           self,
           "testQueue",
           queueName = "testQueue",
           visibility_timeout = Duration.seconds(30)

        )



