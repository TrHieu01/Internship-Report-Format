---
title : "Điều kiện chạy & Outputs"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.5.3.1 </b> "
---

#### Mục tiêu

Làm rõ điều kiện kích hoạt Job Terraform và nhóm outputs được publish để truyền dữ liệu cho các job downstream.

#### Nội dung chính

Job Terraform chỉ chạy khi thoả điều kiện needs và if, bảo đảm job Packer đã hoàn tất theo trạng thái hợp lệ và workflow được kích hoạt đúng ngữ cảnh. Sau khi hoàn thành, job publish các outputs như ASG name, ECR repository URL, ALB DNS và backend target group ARN để các bước triển khai sau sử dụng nhất quán.

**Trích đoạn cấu hình liên quan**

```yaml
needs: packer
if: always() && (needs.packer.result == 'success' || needs.packer.result == 'skipped') &&
    (github.event_name == 'workflow_dispatch' || github.event.workflow_run.conclusion == 'success')
outputs:
  asg_name: ${{ steps.tf_output.outputs.asg_name }}
  ecr_repository_url: ${{ steps.tf_output.outputs.ecr_repository_url }}
  alb_dns_name: ${{ steps.tf_output.outputs.alb_dns_name }}
  backend_target_group_arn: ${{ steps.tf_output.outputs.backend_target_group_arn }}
```

#### Lưu Ý

- Ràng buộc điều kiện chạy bằng `needs` và `if` để bảo đảm thứ tự thực thi đúng theo thiết kế pipeline.
- Outputs chỉ nên chứa dữ liệu phục vụ cho job kế tiếp, tránh đưa các giá trị thuộc nhóm bí mật cấu hình hoặc thông tin định danh nhạy cảm (ví dụ: access key, secret key, token, mật khẩu, private key, connection string, API key).
- Đặt tên outputs rõ nghĩa để dễ theo dõi và truy vết trong toàn bộ workflow.
