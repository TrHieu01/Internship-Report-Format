---
title : "WAF Frontend"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 4.6.4 </b> "
---

#### Mục tiêu

Bảo vệ layer frontend (CloudFront) bằng WAF.

#### Các bước triển khai

1. Tạo Web ACL trên AWS WAF.
2. Chọn scope CloudFront và thêm managed rule groups cơ bản.
3. Gắn Web ACL vào CloudFront distribution của Amplify.

#### Kiểm tra rule hoạt động

1. Thử áp dụng rate limit hoặc IP block để xác nhận rule có hiệu lực.
2. Theo dõi log/metrics trong CloudWatch để đánh giá false positive.

1. Vào AWS WAF, tạo Web ACL.
2. Chọn scope CloudFront và thêm managed rule groups.
3. Mở CloudFront Distribution của Amplify.
4. Chọn Web ACL vừa tạo trong phần WAF.
5. Lưu cấu hình và chờ cập nhật hoàn tất.

#### Lưu ý

1. Ưu tiên bật chế độ monitor trước khi chuyển sang block.
