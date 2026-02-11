

import boto3
import os

def lambda_handler(event, context):

    dynamo_client = boto3.client("dynamo")

    result = dynamo_client.scan("demo_table")

    for res in result[] :



 return{
     output 
 }       


def lambda_handler(event, context):

    s3_client = boto3.client("s3")
    module_bucket = os.env.module_bucket

    result = s3_client.getObject("module_bbucket")
    