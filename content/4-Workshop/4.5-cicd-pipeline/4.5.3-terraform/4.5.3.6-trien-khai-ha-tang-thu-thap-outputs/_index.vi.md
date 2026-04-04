---
title : "Triển khai hạ tầng & Thu thập Outputs"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 4.5.3.6 </b> "
---

#### Mục tiêu

Triển khai hạ tầng theo cấu hình Terraform và xuất outputs phục vụ các bước build/deploy tiếp theo trong pipeline.

#### Nội dung chính

1. Thực thi terraform apply (-auto-approve -input=false) để cập nhật hạ tầng tự động theo cấu hình IaC trong các file .tf ở thư mục Terraform; giá trị biến được lấy từ terraform.tfvars được inject từ GitHub Secrets. Terraform so sánh state hiện tại với cấu hình mong muốn, sau đó tạo/điều chỉnh/xoá tài nguyên theo sự khác biệt đó.

2. Đọc outputs từ Terraform và ghi vào $GITHUB_OUTPUT để các job downstream sử dụng nhất quán.

💡 $GITHUB_OUTPUT là cơ chế chuẩn trong GitHub Actions để truyền dữ liệu giữa các job, giúp liên kết các bước triển khai mà không cần truyền biến thủ công.

**Trích đoạn cấu hình liên quan**

```yaml
- name: Terraform Apply
  working-directory: ${{ env.TF_DIR }}
  run: terraform apply -auto-approve -input=false

- name: Get Terraform Outputs
  id: tf_output
  working-directory: ${{ env.TF_DIR }}
  run: |
    echo "asg_name=$(terraform output -raw backend_asg_name)" >> "$GITHUB_OUTPUT"
    echo "aws_region=$(terraform output -raw aws_region)" >> "$GITHUB_OUTPUT"
    echo "ecr_repository_url=$(terraform output -raw ecr_repository_url)" >> "$GITHUB_OUTPUT"
    echo "backend_port=$(terraform output -raw backend_port)" >> "$GITHUB_OUTPUT"
    echo "secrets_kms_key_arn=$(terraform output -raw secrets_kms_key_arn)" >> "$GITHUB_OUTPUT"
    echo "alb_dns_name=$(terraform output -raw alb_dns_name)" >> "$GITHUB_OUTPUT"
    echo "api_domain_name=$(terraform output -raw api_domain_name)" >> "$GITHUB_OUTPUT"
    echo "backend_target_group_arn=$(terraform output -raw backend_target_group_arn)" >> "$GITHUB_OUTPUT"
```
