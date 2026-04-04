---
title : "Job Terraform"
date : 2024-01-01
weight : 3
chapter : true
pre : " <b> 4.5.3 </b> "
---

#### Tổng quan

Phần này giới thiệu Job Terraform trong pipeline CI/CD của EduTrust, đây là bước build hạ tầng chính theo mô hình Infrastructure as Code (IaC). Hạ tầng được đặc tả dưới dạng cấu hình có thể kiểm soát phiên bản, truy vết thay đổi và tái lập triển khai một cách chuẩn hoá. Cách tiếp cận IaC giúp tăng tính tái lập (reproducibility), tăng khả năng kiểm toán (auditability), giảm sai lệch cấu hình giữa các môi trường và hỗ trợ tự động hoá phần lớn vòng đời triển khai. Job cũng đóng vai trò cung cấp outputs để liên kết dữ liệu đầu ra giữa các job, bảo đảm tính nhất quán và tính toàn vẹn của chuỗi triển khai.

#### Nội dung

1. [Điều kiện chạy & Outputs](4.5.3.1-dieu-kien-chay-outputs/)
2. [Chuẩn bị môi trường Terraform](4.5.3.2-chuan-bi-moi-truong-terraform/)
3. [Đọc cấu hình ECR & Xác thực AWS](4.5.3.3-doc-cau-hinh-ecr-xac-thuc-aws/)
4. [S3 lưu trữ file Terraform State](4.5.3.4-s3-luu-tru-terraform-state/)
5. [Khởi tạo & Import Terraform State](4.5.3.5-khoi-tao-import-terraform-state/)
6. [Triển khai hạ tầng & Thu thập Outputs](4.5.3.6-trien-khai-ha-tang-thu-thap-outputs/)
7. [Các tài nguyên được tạo sau khi chạy Terraform](4.5.3.7-tai-nguyen-duoc-tao/)
