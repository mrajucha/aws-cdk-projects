

resource "aws_sqs_queue" "testDLQ"{
   name = "testDLQ"
   message_retention_seconds = 345600 
}

resource "aws_sqs_queue" "testMainQueue"{
    name = "TestMainQueue"
    #fifo_queue = true  --> to make the type queue fifo else it would be standerd
    visibility_timeout_seconds = 30
    max_message_size = 2048
    message_retention_seconds = 345600 
    redrive_policy = jsondecode(
        {
            deadletterQueueARN = ""
            max_received_count = 4
        }
    )

    tags = {
      
    }
}