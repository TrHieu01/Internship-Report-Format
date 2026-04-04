---
title : "S3 lưu trữ file Terraform State"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 4.5.3.4 </b> "
---

#### Mục tiêu

Tạo nơi lưu trữ Terraform state file trước khi chạy terraform init, nhằm đảm bảo việc quản lý danh sách tài nguyên được tạo bởi IaC luôn nhất quán và có thể truy vết.

<small><i>Terraform state file là bản ghi trạng thái hiện tại của hạ tầng, dùng để so sánh và xác định thay đổi khi chạy Terraform; vì vậy cần lưu trữ riêng, an toàn và có kiểm soát.</i></small>

#### Nội dung chính

State file của Terraform là nguồn dữ liệu quan trọng phản ánh trạng thái hạ tầng thực tế và được dùng để tính toán thay đổi khi chạy apply. Vì vậy, state cần được lưu trữ ở một backend riêng, ổn định và an toàn. Trong dự án này, S3 được lựa chọn làm nơi lưu trữ state thông qua bước **Ensure Terraform State Bucket Exists**.

Giải thích logic:

1. Kiểm tra bucket đã tồn tại hay chưa.
2. Nếu chưa, tạo bucket với LocationConstraint phù hợp.
3. Hardening bắt buộc: block public access, bật versioning, bật encryption AES256.

💡 Đây là best practice quan trọng vì state bucket phải tồn tại trước khi terraform init chạy và luôn cần được bảo mật.

**Trích đoạn cấu hình liên quan**

```yaml
- name: Ensure Terraform State Bucket Exists
  shell: bash
  run: |
    set -euo pipefail
    bucket="${TF_STATE_BUCKET}"
    region="${TF_STATE_REGION}"
    if aws s3api head-bucket --bucket "${bucket}" --region us-east-1 2>/dev/null; then
      echo "Bucket exists, skipping create."
    else
      if [ "${region}" = "us-east-1" ]; then
        aws s3api create-bucket --bucket "${bucket}" --region "${region}"
      else
        aws s3api create-bucket \
          --bucket "${bucket}" \
          --region "${region}" \
          --create-bucket-configuration LocationConstraint="${region}"
      fi
    fi
    aws s3api put-public-access-block \
      --bucket "${bucket}" \
      --public-access-block-configuration '{
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
      }'
    aws s3api put-bucket-versioning \
      --bucket "${bucket}" \
      --versioning-configuration Status=Enabled
    aws s3api put-bucket-encryption \
      --bucket "${bucket}" \
      --server-side-encryption-configuration '{
        "Rules": [
          { "ApplyServerSideEncryptionByDefault": { "SSEAlgorithm": "AES256" } }
        ]
      }'
```
