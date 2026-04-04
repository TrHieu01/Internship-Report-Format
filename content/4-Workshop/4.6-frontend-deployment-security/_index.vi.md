---
title : "Triển khai Frontend & Bảo mật"
date : 2024-01-01 
weight : 6
chapter : true
pre : " <b> 4.6. </b> "
---

#### Tổng quan

<p style="text-align: justify;">
Phần này tập trung vào triển khai frontend trên AWS Amplify, cấu hình xác thực người dùng bằng Cognito và bật WAF để bảo vệ lớp edge. Khi gắn custom domain vào Amplify, hệ thống tự tạo bản ghi DNS; phía domain provider chỉ cần cập nhật nameserver để Route 53 quản lý DNS và ACM xác thực TLS. Cách thiết lập này giảm thao tác thủ công, hạn chế sai sót và đảm bảo HTTPS vận hành ổn định.
</p>

#### Nội dung

1. [Triển khai Frontend bằng Amplify](4.7.1-setup-amplify-frontend/)
2. [Cognito (Xác thực người dùng)](4.7.2-cognito/)
3. [Custom Domain & HTTPS](4.7.3-custom-domain-https/)
4. [WAF Frontend](4.7.4-waf-frontend/)



