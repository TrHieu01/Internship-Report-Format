---
title : "Các tài nguyên được tạo sau khi chạy Terraform"
date : 2024-01-01
weight : 7
chapter : false
pre : " <b> 4.5.3.7 </b> "
---

#### Tổng quan

Phần này tổng hợp các tài nguyên AWS được tạo hoặc cập nhật sau khi chạy `terraform apply`. Đưa hình chụp màn hình hoặc output kiểm tra tại đây (AWS Console, CLI, hoặc dashboard) để chứng minh hạ tầng đã được provision đúng.

#### Network & VPC

**VPC**

![VPC](vpc.png)

**Subnets**

![Subnets](subnets.png)

**Route Tables**

![Route Tables](route-tables.png)

**NAT Gateway**

![NAT Gateway](nat-gateway.png)

**Elastic IP**

![Elastic IP](elastic-ip.png)

**VPC Endpoints**

![VPC Endpoints](vpc-endpoints.png)

**Security Groups**

![Security Groups](security-groups.png)

#### Load Balancer & Routing

**Application Load Balancer (ALB)**

![ALB](alb.png)

**Target Group (Summary)**

![Target Group Summary](target-group-summary.png)

**Target Group (Targets)**

![Target Group Targets](target-group-targets.png)

#### Compute

**Launch Template**

![Launch Template](launch-template.png)

**Auto Scaling Group**

![Auto Scaling Group](asg.png)

#### Storage

**S3 Buckets**

![S3 Buckets](s3-buckets.png)

#### IAM & Security

**Backend IAM Role & Instance Profile**

![Backend IAM Role](iam-backend-role.png)

**EC2 Instances (Instance Profile)**

![EC2 Instances - Instance Profile](instance-profile.png)

**VPC Flow Log IAM Role**

![VPC Flow Log IAM Role](iam-vpc-flow-log-role.png)

**KMS Key**

![KMS Key](kms-key.png)

**SSM Parameter**

![SSM Parameter](ssm-parameter.png)

#### Identity (Cognito)

**User Pool**

![Cognito User Pool](cognito-user-pool.png)

**App Client**

![Cognito App Client](cognito-app-client.png)

**Users**

![Cognito Users](cognito-users.png)

**Groups**

![Cognito Groups](cognito-groups.png)

#### Observability

**CloudWatch Log Groups**

![CloudWatch Log Groups](cloudwatch-log-groups.png)

**CloudWatch Alarms**

![CloudWatch Alarms](cloudwatch-alarms.png)

**SNS Topic**

![SNS Topic](sns-topic.png)

#### Container Registry

**ECR Repository**

![ECR Repository](ecr-repo.png)

**ECR Images**

![ECR Images](ecr-images.png)

#### WAF

**Web Application Firewall**

![WAF](waf.png)
