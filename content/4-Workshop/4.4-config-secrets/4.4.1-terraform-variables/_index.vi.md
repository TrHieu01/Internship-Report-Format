---
title : "Cài đặt biến Terraform"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.4.1 </b> "
---

1. **Nhóm vùng & tên tài nguyên**

| Tên biến | Mô tả |
| --- | --- |
| **aws_region** | Region triển khai |
| **ec2_instance_name** | Tên EC2 instance backend |
| **vpc_name** | Tên VPC backend |
| **igw_name** | Tên Internet Gateway |

2. **Nhóm compute & ASG**

| Tên biến | Mô tả |
| --- | --- |
| **ec2_instance_type** | Cấu hình EC2 |
| **asg_min_size** | Số instance tối thiểu |
| **asg_max_size** | Số instance tối đa |
| **asg_desired_capacity** | Số instance mong muốn |
| **backend_port** | Cổng backend service |

3. **Nhóm ECR & image**

| Tên biến | Mô tả |
| --- | --- |
| **ecr_repository_name** | Repo chứa image backend |
| **ecr_tag_immutable** | Bật/tắt immutable tag |
| **backend_image_tag** | Tag image deploy |

4. **Nhóm network (VPC/Subnet)**

| Tên biến | Mô tả |
| --- | --- |
| **vpc_cidr_block** | Dải mạng VPC |
| **private_subnet_1a_cidr** | Subnet private AZ 1a |
| **private_subnet_1c_cidr** | Subnet private AZ 1c |
| **public_subnet_1a_cidr** | Subnet public AZ 1a |
| **public_subnet_1c_cidr** | Subnet public AZ 1c |

5. **Nhóm egress CIDR**

| Tên biến | Mô tả |
| --- | --- |
| **docdb_egress_cidr_blocks** | CIDR cho DocDB egress |
| **redis_egress_cidr_blocks** | CIDR cho Redis egress |
| **dns_egress_cidr_blocks** | CIDR cho DNS egress |

6. **Nhóm domain & Cognito**

| Tên biến | Mô tả |
| --- | --- |
| **domain_name** | Domain frontend |
| **cognito_domain_prefix** | Prefix domain Cognito |
| **enable_api_custom_domain** | Bật/tắt domain API |
| **api_domain_name** | Domain API |
| **route53_zone_id** | Hosted Zone ID |
| **certificate_arn** | ARN chứng chỉ ACM (nếu có) |

7. **Nhóm S3 & endpoint services**

| Tên biến | Mô tả |
| --- | --- |
| **frontend_bucket_name** | Bucket chứa asset frontend |
| **camera_detect_bucket_name** | Bucket log camera detect |
| **s3_endpoint_service_name** | Endpoint service S3 |
| **ecr_dkr_endpoint_service_name** | Endpoint service ECR Docker |
| **ecr_api_endpoint_service_name** | Endpoint service ECR API |
| **ssm_endpoint_service_name** | Endpoint service SSM |
| **sts_endpoint_service_name** | Endpoint service STS |
| **logs_endpoint_service_name** | Endpoint service CloudWatch Logs |

8. **Nhóm WAF frontend**

| Tên biến | Mô tả |
| --- | --- |
| **enable_frontend_waf** | Bật/tắt WAF |
| **frontend_cloudfront_distribution_id** | CloudFront distribution ID |
| **frontend_waf_rate_limit** | Rate limit WAF |

9. **Nhóm Monitoring & Alarms**

| Tên biến | Mô tả |
| --- | --- |
| **enable_alarms** | Bật/tắt alarms |
| **alarm_email** | Email nhận cảnh báo |

#### Giá trị mẫu (copy một lần)

```
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
alarm_email = "ntthanh14052005@gmail.com"
```

#### Lưu ý: biến lấy từ AWS Console (không tự đặt)

1. **route53_zone_id**  
   + Vào AWS Console → Route 53 → Hosted Zones.  
   + Chọn domain → lấy Hosted Zone ID.
2. **certificate_arn**  
   + Vào AWS Console → ACM.  
   + Chọn certificate → copy ARN.  
   + Nếu Terraform tự tạo ACM thì để rỗng.
3. **frontend_cloudfront_distribution_id**  
   + Vào AWS Console → CloudFront.  
   + Chọn distribution của frontend → copy ID.
4. **alarm_email**  
   + Email nhận thông báo từ SNS (dùng email thật để xác nhận).

#### Lưu ý: biến endpoint service theo region

+ **s3_endpoint_service_name**
+ **ecr_dkr_endpoint_service_name**
+ **ecr_api_endpoint_service_name**
+ **ssm_endpoint_service_name**
+ **sts_endpoint_service_name**
+ **logs_endpoint_service_name**

Những biến này phải đúng theo region bạn dùng (ví dụ `ap-southeast-1`). Không tự sửa nếu không chắc.
