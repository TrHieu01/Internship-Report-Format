---
title: "Tuần 7: Hạ tầng & Tự động hóa"
date: 2025-02-12
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 7:
* Thiết lập hạ tầng mạng VPC/EC2 cho hệ thống EduTrust.
* Triển khai hạ tầng dưới dạng mã (Infrastructure as Code - IaC).
* Cấu hình cân bằng tải (Load Balancer) và bảo mật SSL/HTTPS.

### Các công việc cần triển khai trong tuần này:
| Thứ | Ngày | Công việc |
| --- | --- | --- |
| 2 | 16/02 | Khởi tạo VPC, Subnet và EC2 cho Backend EduTrust. |
| 3 | 17/02 | Triển khai hạ tầng lên AWS bằng các kịch bản tự động (IaC). |
| 4 | 18/02 | Cấu hình Application Load Balancer để điều phối lưu lượng. |
| 5 | 19/02 | Tích hợp SSL (HTTPS) cho domain qua AWS Certificate Manager. |
| 6 | 20/02 | Thực hiện Load Testing kiểm tra khả năng chịu tải của hạ tầng. |
| 7 | 21/02 | Hoàn thiện tài liệu mô tả hạ tầng mạng (Security Groups). |
| CN | 22/02 | Đánh giá hiệu năng và bảo mật mạng cơ bản. |

### Kết quả đạt được tuần 7:
* Hạ tầng mạng AWS được thiết lập bài bản theo mô hình chuẩn của đồ án.
* Hệ thống đạt chuẩn bảo mật HTTPS, sẵn sàng cho người dùng truy cập.
* Tự động hóa triển khai giúp quản lý tài nguyên linh hoạt hơn.
