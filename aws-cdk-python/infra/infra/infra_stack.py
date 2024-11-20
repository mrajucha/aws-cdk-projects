from aws_cdk import (
    # Duration,
    Stack,
    # aws_sqs as sqs,
)
from constructs import Construct
import aws_cdk.aws_cloudwatch as cloudwatch


class InfraStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.create_cloudwatch_dashboard()

    def create_cloudwatch_dashboard(self):
        dashboard = cloudwatch.Dashboard(self, "MyDashboard", dashboard_name="My_Dashboard")   

        # Add widgets to the dashboard
        dashboard.add_widgets(
            cloudwatch.GraphWidget(
                title="CPU Utilization",
                left=[
                    cloudwatch.Metric(
                        namespace="AWS/EC2",
                        metric_name="CPUUtilization",
                        dimensions_map={
                            "InstanceId": "${InstanceId}"
                        },
                        label = "${InstanceId}",
                        statistic="Average"
                    )
                ],
                width=24
            )
        )  
        
        # Add a search widget to show running instances
        dashboard.add_widgets(
            cloudwatch.TextWidget(
                markdown="# Running EC2 Instances",
                width=24,
                height=1
            ),
            cloudwatch.LogQueryWidget(
                title="Running EC2 Instances",
                log_group_names=["/aws/ec2/instance"],
                query_string="""
                fields @timestamp, detail.instance-id as InstanceId
                | filter detail.state = "running"
                | stats count() by InstanceId
                | sort count() desc
                """,
                width=24,
                height=6
            )
        )