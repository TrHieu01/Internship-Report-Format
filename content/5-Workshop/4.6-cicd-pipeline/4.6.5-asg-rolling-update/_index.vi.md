---
title : "Job ASG Rolling Update"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 4.6.5 </b> "
---

#### Tổng quan

<div align="justify">
Job **Deploy to ASG** chịu trách nhiệm cập nhật phiên bản ứng dụng mới lên hạ tầng thực tế mà không gây gián đoạn dịch vụ. Quy trình này kết hợp giữa việc quản lý cấu hình (SSM), cập nhật bản thiết kế hạ tầng (Terraform Launch Template) và thực hiện thay thế dần các instance (ASG Instance Refresh).
</div>

#### Các giai đoạn triển khai

1. **Cập nhật Cấu hình (SSM Parameter Store)**
   Hệ thống nạp các biến môi trường nhạy cảm vào `SSM Parameter Store` dưới dạng `SecureString`. Việc này giúp tách biệt hoàn toàn giữa cấu hình và mã nguồn, đồng thời cho phép các instance tự động tải cấu hình khi khởi khởi động.

2. **Cập nhật Launch Template (Terraform)**
   Thay vì can thiệp thủ công, pipeline gọi Terraform để cập nhật `Launch Template` với thẻ image (ECR Tag) mới nhất. Đây là "bản vẽ" mà Auto Scaling Group sẽ sử dụng để tạo ra các instance mới.

3. **Instance Refresh & Monitoring**
   Sử dụng tính năng `start-instance-refresh` của AWS để thay thế các instance cũ bằng instance mới. Pipeline tích hợp một vòng lặp Bash script thông minh để giám sát trạng thái `% complete` và tự động dừng/thất bại nếu quá trình refresh gặp sự cố.

4. **Xác thực Triển khai (Rollout Verification)**
   Sau khi refresh hoàn tất, pipeline thực hiện các bước kiểm tra cuối cùng:
   - Kiểm tra mã phản hồi từ endpoint `/health`.
   - Xác nhận số lượng Instance Healthy trong Target Group đạt mức kỳ vọng.

#### Vai trò Kỹ thuật
+ **Zero Downtime**: Đảm bảo dịch vụ luôn sẵn sàng trong quá trình cập nhật.
+ **Safety Net**: Tự động phát hiện lỗi triển khai và dừng quá trình cập nhật để bảo vệ hệ thống.
+ **Traceability**: Mọi thay đổi về phiên bản đều được ghi lại qua Terraform state và ECR tags.
