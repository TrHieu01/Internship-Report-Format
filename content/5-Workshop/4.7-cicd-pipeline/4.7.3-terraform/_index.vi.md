---
title : "Job Terraform"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 4.6.3 </b> "
---

#### Tổng quan

Phần này giới thiệu Job Terraform trong pipeline CI/CD của EduTrust, đây là bước build hạ tầng chính theo mô hình Infrastructure as Code (IaC). Hạ tầng được đặc tả dưới dạng cấu hình có thể kiểm soát phiên bản, truy vết thay đổi và tái lập triển khai một cách chuẩn hoá. Cách tiếp cận IaC giúp tăng tính tái lập (reproducibility), tăng khả năng kiểm toán (auditability), giảm sai lệch cấu hình giữa các môi trường và hỗ trợ tự động hoá phần lớn vòng đời triển khai. Job cũng đóng vai trò cung cấp outputs để liên kết dữ liệu đầu ra giữa các job, bảo đảm tính nhất quán và tính toàn vẹn của chuỗi triển khai.

#### Nội dung

1. [Giới thiệu Job Terraform & Outputs](4.6.3.1-gioi-thieu-job-terraform-outputs/)
2. [Chuẩn bị môi trường Terraform](4.6.3.2-chuan-bi-moi-truong-terraform/)
3. [Đọc cấu hình ECR & Xác thực AWS](4.6.3.3-doc-cau-hinh-ecr-xac-thuc-aws/)
4. [Khởi tạo Terraform State Backend (S3)](4.6.3.4-khoi-tao-terraform-state-backend/)
5. [Khởi tạo & Import Terraform State](4.6.3.5-khoi-tao-import-terraform-state/)
6. [Apply Infrastructure & Collect Outputs](4.6.3.6-apply-infra-collect-outputs/)
