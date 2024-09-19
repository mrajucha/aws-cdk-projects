import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'


export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // create s3 bucket to store the json files
    const s3bucketforjson = new s3.Bucket(this,'s3bucketforjson',{
      bucketName : "manojc435",
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL, // default deny 
      versioned: false,

    })

    // create lambda function to trigger when json files are store in s3

    const lamdafuncfors3 = new lambda.Function(this,'lambdafuncfors3',{        // case sensitive l small F capital or wont work
           code : lambda.Code.fromAsset('../app'),
           handler : "lambda_function.lambda_handler",
           runtime : lambda.Runtime.PYTHON_3_11
    })

    // create dynamodb to store the data from s3 

    const dbTostoreFromS3 = new dynamodb.TableV2(this, 'dbTostoreFromS3',{
      partitionKey: { name: 'dbToStoreData', type: dynamodb.AttributeType.STRING },
      
    })

  }
}
