import aws_cdk as core
import aws_cdk.assertions as assertions

from man_practice.man_practice_stack import ManPracticeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in man_practice/man_practice_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ManPracticeStack(app, "man-practice")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
