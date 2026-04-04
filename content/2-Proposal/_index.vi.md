---
title: "Bản đề xuất"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
<!-- {{% notice warning %}}
⚠️ **Lưu ý:** Các thông tin dưới đây chỉ nhằm mục đích tham khảo, vui lòng **không sao chép nguyên văn** cho bài báo cáo của bạn kể cả warning này.
{{% /notice %}}

Tại phần này, bạn cần tóm tắt các nội dung trong workshop mà bạn **dự tính** sẽ làm. -->

# EduTrust — Nền tảng giám sát thi trực tuyến tích hợp AI  
## Giải pháp Fullstack kết hợp AWS cho giám sát phòng thi và hỗ trợ học tập thông minh  

### 1. Tóm tắt điều hành  
EduTrust là một nền tảng quản lý thi trực tuyến được thiết kế cho môi trường giáo dục (trường học, trung tâm đào tạo), nhằm số hóa quy trình tổ chức thi, giám sát phòng thi bằng AI và hỗ trợ học tập thông qua chatbot thông minh. Hệ thống phục vụ 3 nhóm người dùng chính: **Admin** (nhà trường), **Giáo viên** (tạo đề thi, giám sát) và **Học sinh** (làm bài thi, xem kết quả). Backend sử dụng FastAPI (Python) kết hợp MongoDB, Redis, Amazon S3 và mô hình YOLO để phát hiện gian lận qua camera. Frontend xây dựng bằng Next.js với Tailwind CSS, triển khai trên AWS Amplify.  

### 2. Tuyên bố vấn đề  
*Vấn đề hiện tại*  
Việc tổ chức thi trực tuyến tại các trường học gặp nhiều thách thức: giám sát thủ công tốn nhân lực, khó phát hiện gian lận (sử dụng điện thoại, nhiều người trong khung hình, rời khỏi camera), không có hệ thống tập trung để quản lý lớp học — đề thi — kết quả, và thiếu công cụ hỗ trợ học tập thông minh cho học sinh.  

*Giải pháp*  
EduTrust cung cấp một nền tảng toàn diện bao gồm:  
- **Quản lý lớp học & đề thi**: Admin tạo lớp, phân công giáo viên chủ nhiệm và giáo viên bộ môn; giáo viên tạo đề thi trắc nghiệm có mã bảo mật (secret key), thiết lập thời gian bắt đầu/kết thúc.  
- **Giám sát phòng thi bằng AI**: Tích hợp YOLOv26n (object detection) để phát hiện vi phạm qua webcam thời gian thực — bao gồm phát hiện nhiều khuôn mặt (MULTIPLE_FACES), rời khỏi camera (FACE_DISAPPEARED: cell Phone), và vật cấm (FORBIDDEN_OBJECT). Ảnh vi phạm được tải lên Amazon S3 và ghi log vào MongoDB.  
- **Chatbot AI hỗ trợ học tập**: Hệ thống multi-agent sử dụng Pydantic AI với các agent chuyên biệt (technical, social, general, web search) giúp học sinh tra cứu kiến thức, hỏi đáp và tìm kiếm tài liệu.  
- **Xác thực & bảo mật**: JWT token (sử dụng Cognito) phân quyền theo vai trò (RBAC).  

*Lợi ích và hoàn vốn đầu tư (ROI)*  
Giải pháp giúp giảm tải công việc giám sát thủ công cho giáo viên, nâng cao tính minh bạch và công bằng trong thi cử. Hệ thống tự động chấm điểm, ghi nhận vi phạm với bằng chứng hình ảnh, và cung cấp dashboard tổng hợp kết quả. Chi phí vận hành thấp nhờ tận dụng MongoDB Atlas (free tier), Redis Cloud, và AWS S3/Amplify. Ước tính chi phí hạ tầng AWS dưới 5 USD/tháng cho quy mô trường học vừa.  

### 3. Kiến trúc giải pháp  
Nền tảng áp dụng kiến trúc **Fullstack monorepo** với backend Python (FastAPI) và frontend Next.js, triển khai qua Docker container. Dữ liệu được lưu trữ trên MongoDB (collections: users, exams, classes, submissions, violations), cache session hội thoại trên Redis, và hình ảnh vi phạm trên Amazon S3.  

![Kiến trúc giải pháp EduTrust](/images/2-Proposal/edutrust-architect.png)

