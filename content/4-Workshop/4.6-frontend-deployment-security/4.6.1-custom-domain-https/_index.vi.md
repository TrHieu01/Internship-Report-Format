---
title : "Custom Domain & HTTPS"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.6.1 </b> "
---

#### Tổng quan

Trong phần này, bạn cấu hình custom domain theo flow Name.com → Route 53 → ACM → Amplify để bật HTTPS và đảm bảo truy cập an toàn.

Trình tự thực hiện:

1. Thiết lập Route 53 và cập nhật nameserver tại Name.com.
2. Cấp chứng chỉ ACM bằng DNS validation.
3. Gắn domain vào Amplify và kiểm tra HTTPS.

#### Nội dung

1. [Thiết lập Route53 cho domain Name.com](4.6.1.1-acm-route53-cicd/)
2. [Cấp chứng chỉ ACM cho domain](4.6.1.2-nameserver-domain-provider/)