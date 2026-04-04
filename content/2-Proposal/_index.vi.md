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

![EduTrust Platform Architecture](/images/2-Proposal/platform_architecture.jpeg)

*Dịch vụ & công nghệ sử dụng*  
- *Amazon S3*: Lưu trữ ảnh vi phạm, file tài liệu — hỗ trợ presigned URL để truy cập an toàn.  
- *AWS Amplify*: Triển khai và hosting frontend Next.js.  
- *MongoDB (Atlas)*: Cơ sở dữ liệu NoSQL cho users, exams, classes, submissions, violations.  
- *Redis*: Cache hội thoại AI (conversation context) với TTL, rate limiting.  
- *FastAPI*: Backend API framework — async, tự động tạo docs (Swagger/ReDoc).  
- *Next.js 16 + Tailwind CSS v4*: Frontend SPA với App Router, server/client components.  
- *YOLOv26n (Ultralytics)*: Mô hình object detection cho giám sát phòng thi.  
- *Pydantic AI + LiteLLM*: Orchestrator multi-agent cho chatbot hỗ trợ học tập.  
- *Logfire*: Observability và tracing cho FastAPI và Pydantic AI.  
- *Docker*: Containerize backend với multi-stage build (Ubuntu 24.04).  

*Thiết kế thành phần*  
- *Xác thực (Auth)*: JWT access/refresh token, session quản lý qua cookie, phân quyền RBAC (admin/teacher/student).  
- *Quản lý lớp học*: phân công giáo viên chủ nhiệm/bộ môn, thêm/xóa học sinh, tự động cập nhật trạng thái (active/inactive).  
- *Quản lý bài thi*: Tạo đề trắc nghiệm, mã bảo mật tự động, thời gian kiểm soát (start/end time), tự động chấm điểm khi nộp bài.  
- *Giám sát camera (Detection)*: CameraService nhận frame từ client, ObjectDetector (YOLO) phát hiện vi phạm, ViolationLogger ghi log MongoDB + S3, ScreenshotUtils chụp ảnh bằng chứng.  
- *AI Agent*: UnifiedAgent điều phối các sub-agent (technical, social, general, web_search) qua tool delegation, streaming response qua WebSocket.  

### 4. Triển khai kỹ thuật  
*Các giai đoạn triển khai*  
Dự án được chia thành 4 giai đoạn chính:  
1. *Nghiên cứu và thiết kế kiến trúc*: Nghiên cứu các công nghệ (FastAPI, Next.js, YOLO, Pydantic AI), thiết kế database schema, API contract và kiến trúc hệ thống (3 tuần).  
2. *Phát triển core features*: Xây dựng hệ thống auth (JWT của cognito), CRUD lớp học, quản lý bài thi, chấm điểm tự động (3 tuần).  
3. *Tích hợp AI & Camera*: Tích hợp YOLO cho phát hiện vi phạm, xây dựng hệ thống multi-agent chatbot, kết nối S3/Redis (3 tuần).  
4. *Frontend, kiểm thử & triển khai*: Hoàn thiện dashboard Next.js cho 3 vai trò, kiểm thử end-to-end, Docker hóa và triển khai lên AWS (3 tuần).  

*Yêu cầu kỹ thuật*  
- *Backend*: Python ≥ 3.11, FastAPI, Motor (async MongoDB driver), Redis ≥ 5.0, Boto3 (AWS SDK), Ultralytics (YOLO), Pydantic AI + LiteLLM, Kreuzberg (document parsing), SlowAPI (rate limiting).  
- *Frontend*: Next.js 16, React 19, Tailwind CSS v4, Lucide React (icons), React Markdown + KaTeX (render math), ONNX Runtime Web, next-intl (i18n).  
- *Hạ tầng*: Docker (multi-stage build), MongoDB Atlas, Redis Cloud, Amazon S3, AWS Amplify, Logfire (observability).  

