---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---
{{% notice warning %}}
⚠️ **Note:** The information below is for reference purposes only. Please **do not copy verbatim** for your report, including this warning.
{{% /notice %}}

In this section, you need to summarize the contents of the workshop that you **plan** to conduct.

# IoT Weather Platform for Lab Research
## A Unified AWS Serverless Solution for Real-Time Weather Monitoring

### 1. Executive Summary
The IoT Weather Platform is designed for the ITea Lab team in Ho Chi Minh City to enhance weather data collection and analysis. It supports up to 5 weather stations, with potential scalability to 10-15, utilizing Raspberry Pi edge devices with ESP32 sensors to transmit data via MQTT. The platform leverages AWS Serverless services to deliver real-time monitoring, predictive analytics, and cost efficiency, with access restricted to 5 lab members via Amazon Cognito.

### 2. Problem Statement
### Current Problems
Online exams face multiple challenges: manual proctoring is labor‑intensive, cheating is difficult to detect (phones, multiple faces in frame, leaving the camera), there is no centralized system to manage classes — exams — results, and students lack intelligent learning support tools.

### The Solution
EduTrust provides a comprehensive platform including:
- **Class & Exam Management**: Admin creates classes, assigns homeroom/subject teachers; teachers create multiple‑choice exams with secret keys and start/end times.
- **AI Proctoring**: Integrates YOLOv26n to detect violations in real time (MULTIPLE_FACES, FACE_DISAPPEARED, FORBIDDEN_OBJECT). Evidence images are stored in Amazon S3 and logged in MongoDB.
- **AI Learning Assistant**: Multi‑agent system (Pydantic AI) helps students search knowledge, ask questions, and find learning materials.
- **Authentication & Security**: JWT (via Cognito) with role‑based access control (RBAC).

### Benefits and ROI
The solution reduces teachers’ manual workload, improves transparency and fairness, and automates grading with evidence stored in S3. Operational cost stays low by leveraging MongoDB Atlas (free tier), Redis Cloud, and AWS S3/Amplify. Estimated AWS cost is under 5 USD/month for a mid‑size school.

### 3. Solution Architecture
EduTrust applies a **fullstack monorepo** architecture with a Python FastAPI backend and a Next.js frontend, deployed via Docker. Data is stored in MongoDB (users, exams, classes, submissions, violations), session/conversation cache uses Redis, and violation images are stored in Amazon S3. The architecture is shown below:

![EduTrust Solution Architecture](/images/2-Proposal/edutrust-architect.png)

### Services & Technology (Aligned with Architecture)
- **AWS Amplify + CloudFront**: Hosts the Next.js frontend and delivers content via CDN.
- **Amazon Route 53 + AWS ACM**: DNS and TLS/HTTPS certificate management.
- **AWS WAF**: Web application firewall protection.
- **Amazon VPC (public/private subnets)**: Network isolation and segmentation.
- **Application Load Balancer (ALB)**: Distributes traffic to backend services.
- **Amazon EC2 Auto Scaling**: Scales backend compute based on load.
- **Amazon ECR**: Container registry for backend images.
- **Amazon S3**: Stores violation images, ALB logs, and Terraform state.
- **Amazon DynamoDB**: Key-value data store (as shown in the architecture).
- **Amazon ElastiCache for Redis**: Cache/session layer for fast access.
- **Amazon Cognito**: Authentication and user management.
- **Amazon CloudWatch + VPC Flow Logs + SNS**: Monitoring, logs, and alerting.
- **AWS KMS + SSM Parameter Store + PrivateLink**: Secrets and secure internal access.
- **Terraform + GitHub Actions**: Infrastructure as Code and CI/CD automation.

### Application Stack
- **FastAPI**: Async backend API framework with automatic docs.
- **Next.js + Tailwind CSS**: Frontend app with modern UI.
- **YOLOv26n (Ultralytics)**: AI object detection for proctoring.
- **Pydantic AI + LiteLLM**: Multi-agent orchestration for the chatbot.
- **Docker**: Containerization with multi-stage builds.

