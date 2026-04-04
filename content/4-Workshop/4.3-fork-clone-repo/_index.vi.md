---
title : "Fork & Clone Repo"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 4.3. </b> "
---

Repo: https://github.com/AWS-FCJ-Project/EduTrust_origin.git

#### Các lệnh git cơ bản

1. **Fork repository** trên GitHub (nếu bạn không có quyền push trực tiếp):
   + Mở repo: https://github.com/AWS-FCJ-Project/EduTrust_origin
   + Nhấn nút **Fork** (góc phải trên).
   + Chọn tài khoản GitHub của bạn để tạo bản sao.
2. **Clone về máy local**:
```
git clone https://github.com/AWS-FCJ-Project/EduTrust_origin.git
```
3. **Vào thư mục dự án**:
```
cd EduTrust_origin
```
4. **Tạo nhánh làm việc**:
```
git checkout -b feature/<ten-nhanh>
```
Ví dụ:
```
git checkout -b feature/setup-workshop
```
5. **Đẩy nhánh lên GitHub lần đầu**:
```
git push -u origin feature/<ten-nhanh>
```
6. **Cập nhật code mới nhất từ main** (trước khi làm việc hoặc trước khi tạo PR):
```
git fetch origin
git rebase origin/main
```