### 5. Lộ trình & Mốc triển khai  
- *Tuần 1–2*: Nghiên cứu công nghệ, thiết kế kiến trúc và database schema.  
- *Tuần 3–5*: Phát triển backend core (auth, classes, exams, submissions).  
- *Tuần 6–8*: Tích hợp YOLO detection, AI chatbot (multi-agent), S3 storage.  
- *Tuần 9–10*: Phát triển frontend dashboard (admin/teacher/student views).  
- *Tuần 11*: Kiểm thử tích hợp, tối ưu hiệu năng, Docker hóa.  
- *Tuần 12*: Triển khai lên AWS (Amplify + EC2/ECS cho backend), viết tài liệu.  

### 6. Ước tính ngân sách  

*Chi phí hạ tầng (hàng tháng)*  
- MongoDB Atlas (Free Tier — M0): 0,00 USD/tháng (512 MB storage).  
- Redis Cloud (Free Tier): 0,00 USD/tháng (30 MB).  
- Amazon S3: ~0,50 USD/tháng (ước tính 5 GB ảnh vi phạm, PUT/GET requests).  
- AWS Amplify (Frontend hosting): ~0,35 USD/tháng.  
- EC2 hoặc ECS (Backend): ~3,00 USD/tháng (t3.micro hoặc Fargate spot).  
- Truyền dữ liệu (Data Transfer): ~0,10 USD/tháng.  

*Tổng*: ~3,95 USD/tháng, ~47,40 USD/12 tháng  

*Chi phí API bên thứ ba*  
- OpenAI/LiteLLM API: Tùy theo usage (có thể dùng free tier hoặc self-hosted model).  
- Tavily Search API: Free tier (1.000 requests/tháng).  

### 7. Đánh giá rủi ro  
*Ma trận rủi ro*  
- Độ chính xác YOLO thấp (false positive/negative): Ảnh hưởng cao, xác suất trung bình.  
- Mất kết nối camera/mạng của học sinh: Ảnh hưởng trung bình, xác suất trung bình.  
- Vượt ngân sách API (LLM calls): Ảnh hưởng trung bình, xác suất thấp.  
- MongoDB Atlas downtime: Ảnh hưởng cao, xác suất thấp.  

*Chiến lược giảm thiểu*  
- YOLO: Điều chỉnh ngưỡng confidence (min 0.5), chỉ alert sau nhiều frame liên tiếp, cho phép giáo viên review vi phạm thủ công.  
- Mạng: Client-side detection với ONNX Runtime Web (fallback), ghi log vi phạm locally và đồng bộ khi có mạng.  
- Chi phí API: Rate limiting (SlowAPI), đặt budget alerts, sử dụng model nhẹ hơn cho tác vụ đơn giản.  
- Database: Backup định kỳ, sử dụng MongoDB Atlas replica set.  

*Kế hoạch dự phòng*  
- Chuyển sang giám sát thủ công (giáo viên xem camera trực tiếp) nếu AI detection gặp sự cố.  
- Sử dụng SQLite/local storage làm fallback nếu MongoDB Atlas không khả dụng.  
- Docker image cho phép deploy nhanh trên bất kỳ cloud provider nào (không lock-in AWS).  

### 8. Kết quả kỳ vọng  
*Cải tiến kỹ thuật*: Tự động hóa quy trình giám sát thi bằng AI (YOLO) thay thế giám sát thủ công. Tự động chấm điểm trắc nghiệm, ghi nhận vi phạm kèm bằng chứng hình ảnh trên S3. Chatbot AI multi-agent hỗ trợ học sinh học tập 24/7.  
*Giá trị dài hạn*: Nền tảng có thể mở rộng cho nhiều trường học, hỗ trợ đa ngôn ngữ (next-intl), tích hợp thêm các loại đề thi (tự luận với AI chấm), và phát triển thành SaaS giáo dục hoàn chỉnh. Dữ liệu vi phạm tích lũy có thể dùng để cải thiện mô hình detection qua thời gian.