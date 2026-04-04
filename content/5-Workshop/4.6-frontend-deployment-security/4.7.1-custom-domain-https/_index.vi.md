---
title : "Custom Domain & HTTPS"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.6.1 </b> "
---

#### Tổng quan

Trong phần này, bạn thiết lập Route 53 cho domain mua ở nhà cung cấp bên ngoài (ví dụ Name.com). Mục tiêu là quản lý DNS record trong Route 53 để dùng cho các bước tiếp theo (bao gồm custom domain & HTTPS trên Amplify ở mục 4.6.2).

#### Các bước

1. Tạo Hosted Zone trong Route 53 cho domain.

   ![Danh sách Hosted zones](create.png)

   *Trong Route 53 → **Hosted zones**, chọn **Create hosted zone**.*

   ![Tạo Hosted Zone](fill-info.png)

   *Nhập **Domain name**, giữ **Type = Public hosted zone**, sau đó bấm **Create hosted zone**.*

2. Lấy danh sách Nameservers (NS) từ Hosted Zone.

   ![Bản ghi NS trong Hosted Zone](ns.png)

   *Mở Hosted Zone vừa tạo và sao chép 4 giá trị trong bản ghi **NS**.*

3. Vào Name.com và cập nhật Nameserver trỏ về Route 53.

   ![Cập nhật Nameservers trên Name.com](domain.png)

   *Dán 4 Nameserver từ Route 53 vào mục **Manage Nameservers** trên Name.com và lưu thay đổi.*

4. Xác nhận DNS propagation hoàn tất.

   Bạn có thể kiểm tra bằng Route 53 **Test record** hoặc dùng terminal:

   ```bash
   nslookup -type=ns <ten-domain-cua-ban>
   ```
