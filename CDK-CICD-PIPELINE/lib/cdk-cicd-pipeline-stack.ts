import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import { Pipeline } from 'aws-cdk-lib/aws-codepipeline';
import { CodePipeline, ShellStep, CodePipelineSource } from 'aws-cdk-lib/pipelines';

export class CdkCicdPipelineStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here

    // example resource
    // const queue = new sqs.Queue(this, 'CdkCicdPipelineQueue', {
    //   visibilityTimeout: cdk.Duration.seconds(300)
    // });
 // create codepipeline 
 
 const democodecicd = new CodePipeline(this, 'democodecicd',{
    synth: new ShellStep('Synth', {
    // Use a connection created using the AWS console to authenticate to GitHub
    // Other sources are available.
    input: CodePipelineSource.gitHub(
      'mrajucha/aws-cdk-projects',  
      'main',{}
    ),
    commands: ['cd CDK-CICD-PIPELINE','npm ci', 'npm run build', 'npx cdk synth'],
  }),

 })

  }
}
