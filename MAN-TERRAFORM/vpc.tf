

resource "aws_vpc" "testVPC" {
    cidr_block = var.cidr_block
    enable_dns_hostnames = true
    enable_dns_support =  true

    tags = {
      
    }
}


resource "aws_subnet" "testSubnet"{
    vpc_id = aws_vpc.testVPC.id
    cidr_block = var.cidr_block
    availability_zone = var.availability_zone
    map_public_ip_on_launch = true

    tags = {
      type = "public"
    }
}