#!/usr/bin/env python3
import aws_cdk as cdk
from cost_report_stack import CostReportStack

app = cdk.App()
CostReportStack(app, "CostReportStack")
app.synth()