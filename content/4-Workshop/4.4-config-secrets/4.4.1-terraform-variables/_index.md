---
title : "Terraform Variable Setup"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.4.1 </b> "
---

#### 1. Region & Resource Names

| Variable Name | Description |
| --- | --- |
| **aws_region** | Deployment Region |
| **ec2_instance_name** | Backend EC2 instance name |
| **vpc_name** | Backend VPC name |
| **igw_name** | Internet Gateway name |

#### 2. Compute & ASG

| Variable Name | Description |
| --- | --- |
| **ec2_instance_type** | EC2 Configuration |
| **asg_min_size** | Minimum number of instances |
| **asg_max_size** | Maximum number of instances |
| **asg_desired_capacity** | Desired number of instances |
| **backend_port** | Backend service port |

#### 3. ECR & Image

| Variable Name | Description |
| --- | --- |
| **ecr_repository_name** | Repository for backend images |
| **ecr_tag_immutable** | Enable/disable tag immutability |
| **backend_image_tag** | Image tag for deployment |

#### 4. Network (VPC/Subnet)

| Variable Name | Description |
| --- | --- |
| **vpc_cidr_block** | VPC CIDR block |
| **private_subnet_1a_cidr** | Private Subnet CIDR for AZ 1a |
| **private_subnet_1c_cidr** | Private Subnet CIDR for AZ 1c |
| **public_subnet_1a_cidr** | Public Subnet CIDR for AZ 1a |
| **public_subnet_1c_cidr** | Public Subnet CIDR for AZ 1c |

#### 5. Egress CIDRs

| Variable Name | Description |
| --- | --- |
| **docdb_egress_cidr_blocks** | CIDR for DocDB egress |
| **redis_egress_cidr_blocks** | CIDR for Redis egress |
| **dns_egress_cidr_blocks** | CIDR for DNS egress |

#### 6. Domain & Cognito

| Variable Name | Description |
| --- | --- |
| **domain_name** | Frontend domain |
| **cognito_domain_prefix** | Cognito domain prefix |
| **enable_api_custom_domain** | Enable/disable API custom domain |
| **api_domain_name** | API domain |
| **route53_zone_id** | Hosted Zone ID |
| **certificate_arn** | ACM Certificate ARN (if available) |

#### 7. S3 & Endpoint Services

| Variable Name | Description |
| --- | --- |
| **frontend_bucket_name** | Bucket for frontend assets |
| **camera_detect_bucket_name** | Log bucket for camera detection |
| **s3_endpoint_service_name** | S3 Endpoint service name |
| **ecr_dkr_endpoint_service_name** | ECR Docker Endpoint service name |
| **ecr_api_endpoint_service_name** | ECR API Endpoint service name |
| **ssm_endpoint_service_name** | SSM Endpoint service name |
| **sts_endpoint_service_name** | STS Endpoint service name |
| **logs_endpoint_service_name** | CloudWatch Logs Endpoint service name |

#### 8. Frontend WAF

| Variable Name | Description |
| --- | --- |
| **enable_frontend_waf** | Enable/disable WAF |
| **frontend_cloudfront_distribution_id** | CloudFront Distribution ID |
| **frontend_waf_rate_limit** | WAF Rate limit |

#### 9. Monitoring & Alarms

| Variable Name | Description |
| --- | --- |
| **enable_alarms** | Enable/disable alarms |
| **alarm_email** | Email for receiving alerts |

#### Sample Values (copy once)

```hcl
aws_region = "ap-southeast-1"
ec2_instance_type = "t3.small"
ec2_instance_name = "fcaj-proj-backend"
ecr_repository_name = "edutrust-backend"
ecr_tag_immutable = false
asg_min_size = 2
asg_max_size = 4
asg_desired_capacity = 2
backend_image_tag = "latest"
docdb_egress_cidr_blocks = ["0.0.0.0/0"]
redis_egress_cidr_blocks = ["0.0.0.0/0"]
dns_egress_cidr_blocks = ["0.0.0.0/0"]
vpc_cidr_block = "10.0.0.0/16"
private_subnet_1a_cidr = "10.0.1.0/24"
private_subnet_1c_cidr = "10.0.2.0/24"
public_subnet_1a_cidr = "10.0.101.0/24"
public_subnet_1c_cidr = "10.0.102.0/24"
vpc_name = "my-backend-vpc"
igw_name = "my-backend-igw"
backend_port = 8000
domain_name = "edu-trust.app"
cognito_domain_prefix = "edutrust-auth"
frontend_bucket_name = "edutrust-frontend-assets"
s3_endpoint_service_name = "com.amazonaws.ap-southeast-1.s3"
ecr_dkr_endpoint_service_name = "com.amazonaws.ap-southeast-1.ecr.dkr"
ecr_api_endpoint_service_name = "com.amazonaws.ap-southeast-1.ecr.api"
ssm_endpoint_service_name = "com.amazonaws.ap-southeast-1.ssm"
sts_endpoint_service_name = "com.amazonaws.ap-southeast-1.sts"
logs_endpoint_service_name = "com.amazonaws.ap-southeast-1.logs"
enable_api_custom_domain = true
api_domain_name = "api.edu-trust.app"
route53_zone_id = "Z03182776BZZ04ZU2533"
certificate_arn = ""
camera_detect_bucket_name = "log-camera-detect-cheating-0293839182"
enable_frontend_waf = true
frontend_cloudfront_distribution_id = "E1234567890ABC"
frontend_waf_rate_limit = 2000
enable_alarms = true
alarm_email = "your-email@example.com"
```

#### Note: Variables obtained from AWS Console (do not make these up)

1. **route53_zone_id**  
   - Go to AWS Console → Route 53 → Hosted Zones.  
   - Select your domain → Copy the Hosted Zone ID.
2. **certificate_arn**  
   - Go to AWS Console → ACM.  
   - Select the certificate → Copy the ARN.  
   - If Terraform is creating the ACM automatically, leave this empty.
3. **frontend_cloudfront_distribution_id**  
   - Go to AWS Console → CloudFront.  
   - Select the frontend distribution → Copy the ID.
4. **alarm_email**  
   - The email address for SNS notifications (use a real email and confirm the subscription).

#### Note: Region-specific Endpoint Services

+ **s3_endpoint_service_name**
+ **ecr_dkr_endpoint_service_name**
+ **ecr_api_endpoint_service_name**
+ **ssm_endpoint_service_name**
+ **sts_endpoint_service_name**
+ **logs_endpoint_service_name**

These variables must match the region you are using (e.g., `ap-southeast-1`). Do not modify them unless you are sure.