*Dịch vụ & công nghệ sử dụng (theo kiến trúc)*  
- *AWS Amplify + CloudFront*: Hosting frontend Next.js và phân phối nội dung qua CDN.  
- *AWS Route 53 + AWS ACM*: DNS và quản lý chứng chỉ TLS/HTTPS.  
- *AWS WAF*: Bảo vệ lớp web trước các pattern tấn công phổ biến.  
- *Amazon VPC (public/private subnet)*: Cô lập mạng, phân tách tầng public/private.  
- *Application Load Balancer (ALB)*: Điều phối request vào backend.  
- *Amazon EC2 Auto Scaling*: Vận hành backend theo tải với khả năng mở rộng tự động.  
- *Amazon ECR*: Lưu trữ Docker image cho backend.  
- *Amazon S3*: Lưu trữ ảnh vi phạm, log ALB và Terraform state.  
- *Amazon DynamoDB*: Lưu trữ dữ liệu nhanh theo key-value (theo ảnh kiến trúc).  
- *Amazon ElastiCache for Redis*: Cache session/hội thoại và dữ liệu truy cập nhanh.  
- *Amazon Cognito*: Xác thực người dùng, phân quyền theo vai trò.  
- *Amazon CloudWatch + VPC Flow Logs + SNS*: Giám sát, log và cảnh báo.  
- *AWS KMS + SSM Parameter Store + PrivateLink*: Bảo mật secret và truy cập nội bộ.  
- *Terraform + GitHub Actions*: IaC và CI/CD tự động hoá triển khai.  

*Công nghệ ứng dụng*  
- *FastAPI*: Backend API framework — async, tự động tạo docs (Swagger/ReDoc).  
- *Next.js 16 + Tailwind CSS v4*: Frontend SPA với App Router, server/client components.  
- *YOLOv26n (Ultralytics)*: Mô hình object detection cho giám sát phòng thi.  
- *Pydantic AI + LiteLLM*: Orchestrator multi-agent cho chatbot hỗ trợ học tập.  
- *Docker*: Containerize backend với multi-stage build (Ubuntu 24.04).  

*Thiết kế thành phần*  
- *Xác thực (Auth)*: JWT access/refresh token, session quản lý qua cookie, phân quyền RBAC (admin/teacher/student).  
- *Quản lý lớp học*: phân công giáo viên chủ nhiệm/bộ môn, thêm/xóa học sinh, tự động cập nhật trạng thái (active/inactive).  
- *Quản lý bài thi*: Tạo đề trắc nghiệm, mã bảo mật tự động, thời gian kiểm soát (start/end time), tự động chấm điểm khi nộp bài.  
- *Giám sát camera (Detection)*: CameraService nhận frame từ client, ObjectDetector (YOLO) phát hiện vi phạm, ViolationLogger ghi log MongoDB + S3, ScreenshotUtils chụp ảnh bằng chứng.  
- *AI Agent*: UnifiedAgent điều phối các sub-agent (technical, social, general, web_search) qua tool delegation, streaming response qua WebSocket.  

### 4. Triển khai kỹ thuật  
*Các giai đoạn triển khai*  
Dự án được chia thành 5 giai đoạn chính:  
1. *Tìm hiểu dịch vụ AWS nền tảng*: Làm quen các dịch vụ trong kiến trúc (VPC, EC2/ALB/ASG, S3, ECR, Cognito, CloudWatch, KMS, SSM, WAF) và quy trình CI/CD/IaC.  
2. *Nghiên cứu và thiết kế kiến trúc*: Nghiên cứu các công nghệ (FastAPI, Next.js, YOLO, Pydantic AI), thiết kế database schema, API contract và kiến trúc hệ thống.  
3. *Phát triển core features*: Xây dựng hệ thống auth (JWT của cognito), CRUD lớp học, quản lý bài thi, chấm điểm tự động.  
4. *Tích hợp AI & Camera*: Tích hợp YOLO cho phát hiện vi phạm, xây dựng hệ thống multi-agent chatbot, kết nối S3/Redis.  
5. *Frontend & kiểm thử*: Hoàn thiện dashboard Next.js cho 3 vai trò, kiểm thử end-to-end và Docker hóa.  

*Yêu cầu kỹ thuật*  
- *Backend*: Python ≥ 3.11, FastAPI, Motor (async MongoDB driver), Redis ≥ 5.0, Boto3 (AWS SDK), Ultralytics (YOLO), Pydantic AI + LiteLLM, Kreuzberg (document parsing), SlowAPI (rate limiting).  
- *Frontend*: Next.js 16, React 19, Tailwind CSS v4, Lucide React (icons), React Markdown + KaTeX (render math), ONNX Runtime Web, next-intl (i18n).  
- *Hạ tầng*: Docker (multi-stage build), MongoDB Atlas, Redis Cloud, Amazon S3, AWS Amplify, Logfire (observability).  

