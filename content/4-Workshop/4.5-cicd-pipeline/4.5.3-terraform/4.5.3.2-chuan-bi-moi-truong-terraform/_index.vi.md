---
title : "Chuẩn bị môi trường Terraform"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.5.3.2 </b> "
---

#### Mục tiêu

Thiết lập môi trường Terraform theo chuẩn CI/CD để đảm bảo tính nhất quán và an toàn cấu hình.

#### Các bước thực hiện

1. Checkout code.
2. Cache Terraform plugins để tối ưu thời gian chạy.
3. Setup Terraform đúng version 1.14.6.
4. Write terraform.tfvars từ GitHub Secrets để inject biến nhạy cảm.

💡 Không commit terraform.tfvars vào repo để tránh rò rỉ thông tin. GitHub Secrets là cơ chế chuẩn để inject cấu hình nhạy cảm trong CI/CD.

**Trích đoạn cấu hình liên quan**

```yaml
- name: Checkout code
  uses: actions/checkout@v4

- name: Cache Terraform plugins
  uses: actions/cache@v4
  with:
    path: ~/.terraform.d/plugin-cache
    key: ${{ runner.os }}-terraform-${{ hashFiles('.github/terraform/*.tf') }}
    restore-keys: |
      ${{ runner.os }}-terraform-

- name: Setup Terraform
  uses: hashicorp/setup-terraform@v3
  with:
    terraform_version: "1.14.6"
    terraform_wrapper: false

- name: Write terraform.tfvars from secret
  working-directory: ${{ env.TF_DIR }}
  env:
    TF_PLUGIN_CACHE_DIR: ~/.terraform.d/plugin-cache
  run: printf "%s\n" "$TERRAFORM_VARS" > terraform.tfvars
```
