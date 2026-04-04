---
title : "Dọn dẹp"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 4.8. </b> "
---

#### Dọn dẹp bằng terraform destroy

1. Vào thư mục Terraform hoặc chạy qua CI/CD.
2. Chạy lệnh:
```
terraform destroy
```
3. Xác nhận thao tác khi được yêu cầu.

#### Tài nguyên cần xóa thủ công

1. **ACM certificates**: xóa chứng chỉ không còn dùng.
2. **CloudFront/Amplify**: xóa distribution hoặc app nếu còn tồn tại.
3. **Logs/Snapshots**: xóa log group và snapshot không cần thiết.

#### Kiểm tra trạng thái xóa thành công

1. Kiểm tra Terraform state không còn resource.
2. Vào AWS Console xác nhận không còn tài nguyên tính phí.
