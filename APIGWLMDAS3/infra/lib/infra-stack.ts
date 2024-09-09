import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3'
// import * as sqs from 'aws-cdk-lib/aws-sqs';

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

  //define s3 
  const mys3bucket = new s3.Bucket(this, 'mydemobuckets3',{
       bucketName : 'demobuckettoday0809',
       versioned: true

  })
 
   
  }
}
