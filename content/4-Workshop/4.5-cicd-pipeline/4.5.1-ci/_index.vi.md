---
title : "Job CI"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.5.1 </b> "
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

2. **Backend Test & Coverage**
   - Tải mã nguồn kèm lịch sử đầy đủ để phục vụ kiểm thử/coverage
   - Thiết lập **uv** và Python 3.11, cài dependencies bằng **uv sync --dev**
   - Nạp **.env** từ secret **BACKEND_ENV_FILE** (nếu có)
   - Thực thi **pytest** và xuất báo cáo **coverage.xml**

3. **Terraform Validate & Security Scan**
   - Thiết lập Terraform **1.14.6**
   - Kiểm tra định dạng với **terraform fmt -check -recursive**
   - Thực hiện **terraform init -backend=false** và **terraform validate**
   - Quét bảo mật Terraform bằng Checkov, dừng pipeline nếu phát hiện vi phạm

#### Vai trò

+ Bảo đảm chất lượng mã nguồn backend, tuân thủ chuẩn hạ tầng và an toàn cấu hình trước khi merge hoặc triển khai vào môi trường staging/production.
