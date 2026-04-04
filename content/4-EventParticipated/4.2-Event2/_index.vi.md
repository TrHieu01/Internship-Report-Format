---
title: "Event 2"
date: 2024-01-01
weight: 1
chapter: false
pre: " <b> 4.2. </b> "
---

# Bài thu hoạch “Cloud Mastery Series #2: DevOps Fundamentals & Infrastructure”

### Mục tiêu sự kiện

- Hệ thống hóa kiến thức về IaC: Cung cấp cái nhìn toàn diện về Infrastructure as Code và cách triển khai thực tế với Terraform trên AWS.  
- Làm chủ điều phối Container: Giới thiệu kiến trúc Kubernetes (K8s) và cách quản lý ứng dụng hiện đại trên môi trường Cloud-native.  
- Tối ưu hóa vận hành với Elixir: Khám phá giải pháp Elixir/Erlang như một công cụ thống nhất cho hệ thống DevOps có độ sẵn sàng cao và khả năng chịu lỗi.  
- Thực hành thực tế (Hands-on): Trình diễn các kỹ thuật triển khai hạ tầng và ứng dụng thông qua Demo trực tiếp.  

### Diễn giả

- Thinh Nguyễn – FCAJ Cloud Engineer Trainee (Chuyên gia về IaC & Terraform).  
- Bảo Huỳnh – Junior Cloud Native Developer tại Endava / Founder ITea Lab (Chuyên gia Kubernetes).  
- Nguyễn Tạ Minh Triết – R&D Member tại ITea Lab / SAP Developer Intern tại Bosch GSV (Chuyên gia Elixir).  

### Điểm nổi bật

#### Infrastructure as Code (IaC) với Terraform

- Phân tích sự dịch chuyển từ "ClickOps" sang tự động hóa hạ tầng để tránh sai sót con người và tăng tính nhất quán.  
- So sánh AWS CloudFormation, AWS CDK và Terraform (HCL).  
- Quy trình quản lý State file và các lệnh thực thi cốt lõi (plan, apply, destroy).  

#### Kubernetes (K8s) Architecture

- Giải quyết thách thức quản lý hàng ngàn container: tự phục hồi (self-healing) và tự động mở rộng (auto-scaling).  
- Đi sâu vào các thành phần: Control Plane, Worker Nodes, Pods, Deployments và Services.  
- Giới thiệu công cụ hỗ trợ: Helm (quản lý package) và K9s (giao diện terminal trực quan).  

#### Elixir in DevOps Pipeline

- Sức mạnh của máy ảo BEAM trong việc xử lý hàng triệu kết nối đồng thời với chi phí cực thấp.  
- Triết lý "Let it crash": Sử dụng Supervision Trees để hệ thống tự phục hồi mà không cần can thiệp thủ công.  
- Case study: Chuyển đổi từ Serverless (Node.js/Lambda) sang Elixir giúp giảm chi phí từ $30,000/tháng xuống còn dưới $400/tháng.  

### Kết quả rút ra

- Tư duy tự động hóa: Hạ tầng không còn là các server đơn lẻ mà là các dòng code có thể phiên bản hóa (versioning) và tái sử dụng.  
- Quản lý Cluster hiệu quả: Hiểu rõ Amazon EKS là giải pháp tối ưu cho doanh nghiệp để giảm bớt gánh nặng quản lý Control Plane của Kubernetes.  
- Khả năng chịu lỗi (Fault-Tolerance): Việc thiết kế hệ thống có khả năng tự phục hồi (như trong Elixir) quan trọng hơn việc cố gắng viết code không bao giờ lỗi.  
- Tối ưu hóa chi phí (Cost Optimization): Lựa chọn đúng công nghệ (như Elixir cho các task tính toán song song) có thể mang lại hiệu quả ROI vượt trội so với các mô hình truyền thống.  

### Ứng dụng vào công việc

- Định hướng dự án EduTrust: Sử dụng Terraform để thiết lập hạ tầng AWS một cách chuẩn hóa, giúp dễ dàng sao chép môi trường (Dev/Staging/Prod).  
- Triển khai ứng dụng: Cân nhắc đóng gói các microservices của EduTrust vào Docker và điều phối bằng Kubernetes để đảm bảo tính sẵn sàng cao.  
- Cải thiện hiệu suất: Tìm hiểu sâu hơn về kiến trúc hướng sự kiện (Event-driven) thông qua cách Elixir xử lý tiến trình để áp dụng vào các tính năng cần xử lý thời gian thực.  

### Trải nghiệm sự kiện

Chuỗi workshop mang lại một hành trình từ hạ tầng đến ứng dụng rất logic:  

- Nội dung chuyên sâu: Không chỉ dừng lại ở lý thuyết, các phiên Demo về Terraform và K9s giúp hình dung rõ cách vận hành thực tế của một kỹ sư Cloud.  
- Góc nhìn đa chiều: Sự kết hợp giữa công nghệ phổ biến (AWS, K8s) và công nghệ đặc thù hiệu suất cao (Elixir) giúp mở rộng tư duy chọn lựa giải pháp.  
- Sự kết nối: Cơ hội trao đổi với các diễn giả có kinh nghiệm thực chiến từ các tập đoàn lớn như Endava và Bosch.  

### Bài học rút ra

- Hiện đại hóa hạ tầng bắt buộc phải đi kèm với IaC để đảm bảo tốc độ và an toàn.  
- Kubernetes là "hệ điều hành" của đám mây, nhưng cần các công cụ bổ trợ như Helm và K9s để quản trị hiệu quả.  
- Đừng ngại thử nghiệm các ngôn ngữ/nền tảng mới (như Elixir) nếu chúng giải quyết được bài toán về chi phí và độ tin cậy tốt hơn các giải pháp phổ thông.  

### Một số hình ảnh tham gia sự kiện

(Chưa có ảnh sự kiện)

### Tổng kết

Chuỗi sự kiện đã cung cấp một bộ khung kiến thức vững chắc về DevOps hiện đại. Đây là nền tảng quan trọng để tôi áp dụng vào việc xây dựng và vận hành dự án EduTrust một cách chuyên nghiệp, sẵn sàng cho các bài toán quy mô lớn trên Cloud.
