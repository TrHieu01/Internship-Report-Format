---
title : "Biến môi trường Backend"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 4.4.2 </b> "
---

Dự án Workspace AI Agent sử dụng tệp .env để cấu hình các dịch vụ như LLM (thông qua LiteLLM), Cơ sở dữ liệu (MongoDB), Xác thực (AWS Cognito), Bộ nhớ đệm (Redis) và các dịch vụ khác.

#### 1. Cấu hình AI Model (LiteLLM)

Dự án sử dụng **LiteLLM** làm lớp trung gian để quản lý các nhà cung cấp AI khác nhau (OpenAI, AWS Bedrock, Google Gemini, v.v.).

+ **LITELLM_API_KEY**: API Key dùng để truy cập vào proxy LiteLLM (nếu dùng self-hosted). Hoặc dùng **OPENAI_API_KEY** nếu gọi trực tiếp OpenAI.
+ **ORCHESTRATOR_MODEL**: Tên model dùng cho agent điều phối (ví dụ: gpt-4o-mini).
+ **AGENT_MODEL**: Tên model dùng cho các worker agent (ví dụ: gpt-4o-mini).
+ **TRANSLATE_MODEL**: Tên model dùng cho chức năng dịch thuật (ví dụ: gpt-4o-mini).
+ **TAVILY_API_KEY**: API Key cho dịch vụ tìm kiếm thông tin trên web (Tavily Search).

#### 2. Cơ sở dữ liệu (MongoDB)

Dự án sử dụng MongoDB để lưu trữ dữ liệu người dùng, cuộc hội thoại và trạng thái của agent.

+ **MONGO_URI**: Đường dẫn kết nối đến MongoDB (ví dụ: mongodb://localhost:27017 hoặc link từ MongoDB Atlas).
+ **MONGO_DB_NAME**: Tên cơ sở dữ liệu (ví dụ: workshop_db).

#### 3. Xác thực (AWS Cognito & JWT)

Sử dụng AWS Cognito để quản lý người dùng và JWT để bảo mật các API.

+ **COGNITO_USER_POOL_ID**: ID của User Pool trên AWS.
+ **COGNITO_APP_CLIENT_ID**: ID của App Client tương ứng.
+ **COGNITO_REGION**: Region nơi khởi tạo Cognito (ví dụ: ap-southeast-1).
+ **SECRET_KEY**: Chuỗi bí mật dùng để ký và xác thực JWT token.

#### 4. Lưu trữ (AWS S3)

Sử dụng S3 để lưu trữ các tài liệu (PDF, Docs) phục vụ cho RAG (Retrieval-Augmented Generation).

+ **S3_BUCKET_NAME**: Tên của S3 Bucket.
+ **AWS_REGION**: Vùng chứa bucket (ví dụ: ap-southeast-1).

#### 5. Bộ nhớ đệm & Memory (Redis)

Dùng để lưu trữ bộ nhớ ngắn hạn của hội thoại (Short-term memory) và tăng tốc truy cập.

+ **REDIS_CLIENT_HOST**: Địa chỉ host của Redis.
+ **REDIS_PORT**: Port của Redis (mặc định: 6379).

#### 6. Giám sát (Logfire)

+ **LOGFIRE_TOKEN**: Token dùng để đẩy log lên hệ thống giám sát Pydantic Logfire.

---

**Lưu ý**: Bạn có thể tham khảo tệp `backend/.env.example` trong mã nguồn dự án để biết đầy đủ các biến cần thiết.
