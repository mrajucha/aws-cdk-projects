from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_iam as iam,
    Duration
)
from constructs import Construct

class CostReportStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        # Lambda function
        cost_report_lambda = _lambda.Function(
            self, "CostReportLambda",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="cost-report.lambda_handler",
            code=_lambda.Code.from_asset("lambda-automation-scripts"),
            timeout=Duration.minutes(5)
        )
        
        # IAM permissions
        cost_report_lambda.add_to_role_policy(
            iam.PolicyStatement(
                actions=["ce:GetCostAndUsage"],
                resources=["*"]
            )
        )
        
        cost_report_lambda.add_to_role_policy(
            iam.PolicyStatement(
                actions=["ses:SendEmail", "ses:SendRawEmail"],
                resources=["*"]
            )
        )
        
        # Daily schedule
        events.Rule(
            self, "DailyCostReportRule",
            schedule=events.Schedule.cron(hour="9", minute="0"),
            targets=[targets.LambdaFunction(cost_report_lambda)]
        )