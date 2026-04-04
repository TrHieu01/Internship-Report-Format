---
title : "Cảnh báo SNS qua Email"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.7.2 </b> "
---

#### Mục tiêu

Thiết lập cảnh báo gửi email khi CloudWatch Alarm vượt ngưỡng, giúp phản ứng sớm trước sự cố.

#### Thiết lập SNS Topic

1. Tạo SNS Topic cho hệ thống cảnh báo.
2. Đăng ký email nhận cảnh báo và xác nhận subscription.

#### Tạo CloudWatch Alarm

1. Chọn metric cần giám sát (ALB 5xx, CPU/Memory, instance unhealthy).
2. Thiết lập threshold và evaluation period phù hợp.
3. Gắn alarm vào SNS Topic để gửi email khi vượt ngưỡng.

#### Kiểm tra hoạt động

1. Tạo điều kiện giả lập vượt ngưỡng để kích hoạt alarm.
2. Xác nhận email cảnh báo được gửi thành công.
3. Kiểm tra nội dung cảnh báo có đủ thông tin truy vết.