### 5. Lộ trình & Mốc triển khai  
- *Tuần 1–2*: Tìm hiểu các dịch vụ AWS theo kiến trúc (VPC, EC2/ALB/ASG, S3, ECR, Cognito, CloudWatch, KMS/SSM, WAF) và quy trình CI/CD/IaC.  
- *Tuần 3–4*: Nghiên cứu công nghệ, thiết kế kiến trúc và database schema.  
- *Tuần 5–6*: Phát triển backend core (auth, classes, exams, submissions).  
- *Tuần 7–8*: Tích hợp YOLO detection, AI chatbot (multi-agent), S3 storage.  
- *Tuần 9*: Phát triển frontend dashboard (admin/teacher/student views).  
- *Tuần 10*: Kiểm thử tích hợp, tối ưu hiệu năng và Docker hóa.  

### 6. Ước tính ngân sách  

*Giả định theo kiến trúc*  
- Môi trường nhỏ (staging/production nhỏ), lưu lượng thấp–trung bình.  
- Backend chạy EC2 Auto Scaling (t3.small, 2 instance), ALB hoạt động 24/7.  
- Frontend host trên Amplify + CloudFront, dùng WAF.  
- Dữ liệu vi phạm lưu trên S3 (~10–20 GB/tháng).  

*Chi phí hạ tầng (hàng tháng – ước tính)*  
- VPC Endpoints (Interface cho ECR/SSM/STS/Logs…): ~30–60 USD  
- EC2 Auto Scaling (2 x t3.small): ~30–40 USD  
- Application Load Balancer: ~16–25 USD  
- Amazon S3 (ảnh vi phạm, log ALB, terraform state): ~2–6 USD  
- Amazon CloudFront + Amplify: ~1–5 USD  
- AWS WAF: ~5–10 USD  
- Amazon ElastiCache (Redis – cache nhỏ): ~15–25 USD  
- Amazon DynamoDB (low traffic): ~1–3 USD  
- Amazon ECR (storage image): ~1–3 USD  
- Amazon Cognito (<= 50k MAU): ~0–2 USD  
- Amazon CloudWatch + VPC Flow Logs + SNS: ~5–10 USD  
- AWS KMS + SSM Parameter Store: ~1–3 USD  
- Data Transfer: ~2–6 USD  

*Tổng dự kiến*: ~110–195 USD/tháng (đã tính VPC Endpoints; phụ thuộc lưu lượng và dung lượng S3)  

*Chi phí API bên thứ ba*  
- OpenAI/LiteLLM API: tuỳ usage.  
- Các dịch vụ tìm kiếm ngoài (nếu dùng): tuỳ gói.  

### 7. Đánh giá rủi ro  
*Ma trận rủi ro*  
- Độ chính xác YOLO thấp (false positive/negative): Ảnh hưởng cao, xác suất trung bình.  
- Mất kết nối camera/mạng của học sinh: Ảnh hưởng trung bình, xác suất trung bình.  
- Vượt ngân sách API (LLM calls): Ảnh hưởng trung bình, xác suất thấp.  
- Chuyển từ MongoDB sang MySQL gây thay đổi schema & query phức tạp: Ảnh hưởng trung bình–cao, xác suất trung bình.  

*Chiến lược giảm thiểu*  
- YOLO: Điều chỉnh ngưỡng confidence (min 0.5), chỉ alert sau nhiều frame liên tiếp, cho phép giáo viên review vi phạm thủ công.  
- Mạng: Client-side detection với ONNX Runtime Web (fallback), ghi log vi phạm locally và đồng bộ khi có mạng.  
- Chi phí API: Rate limiting (SlowAPI), đặt budget alerts, sử dụng model nhẹ hơn cho tác vụ đơn giản.  
- Database: Thiết kế lớp repository để trừu tượng hoá DB, chuẩn hoá schema, chuẩn bị script migrate dữ liệu nếu chuyển MySQL.  

*Kế hoạch dự phòng*  
- Chuyển sang giám sát thủ công (giáo viên xem camera trực tiếp) nếu AI detection gặp sự cố.  
- Sử dụng SQLite/local storage làm fallback nếu MongoDB Atlas không khả dụng.  
- Docker image cho phép deploy nhanh trên bất kỳ cloud provider nào (không lock-in AWS).  

### 8. Kết quả kỳ vọng  
*Cải tiến kỹ thuật*: Tự động hóa quy trình giám sát thi bằng AI (YOLO) thay thế giám sát thủ công. Tự động chấm điểm trắc nghiệm, ghi nhận vi phạm kèm bằng chứng hình ảnh trên S3. Chatbot AI multi-agent hỗ trợ học sinh học tập 24/7.  
*Giá trị dài hạn*: Nền tảng có thể mở rộng cho nhiều trường học, hỗ trợ đa ngôn ngữ (next-intl), tích hợp thêm các loại đề thi (tự luận với AI chấm), và phát triển thành SaaS giáo dục hoàn chỉnh. Dữ liệu vi phạm tích lũy có thể dùng để cải thiện mô hình detection qua thời gian.
