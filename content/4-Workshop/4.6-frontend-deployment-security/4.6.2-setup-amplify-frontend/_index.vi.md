---
title : "Triển khai Frontend bằng Amplify"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.6.2 </b> "
---

#### Mục tiêu

Triển khai frontend từ GitHub lên AWS Amplify để tự động build và deploy.

#### Tổng quan

AWS Amplify cung cấp cơ chế build, host và phát hành frontend theo nhánh, tích hợp pipeline build và hỗ trợ cấu hình domain/HTTPS.

#### Kết nối repo GitHub, chọn branch triển khai

1. Tạo ứng dụng Amplify mới.
2. Chọn GitHub và cấp quyền truy cập.
3. Chọn repo EduTrust và nhánh triển khai (main hoặc release).
4. Bật auto-deploy nếu cần đồng bộ bản phát hành theo commit.


#### Custom domain

Phần cấu hình custom domain và HTTPS được trình bày chi tiết ở mục 4.6.3 theo stack Name.com, Route 53 và ACM.

1. Vào Amplify, chọn Add domain và chọn domain ở Route 53.
2. Amplify tự tạo record CNAME/ALIAS.
3. Kiểm tra HTTPS hoạt động và redirect HTTP → HTTPS.

#### Cấu hình build (amplify.yml)

1. Mô tả vai trò file amplify.yml trong việc định nghĩa install, build, artifacts.
2. Đảm bảo đúng thư mục output để build thành công.
3. Bật cache nếu cần tối ưu thời gian build.


#### Biến môi trường FE

1. Thiết lập biến môi trường cho frontend như API base URL, Cognito IDs và region.
2. Đồng bộ biến theo môi trường staging và production.


#### Kiểm tra build thành công

1. Xác nhận build thành công trong Amplify Console.
2. Truy cập URL mặc định của Amplify và kiểm tra hiển thị giao diện.
