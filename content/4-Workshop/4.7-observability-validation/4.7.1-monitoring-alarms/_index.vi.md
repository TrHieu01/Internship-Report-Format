---
title : "Giám sát CloudWatch Logs"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.7.1 </b> "
---

#### Tổng quan

CloudWatch được sử dụng để thu thập và giám sát log hệ thống, hỗ trợ phát hiện lỗi và theo dõi xu hướng hoạt động theo thời gian.

#### Log cần giám sát

1. **Application logs**: request, error, API latency.
2. **ALB logs**: 4xx/5xx và latency.
3. **System metrics**: CPU, memory, disk (CloudWatch Agent).

#### Vì sao cần giám sát

1. **Application logs**: phát hiện lỗi nghiệp vụ, lỗi API và bottleneck.
2. **ALB logs**: theo dõi chất lượng truy cập và tỉ lệ lỗi từ phía người dùng.
3. **System metrics**: cảnh báo sớm khi tài nguyên quá tải gây downtime.

#### Ghi chú

Thiết lập alarm và SNS sẽ được trình bày chi tiết ở mục 4.7.2.