### Component Design
- **Authentication (Auth)**: JWT access/refresh tokens, session via cookies, RBAC (admin/teacher/student).
- **Class Management**: Assign homeroom/subject teachers, add/remove students, auto update status (active/inactive).
- **Exam Management**: Create MCQ exams, auto generate secret keys, control start/end time, auto grading on submit.
- **Camera Proctoring (Detection)**: CameraService receives frames, YOLO detects violations, ViolationLogger writes MongoDB + S3, ScreenshotUtils captures evidence.
- **AI Agent**: UnifiedAgent orchestrates sub‑agents (technical, social, general, web_search) with tool delegation and WebSocket streaming.

### 4. Technical Implementation
**Implementation Phases**
This project has two parts—setting up weather edge stations and building the weather platform—each following 4 phases:
- Build Theory and Draw Architecture: Research Raspberry Pi setup with ESP32 sensors and design the AWS serverless architecture (1 month pre-internship)
- Calculate Price and Check Practicality: Use AWS Pricing Calculator to estimate costs and adjust if needed (Month 1).
- Fix Architecture for Cost or Solution Fit: Tweak the design (e.g., optimize Lambda with Next.js) to stay cost-effective and usable (Month 2).
- Develop, Test, and Deploy: Code the Raspberry Pi setup, AWS services with CDK/SDK, and Next.js app, then test and release to production (Months 2-3).

**Technical Requirements**
- Weather Edge Station: Sensors (temperature, humidity, rainfall, wind speed), a microcontroller (ESP32), and a Raspberry Pi as the edge device. Raspberry Pi runs Raspbian, handles Docker for filtering, and sends 1 MB/day per station via MQTT over Wi-Fi.
- Weather Platform: Practical knowledge of AWS Amplify (hosting Next.js), Lambda (minimal use due to Next.js), AWS Glue (ETL), S3 (two buckets), IoT Core (gateway and rules), and Cognito (5 users). Use AWS CDK/SDK to code interactions (e.g., IoT Core rules to S3). Next.js reduces Lambda workload for the fullstack web app.

### 5. Timeline & Milestones
**Project Timeline**
- Pre-Internship (Month 0): 1 month for planning and old station review.
- Internship (Months 1-3): 3 months.
    - Month 1: Study AWS and upgrade hardware.
    - Month 2: Design and adjust architecture.
    - Month 3: Implement, test, and launch.
- Post-Launch: Up to 1 year for research.

### 6. Budget Estimation
You can find the budget estimation on the [AWS Pricing Calculator](https://calculator.aws/#/estimate?id=621f38b12a1ef026842ba2ddfe46ff936ed4ab01).  
Or you can download the [Budget Estimation File](../attachments/budget_estimation.pdf).

### Infrastructure Costs
- AWS Services:
    - AWS Lambda: $0.00/month (1,000 requests, 512 MB storage).
    - S3 Standard: $0.15/month (6 GB, 2,100 requests, 1 GB scanned).
    - Data Transfer: $0.02/month (1 GB inbound, 1 GB outbound).
    - AWS Amplify: $0.35/month (256 MB, 500 ms requests).
    - Amazon API Gateway: $0.01/month (2,000 requests).
    - AWS Glue ETL Jobs: $0.02/month (2 DPUs).
    - AWS Glue Crawlers: $0.07/month (1 crawler).
    - MQTT (IoT Core): $0.08/month (5 devices, 45,000 messages).

Total: $0.7/month, $8.40/12 months

- Hardware: $265 one-time (Raspberry Pi 5 and sensors).

### 7. Risk Assessment
#### Risk Matrix
- Network Outages: Medium impact, medium probability.
- Sensor Failures: High impact, low probability.
- Cost Overruns: Medium impact, low probability.

#### Mitigation Strategies
- Network: Local storage on Raspberry Pi with Docker.
- Sensors: Regular checks and spares.
- Cost: AWS budget alerts and optimization.

#### Contingency Plans
- Revert to manual methods if AWS fails.
- Use CloudFormation for cost-related rollbacks.

### 8. Expected Outcomes
#### Technical Improvements: 
Real-time data and analytics replace manual processes.  
Scalable to 10-15 stations.
#### Long-term Value
1-year data foundation for AI research.  
Reusable for future projects.
