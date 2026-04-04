---
title : "Hướng dẫn chạy CI/CD"
date : 2024-01-01
weight : 5
chapter : true
pre : " <b> 4.5. </b> "
---

#### Tổng quan

<div align="justify">
Pipeline CI/CD của EduTrust được thiết kế theo mô hình chuẩn hoá để đảm bảo tính tái lập, truy vết thay đổi và an toàn khi triển khai trên môi trường staging/production. Thay vì thao tác thủ công từng bước, CI/CD tự động hoá toàn bộ chu trình từ kiểm tra chất lượng mã nguồn, đóng gói artifact, cập nhật hạ tầng cho đến rolling update dịch vụ backend; nhờ đó tăng tính nhất quán giữa các lần triển khai, kiểm soát thay đổi theo từng commit để dễ truy vết/rollback, giảm rủi ro cấu hình do thao tác tay, rút ngắn thời gian đưa thay đổi vào môi trường vận hành và có thể mở rộng thêm các bước kiểm thử hoặc bảo mật khi cần.
</div>

#### Cơ chế hoạt động (tổng quan)

<div align="justify">
Pipeline được kích hoạt khi có thay đổi được merge vào nhánh main hoặc khi được chạy thủ công (workflow_dispatch). Pipeline được chia thành 2 phần:

**CI (Continuous Integration):** phần kiểm tra, bao gồm định dạng, lint, test cơ bản để đảm bảo code đạt chuẩn trước khi build.

**CD (Continuous Delivery/Deployment):** phần quan trọng nhất, gồm 4 job chạy theo thứ tự phụ thuộc để đảm bảo hạ tầng và artifact luôn đồng bộ.
</div>

![Quy trình CI/CD](cicd-image.png)

- **Job Packer:** build image backend đã đóng gói sẵn ứng dụng và phụ thuộc.
- **Job Terraform:** cập nhật hạ tầng theo Terraform (tạo mới, thay đổi hoặc huỷ theo plan).
- **Job Build ECR:** build & push image Docker lên ECR để dùng cho ASG.
- **Job ASG Rolling Update:** triển khai phiên bản mới theo cơ chế rolling, đảm bảo không gián đoạn dịch vụ.

#### Nội dung

1. [Job CI](4.5.1-ci/)
2. [Job Packer](4.5.2-packer/)
3. [Job Terraform](4.5.3-terraform/)
4. [Job Build ECR](4.5.4-build-ecr/)
5. [Job ASG Rolling Update](4.5.5-asg-rolling-update/)
