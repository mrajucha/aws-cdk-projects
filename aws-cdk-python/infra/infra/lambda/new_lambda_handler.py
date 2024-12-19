import boto3

# Initialize boto3 clients
ec2 = boto3.client('ec2')
cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    instance_counts = {}  # Dictionary to track count per instance type
    
    # Describe all EC2 instances
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_type = instance['InstanceType']  # Get instance type
            # Increment count for this instance type
            if instance_type in instance_counts:
                instance_counts[instance_type] += 1
            else:
                instance_counts[instance_type] = 1
    
    # Publish the count for each instance type as a custom CloudWatch metric
    for instance_type, count in instance_counts.items():
        cloudwatch.put_metric_data(
            Namespace='EC2',
            MetricData=[
                {
                    'MetricName': 'InstanceCount',
                    'Dimensions': [
                        {
                            'Name': 'InstanceType',
                            'Value': instance_type  # Group by instance type
                        }
                    ],
                    'Value': count,
                    'Unit': 'Count'
                },
            ]
        )
    
    return {
        'statusCode': 200,
        'body': f"Successfully published EC2 instance count per type: {instance_counts}"
    }
