---
title : "Job Packer"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.5.2 </b> "
---

#### Job Packer gồm những task

**Trigger**

- Chạy thủ công qua workflow_dispatch (khi cần)
- Tự động chạy khi workflow trước đó kết thúc thành công (workflow_run = success)

**Các nhóm tác vụ chính**

1. **Chuẩn bị môi trường**
   - Checkout mã nguồn và thiết lập Packer
   - Cấu hình AWS credentials để tạo tài nguyên build tạm thời

2. **Khởi tạo và kiểm tra điều kiện build**
   - Packer init trong thư mục cấu hình
   - Tính hash template, kiểm tra AMI đã tồn tại để tránh build lại

3. **Tạo VPC tạm cho Packer**
   - Tạo VPC, Internet Gateway, Subnet và Route phục vụ build

4. **Dọn dẹp AMI cũ và build AMI mới**
   - Huỷ đăng ký AMI cũ trùng tên, xoá snapshot liên quan
   - Build AMI mới và gắn hash để truy vết cấu hình

5. **Cleanup sau build**
   - Xoá hạ tầng mạng tạm theo thứ tự ngược

**Luồng hoạt động**

- Job kích hoạt theo workflow_dispatch hoặc workflow_run (success).
- Thiết lập Packer và AWS credentials để có quyền tạo tài nguyên tạm.
- Packer init, tính hash cấu hình; nếu AMI tương ứng đã tồn tại và không ép build thì dừng.
- Tạo mạng tạm (VPC, IGW, Subnet, Route) để build AMI.
- Huỷ AMI cũ trùng tên, xoá snapshot, sau đó build AMI mới có tag hash.
- Dọn dẹp toàn bộ tài nguyên mạng tạm sau build.

#### Vai trò

+ Chuẩn hoá môi trường chạy backend và bảo đảm image triển khai nhất quán giữa các lần build.
