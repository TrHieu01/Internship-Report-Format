---
title : "Terraform Variables"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.4.1 </b> "
---

#### terraform.tfvars.example

1. **Infrastructure**: VPC, subnet, AZ, CIDR.
2. **Compute**: instance type, ASG size.
3. **Storage**: S3 buckets, ECR repo.
4. **Database**: engine, size, username.
5. **Security**: SSH CIDR, allowed origins.

#### Sample values

+ `region = "us-east-1"`
+ `asg_min = 1`, `asg_max = 3`
+ `db_engine = "postgres"`
