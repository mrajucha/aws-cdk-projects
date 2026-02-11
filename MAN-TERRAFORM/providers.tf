
terraform {
  required_providers{
    aws = {
        source = "hashicorp/aws"
        version = "6.21.0"       // aws prvider plugin version which terraform uses.
    }
  }
}

provider "aws" {
    region = "us-east-1"
  
}