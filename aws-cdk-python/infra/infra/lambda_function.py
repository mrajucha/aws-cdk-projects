
from aws_cdk.aws_lambda import Function, Runtime, Code
from aws_cdk.aws_iam import Role
from constructs import Construct
from aws_cdk import Duration, aws_iam as iam
from aws_cdk import (
    aws_events  as eventRule, 
    aws_events_targets as targets
)
 

class lambdaFunctionforMetric(Construct):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)


        #lambda role should be created before the lambda function (dependency)  
        lambdaRoleforCloudwatchandec2 = Role(
            self, 
            "lambda-instance-count-mteric-Role-cloudwatch",
            role_name= "lambda-Role-cloudwatch-ec2",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
               iam.ManagedPolicy.from_aws_managed_policy_name("CloudWatchFullAccess"),
               iam.ManagedPolicy.from_aws_managed_policy_name("AmazonEC2FullAccess")
            ]
        )

        # Define the Lambda function
        my_lambda = Function(
            self,
            "lambda-instance-count-mteric-Function",
            function_name="lambda-instance-count-mteric-Function",
            runtime=Runtime.PYTHON_3_8,
            handler="lambda_instance_count_metric.lambda_handler",
            #code=Code.from_asset("lambda/lambda_instance_count_metric.py")  # Directory containing the lambda handler
            code=Code.from_asset("infra/lambda"),
            role=lambdaRoleforCloudwatchandec2
            
        )

        ruleToInvokeLambda= eventRule.Rule(
            self,
            "lambda-instance-count-mteric-EventRule",
            rule_name="lambda-instance-count-mteric-EventRule",
            schedule=eventRule.Schedule.rate(Duration.minutes(1)),            
            #targets=[targets.LambdaFunction(my_lambda)]
        )       
        
        ruleToInvokeLambda.add_target(targets.LambdaFunction(my_lambda))

        # attach the roles to lambda function
        # my_lambda.add_to_role_policy(lambdaRoleforEC2)
        # my_lambda.add_to_role_policy(lambdaRoleforCloudwatch)
         
