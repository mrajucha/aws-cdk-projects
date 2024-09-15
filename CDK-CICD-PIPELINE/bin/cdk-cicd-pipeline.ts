#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { CdkCicdPipelineStack } from '../lib/cdk-cicd-pipeline-stack';

const app = new cdk.App();
new CdkCicdPipelineStack(app, 'CdkCicdPipelineStack', {
  
  env: {account: '381491935825', region:'us-east-1' }
});