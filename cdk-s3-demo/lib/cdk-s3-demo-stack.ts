import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
// import * as sqs from 'aws-cdk-lib/aws-sqs';
import * as s3 from 'aws-cdk-lib/aws-s3'

export class CdkS3DemoStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'CdkS3DemoQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
    const s3demobucket = new s3.Bucket(this, 's3demobucke,t',{
      bucketName: 'demobucket-manoj',
      versioned: true,
      publicReadAccess: false
  
    })
  
  }
}
