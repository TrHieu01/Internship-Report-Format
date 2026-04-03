---
title: "Tuần 10: Giám sát & Tối ưu"
date: 2025-03-05
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---
{{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

### Mục tiêu tuần 10:
* Thiết lập hệ thống giám sát hiệu suất và log thời gian thực qua CloudWatch.
* Tối ưu bảo mật hạ tầng và quy trình sao lưu dữ liệu tự động.
* Kiểm tra khả năng chịu tải (Stress Test) của hệ thống EduTrust.

### Các công việc cần triển khai trong tuần này:
| Thứ | Ngày | Công việc |
| --- | --- | --- |
| 2 | 09/03 | Cấu hình AWS CloudWatch giám sát log từ FastAPI và Next.js. |
| 3 | 10/03 | Debug và tối ưu hóa thời gian phản hồi của các AI Agent. |
| 4 | 11/03 | Thiết lập quy trình sao lưu (Backup) tự động cho MongoDB Atlas. |
| 5 | 12/03 | Kiểm tra bảo mật S3 Bucket, đảm bảo chỉ truy cập qua Presigned URL. |
| 6 | 13/03 | Thực hiện Stress Test giả lập nhiều học sinh cùng thi một lúc. |
| 7 | 14/03 | Hoàn thiện tài liệu hướng dẫn vận hành và quản trị hệ thống. |
| CN | 15/03 | Kiểm tra tính ổn định của Docker containers trên môi trường AWS. |

### Kết quả đạt được tuần 10:
* Hệ thống được giám sát chặt chẽ, sẵn sàng ứng phó với các sự cố kỹ thuật.
* Quy trình sao lưu dữ liệu tự động đảm bảo an toàn cho bài thi của sinh viên.
* Nắm rõ giới hạn chịu tải của hệ thống để có phương án mở rộng (Scaling).
