import boto3

def lambda_handler(event, context):
    cost_client = boto3.client('ce')

    cost_report = cost_client.get_cost_and_usag(
        TimePeriod= {

        }
        Granularity=
        Filte
    )
