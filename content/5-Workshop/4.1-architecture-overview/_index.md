---
title : "Architecture Overview"
date : 2024-01-01 
weight : 1
chapter : false
pre : " <b> 4.1. </b> "
---

#### Introduction

EduTrust is an AI Camera-based learning support and exam supervision system deployed on AWS to ensure scalability, security, and stable operation. This workshop focuses on setting up the architecture and standard deployment flow for the team.

#### AWS Architecture Overview

Internet → Amplify → Application Load Balancer → EC2 Auto Scaling → Backend services

![Kiến trúc EduTrust](edutrust-architect.png)

#### Main Components (by layer)

**Client/Presentation Layer**

+ **Amplify**: Hosts the frontend and connects to custom domains.

**Traffic/Delivery Layer**

+ **Application Load Balancer**: Distributes requests to the backend.

**Compute/Service Layer**

+ **EC2 Auto Scaling**: Runs backend services based on load.
+ **Backend services**: APIs, AI processing, camera events, and authentication.

**Data Layer**

+ **Data**: Stores logs, videos, and exam results (S3/DB).

#### List of Services Used

**Frontend & Edge Layer**

+ AWS Amplify
+ AWS WAF
+ AWS Route 53
+ AWS ACM

**Identity Layer**

+ Amazon Cognito

**Networking Layer**

+ Amazon VPC (public/private subnets)
+ Internet Gateway
+ NAT Gateway
+ Application Load Balancer

**Compute & Container Layer**

+ Amazon EC2
+ EC2 Auto Scaling
+ Amazon ECR

**Data & Storage Layer**

+ Amazon S3 (frontend assets, logs, Terraform state)
+ Amazon RDS
+ Amazon ElastiCache for Redis

**Observability Layer**

+ Amazon CloudWatch
+ VPC Flow Logs
+ Amazon SNS

**Security & Configuration Layer**

+ AWS KMS
+ AWS Systems Manager Parameter Store
+ AWS PrivateLink

**CI/CD & IaC Layer**

+ GitHub Actions
+ Packer
+ Terraform

#### High Availability (HA) and Multi-AZ

+ EC2 Auto Scaling runs across multiple Availability Zones (AZs) to ensure HA.
+ Application Load Balancer automatically distributes traffic across AZs.
+ Critical data is stored on managed services (RDS/S3) to increase durability.

#### Architecture and Responsibilities Overview

+ **Amplify**: Serves the user interface, manages domain connectivity, and handles HTTPS.
+ **Application Load Balancer**: Acts as the orchestration layer, routing requests to the backend.
+ **EC2 Auto Scaling**: Ensures the backend scales automatically as load increases.
+ **Backend services**: Handles business logic, AI, camera events, and authentication.
+ **Data layer**: Stores exam data, logs, video, and results.

#### Main Flow in the Workshop

1. Users access the frontend via Amplify.
2. The frontend calls APIs through the Application Load Balancer.
3. The backend processes logic, invokes AI services, and receives events from the camera.
4. Data is stored and displayed back to the user.
