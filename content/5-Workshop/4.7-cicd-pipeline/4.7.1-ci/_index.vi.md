---
title : "Job CI"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.6.1 </b> "
---

#### Job CI gồm những task

**Trigger**

- **Pull_request** khi thay đổi trong phạm vi: mã nguồn backend, quy tắc kiểm tra, workflow CI/CD, đóng gói container, hạ tầng IaC
- **Merge PR vào main** (tạo sự kiện push) với cùng phạm vi thay đổi như trên
- **workflow_dispatch** trong GitHub Actions (nếu cần)

**Các nhóm tác vụ chính**

1. **Pre-commit Checks**
   - Tải mã nguồn, thiết lập Python 3.11
   - Tận dụng cache **pre-commit** để tối ưu thời gian
   - Thực thi **pre-commit** theo cấu hình chuẩn hoá tại **.pre-commit-config.yaml**

   **Cấu hình tham chiếu**

   ```yaml
   pre-commit:
     name: Pre-commit Checks
     runs-on: ubuntu-latest
     steps:
       # Lấy mã nguồn để chạy các bước kiểm tra
       - name: Checkout code
         uses: actions/checkout@v4
       # Thiết lập Python cho pre-commit hooks
       - name: Setup Python
         uses: actions/setup-python@v5
         with:
           python-version: "3.11"
       # Cache để tăng tốc các lần chạy sau
       - name: Cache pre-commit
         uses: actions/cache@v4
         with:
           path: ~/.cache/pre-commit
           key: ${{ runner.os }}-pre-commit-${{ hashFiles('.pre-commit-config.yaml') }}
           restore-keys: |
             ${{ runner.os }}-pre-commit-
       # Thực thi các hook đã cấu hình
       - name: Run pre-commit
         uses: pre-commit/action@v3.0.1
   ```

2. **Backend Test & Coverage**
   - Tải mã nguồn kèm lịch sử đầy đủ để phục vụ kiểm thử/coverage
   - Thiết lập **uv** và Python 3.11, cài dependencies bằng **uv sync --dev**
   - Nạp **.env** từ secret **BACKEND_ENV_FILE** (nếu có)
   - Thực thi **pytest** và xuất báo cáo **coverage.xml**

   **Cấu hình tham chiếu**

   ```yaml
   test:
     name: Backend Test & Coverage
     runs-on: ubuntu-latest
     defaults:
       run:
         working-directory: backend
     steps:
       # Lấy mã nguồn (có đủ lịch sử để phục vụ coverage)
       - name: Checkout code
         uses: actions/checkout@v4
         with:
           fetch-depth: 0
       # Cài đặt uv và bật cache dependency
       - name: Setup uv
         uses: astral-sh/setup-uv@v4
         with:
           enable-cache: true
           cache-dependency-glob: "backend/uv.lock"
       # Thiết lập Python đúng phiên bản dự án
       - name: Setup Python
         uses: actions/setup-python@v5
         with:
           python-version: "3.11"
       # Cài dependencies cho môi trường dev/test
       - name: Install dependencies
         run: uv sync --dev
       # Nạp biến môi trường từ GitHub Secrets (nếu có)
       - name: Load backend .env 
         env:
           BACKEND_ENV_FILE: ${{ secrets.BACKEND_ENV_FILE }}
         run: |
           if [ -n "${BACKEND_ENV_FILE}" ]; then
             printf '%s' "${BACKEND_ENV_FILE}" > .env
           fi
       # Chạy test và xuất báo cáo coverage
       - name: Run tests with coverage
         run: PYTHONPATH=. uv run pytest tests -v --maxfail=1 --disable-warnings --cov=src --cov-report=term-missing --cov-report=xml:coverage.xml
   ```

3. **Terraform Validate & Security Scan**
   - Thiết lập Terraform **1.14.6**
   - Kiểm tra định dạng với **terraform fmt -check -recursive**
   - Thực hiện **terraform init -backend=false** và **terraform validate**
   - Quét bảo mật Terraform bằng Checkov, dừng pipeline nếu phát hiện vi phạm

   **Cấu hình tham chiếu**

   ```yaml
   terraform-check:
     name: Terraform Validate & Security Scan
     runs-on: ubuntu-latest
     steps:
       # Lấy mã nguồn IaC để kiểm tra
       - name: Checkout code
         uses: actions/checkout@v4
       # Cài đặt Terraform đúng phiên bản chuẩn
       - name: Setup Terraform
         uses: hashicorp/setup-terraform@v3
         with:
           terraform_version: "1.14.6"
           terraform_wrapper: false
       # Kiểm tra định dạng Terraform
       - name: Terraform Format Check
         working-directory: .github/terraform
         run: terraform fmt -check -recursive
       # Validate cú pháp và cấu trúc Terraform
       - name: Terraform Validate
         working-directory: .github/terraform
         run: |
           terraform init -backend=false
           terraform validate
       # Quét bảo mật IaC bằng Checkov
       - name: Run Checkov (security scan)
         uses: bridgecrewio/checkov-action@v12
         with:
           directory: .github/terraform
           framework: terraform
           soft_fail: false
           skip_check: CKV_AWS_8,CKV_AWS_126,CKV_AWS_24,CKV_AWS_130,CKV_AWS_260,CKV_AWS_2,CKV2_AWS_20,CKV_AWS_103,CKV_AWS_378,CKV_AWS_382,CKV_AWS_91,CKV_AWS_150,CKV2_AWS_11,CKV2_AWS_12,CKV2_AWS_28
   ```

#### Vai trò

+ Bảo đảm chất lượng mã nguồn backend, tuân thủ chuẩn hạ tầng và an toàn cấu hình trước khi merge hoặc triển khai vào môi trường staging/production.
