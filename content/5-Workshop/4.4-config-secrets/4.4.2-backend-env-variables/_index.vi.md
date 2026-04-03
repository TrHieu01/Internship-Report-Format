---
title : "Biến môi trường Backend"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 4.4.2 </b> "
---

#### AI model cho Chatbot

+ **Tên model**: `<ten-model-chatbot>`
+ **Provider**: `<OpenAI/Anthropic/Google/...>`
+ **API key**: lấy trong trang quản lý API của provider.
+ **Cách lấy key**: đăng nhập portal của provider → tạo API key → lưu vào secret **CHATBOT_API_KEY**.

#### AI model cho Camera

+ **Tên model**: `<ten-model-camera>`
+ **Provider**: `<AWS Rekognition/Custom model/...>`
+ **API key / credential**: dùng IAM role hoặc API key tùy provider.
+ **Cách lấy**: tạo credential/role trên AWS hoặc provider → lưu vào secret **CAMERA_API_KEY** (nếu có).
+ **Nếu self-hosted**: tải model từ repo chính thức hoặc Model Zoo của provider.

#### .env.example

1. **AI models**: model name, provider, API key.
2. **Database**: **DB_HOST**, **DB_PORT**, **DB_USER**, **DB_PASS**.
3. **Auth**: JWT secret, Cognito pool ID.
4. **Email**: SMTP host, user, password.
5. **Storage**: S3 bucket name, region.
