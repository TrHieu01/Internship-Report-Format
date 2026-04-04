---
title : "Khởi tạo & Import Terraform State"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 4.5.3.5 </b> "
---

#### Mục tiêu

Thiết lập kết nối backend state và đồng bộ trạng thái Terraform với hạ tầng thực tế để tránh sai lệch khi triển khai.

#### Nội dung chính

1. Thực hiện terraform init để liên kết backend lưu trữ state (S3), đảm bảo state được đọc/ghi đúng nơi lưu trữ.
2. Import ECR repository nếu tài nguyên đã tồn tại, đưa tài nguyên vào state để tránh xung đột khi apply.

💡 State drift là hiện tượng trạng thái trong state khác với hạ tầng thực tế. Import giúp đồng bộ trạng thái và giảm rủi ro lỗi “resource already exists”.

**Giải thích**

- Khởi tạo backend để Terraform có thể đọc/ghi state đúng vị trí lưu trữ.

  ```bash
  terraform init
  ```

- Đọc tên ECR repository từ terraform.tfvars (nếu có), sau đó kiểm tra repository đã tồn tại trong AWS hay chưa.

  ```bash
  REPO_NAME="$(awk -F= '... ecr_repository_name ...' terraform.tfvars || true)"
  aws ecr describe-repositories --repository-names "$REPO_NAME"
  ```

- Mục đích là xác định tài nguyên đã được tạo thủ công hay từ lần chạy trước, từ đó tránh xung đột tên và hạn chế lỗi khi Terraform tạo lại repository.

- Nếu ECR đã tồn tại nhưng chưa có trong state, thực hiện import để đồng bộ; nếu chưa tồn tại thì để Terraform tự tạo khi apply.

  ```bash
  terraform state show aws_ecr_repository.backend
  terraform import aws_ecr_repository.backend "$REPO_NAME"
  ```

**Trích đoạn cấu hình liên quan**

```yaml
- name: Terraform Init
  working-directory: ${{ env.TF_DIR }}
  run: terraform init

- name: Import existing ECR repository (if already created)
  working-directory: ${{ env.TF_DIR }}
  run: |
    set -euo pipefail
    if [ -f terraform.tfvars ]; then
      REPO_NAME="$(awk -F= '
        $1 ~ /^[[:space:]]*ecr_repository_name[[:space:]]*$/ {
          v=$2
          gsub(/^[[:space:]]+|[[:space:]]+$/, "", v)
          gsub(/\"/, "", v)
          print v
          exit
        }' terraform.tfvars || true)"
    fi
    REPO_NAME="${REPO_NAME:-edutrust-backend}"
    if aws ecr describe-repositories --repository-names "$REPO_NAME" >/dev/null 2>&1; then
      if terraform state show aws_ecr_repository.backend >/dev/null 2>&1; then
        echo "ECR repo already in Terraform state, skipping import."
      else
        terraform import aws_ecr_repository.backend "$REPO_NAME"
      fi
    else
      echo "ECR repo not found in AWS; Terraform will create it."
    fi
```
