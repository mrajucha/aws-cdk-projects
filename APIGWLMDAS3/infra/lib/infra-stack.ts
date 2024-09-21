import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3'
import * as iam from 'aws-cdk-lib/aws-iam'
import { Lambda } from 'aws-cdk-lib/aws-ses-actions';
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as apigateway from 'aws-cdk-lib/aws-apigateway'
import assert = require('assert');

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

  //define s3 
  const mys3bucket = new s3.Bucket(this, 'mydemobuckets3',{
       bucketName : 'demobuckettoday6408898656860809',
       versioned: true
  })
 
  // create IAM role
  const lamdarole = new iam.Role(this,' myrole' ,{
    roleName: 'lambdaRole',
    description: 'The role is to access the s3 bucket',
    assumedBy: new iam.ServicePrincipal('lambda.amazonaws.com')
  }) 
  lamdarole.addManagedPolicy(iam.ManagedPolicy.fromAwsManagedPolicyName('AmazonS3FullAccess')); 

  const bankingLambda = new lambda.Function(this, 'bankingLambda',{
   code: lambda.Code.fromAsset('../app'),
   handler:"lambda_function.lambda_handler",
   runtime: lambda.Runtime.PYTHON_3_8,  //should declare first to avoid onscreen error
   role: lamdarole
  })
 
  // Create API gateway
  const bankstatusapi = new apigateway.LambdaRestApi(this,'bankstatusapi', {
    handler: bankingLambda,
    restApiName: "bankstatusapi",
    deploy: true,
    proxy: false

  })
  const bankstatus = bankstatusapi.root.addResource('bankstatus');
  bankstatus.addMethod('GET');
  


 

  }
}

