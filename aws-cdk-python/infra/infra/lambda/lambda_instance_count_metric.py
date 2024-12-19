import boto3

# Initialize boto3 clients
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    count = 0
    
    # Describe all instances
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        count += len(reservation['Instances'])  # Count instances
    
    # Publish the count as a custom CloudWatch metric
    cloudwatch.put_metric_data(
        Namespace='Dummy custom Namespace',
        MetricData=[
            {
                'MetricName': 'TotalInstanceCountMetric',
                'Value': count,  # Use 'Value' instead of 'StatisticValues'
                'Unit': 'Count'
            },
        ]
    )
    
    return {
        'statusCode': 200,
        'body': f"Successfully published EC2 instance count: {count}"
    }
