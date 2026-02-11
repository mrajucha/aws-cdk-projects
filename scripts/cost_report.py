import boto3
import datetime
import json

def lambda_handler(context, event):
   ce_client = boto3.client("ce")
   