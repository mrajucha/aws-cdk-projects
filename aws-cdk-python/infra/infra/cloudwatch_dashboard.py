
from aws_cdk import (
    Duration,
    Stack,
)
from constructs import Construct
import aws_cdk.aws_cloudwatch as cloudwatch


class CloudWatchDashboard(Construct):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #define custom metric
        total_instance = cloudwatch.Metric(
            metric_name="TotalInstanceCountMetric", # Metric name should be same as provided in Lambda
            namespace="Dummy custom Namespace",  # namespace should be same as provided in lambda
            # dimensions_map={
            #      "LambdaFunctionName": "lambda_function"
            # },
            statistic="Maximum",
            period=Duration.minutes(1)
            
        )

        total_instance_widget = cloudwatch.GraphWidget(
            title="Total Instance",
            left=[total_instance]
        ) 

         #define dashboard
        dashboard = cloudwatch.Dashboard(self, "Dashboard", dashboard_name="Total Instance Count Dashboard")   

        # Add widgets to the dashboard
        dashboard.add_widgets(
            total_instance_widget
        )
      