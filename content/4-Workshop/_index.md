---
title: "Workshop"
date: 2024-01-01
weight: 4
chapter: false
pre: " <b> 4. </b> "
---
{{% notice warning %}}
⚠️ **Note:** The information below is for reference purposes only. Please **do not copy verbatim** for your report, including this warning.
{{% /notice %}}

# EduTrust Workshop

#### Overview

EduTrust is a learning support system with AI chatbot assistance and AI camera-based exam monitoring, deployed on AWS for scalability, security, and operational stability. This workshop documents the setup context and the standard deployment flow for the team.

In this workshop, we provision infrastructure with Terraform in CI/CD, configure backend services and frontend on AWS Amplify, and integrate the chatbot and AI camera components.

The workflow is organized into:

- **Infrastructure**: VPC, ALB, EC2 Auto Scaling, S3, ECR, IAM via Terraform and output validation.  
- **Application**: Frontend via Amplify and backend via pipeline, plus environment variables and secrets.  
- **Monitoring & Security**: WAF, CloudWatch alarms, and SNS notifications.

#### Content

1. [Architecture Overview](4.1-architecture-overview)
2. [Environment Setup](4.2-prerequisites/)
3. [Fork & Clone Repo](4.3-fork-clone-repo/)
4. [Config & Secrets](4.4-config-secrets/)
5. [CI/CD Guide](4.5-cicd-pipeline/)
6. [Frontend Deployment & Security](4.6-frontend-deployment-security/)
7. [CloudWatch Monitoring & SNS Alerts](4.7-observability-validation/)
8. [Cleanup](4.8-cleanup/)
