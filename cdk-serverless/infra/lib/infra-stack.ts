import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3'
import * as lambda from 'aws-cdk-lib/aws-lambda'
import * as dynamodb from 'aws-cdk-lib/aws-dynamodb'
import * as IAM from 'aws-cdk-lib/aws-iam'

export class InfraStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // create s3 bucket to store the json files
    const s3bucketforjson = new s3.Bucket(this,'s3bucketforjson',{
      bucketName : "manojc4352009",
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL, // default deny 
      versioned: false,

    })

      // Create IAM role for lambda to access s3
      const lambdaRolefors3 = new IAM.Role(this,'lambdaRolefors3',{
        roleName: 'lambdaRolefors3',
        description: 'to access s3',
        assumedBy: new IAM.ServicePrincipal('lambda.amazonaws.com')
    })
    lambdaRolefors3.addManagedPolicy(IAM.ManagedPolicy.fromAwsManagedPolicyName('AmazonS3FullAccess'))
    lambdaRolefors3.addManagedPolicy(IAM.ManagedPolicy.fromAwsManagedPolicyName('AmazonDynamoDBFullAccess'))

    // create lambda function to trigger when json files are store in s3
    const lamdafuncfors3 = new lambda.Function(this,'lambdafuncfors3',{        // case sensitive l small F capital or wont work
           code : lambda.Code.fromAsset('../app'),
           handler : "lambda_function.lambda_handler",
           runtime : lambda.Runtime.PYTHON_3_11,
           role: lambdaRolefors3,
           functionName : 'lamdafuncfors3'
           
    })
    // Add dependecy to role before lambda 
    lamdafuncfors3.node.addDependency(lambdaRolefors3)
 

    // create dynamodb to store the data from s3 
    const dbTostoreFromS3 = new dynamodb.TableV2(this, 'dbTostoreFromS3',{
      partitionKey: { name: 'customerData', type: dynamodb.AttributeType.STRING },
      tableName: 'tableTostoreJson2209'
      
    })

  }
}
