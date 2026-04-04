---
title : "Job Terraform"
date : 2024-01-01
weight : 3
chapter : true
pre : " <b> 4.5.3 </b> "
---

#### Overview

This section introduces the Terraform Job in EduTrust's CI/CD pipeline, which is the main infrastructure build step following the Infrastructure as Code (IaC) model. The infrastructure is defined as version-controlled configuration, allowing for standardized change tracking and reproducible deployment. The IaC approach increases reproducibility, improves auditability, reduces configuration drift between environments, and automates a large part of the deployment lifecycle. The job also plays a role in providing outputs to link data between jobs, ensuring consistency and integrity throughout the deployment chain.

#### Content

1. [Run Conditions & Outputs](4.5.3.1-dieu-kien-chay-outputs/)
2. [Terraform Environment Preparation](4.5.3.2-chuan-bi-moi-truong-terraform/)
3. [ECR Configuration & AWS Authentication](4.5.3.3-doc-cau-hinh-ecr-xac-thuc-aws/)
4. [S3 Storage for Terraform State Files](4.5.3.4-s3-luu-tru-terraform-state/)
5. [Terraform State Initialization & Import](4.5.3.5-khoi-tao-import-terraform-state/)
6. [Infrastructure Deployment & Output Collection](4.5.3.6-trien-khai-ha-tang-thu-thap-outputs/)
7. [Resources Created After Terraform Apply](4.5.3.7-tai-nguyen-duoc-tao/)
