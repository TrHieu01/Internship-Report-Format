---
title: "Workshop"
date: 2024-01-01
weight: 4
chapter: false
pre: " <b> 4. </b> "
---

{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

<div align="center">
<h1>
Hệ thống hỗ trợ học tập<br/>
và giám sát thi bằng AI Camera<br/>
Edutrust
</h1>
</div>

#### Tổng quan

EduTrust là hệ thống hỗ trợ học tập và giám sát thi bằng AI Camera, được triển khai trên kiến trúc AWS để đảm bảo khả năng mở rộng, bảo mật và vận hành ổn định. Workshop này hướng dẫn bối cảnh setup hệ thống và quy trình triển khai chuẩn cho nhóm.

Trong workshop, chúng ta sẽ thiết lập hạ tầng bằng Terraform trong CI/CD, cấu hình backend services và frontend trên AWS Amplify, đồng thời tích hợp chatbot hỗ trợ học tập và AI Camera giám sát thi.

Quy trình được chia thành các phần chính:

+ **Hạ tầng** - Tạo VPC, ALB, EC2 Auto Scaling, S3, ECR, IAM bằng Terraform và xác minh outputs.
+ **Ứng dụng** - Deploy frontend qua Amplify và backend services qua pipeline, cấu hình biến môi trường và secrets.
+ **Giám sát & bảo mật** - Bật WAF, cấu hình CloudWatch alarms, và thiết lập cảnh báo qua SNS.

#### Nội dung

1. [Tổng quan kiến trúc](4.1-architecture-overview/)
2. [Cài đặt môi trường](4.2-prerequisites/)
3. [Fork & Clone Repo](4.3-fork-clone-repo/)
4. [Cấu hình & Secrets](4.4-config-secrets/)
5. [Hướng dẫn chạy CI/CD](4.5-cicd-pipeline/)
6. [Frontend Deployment & Security](4.6-frontend-deployment-security/)
7. [Observability & Validation](4.7-observability-validation/)
8. [Dọn dẹp](4.8-cleanup/)
