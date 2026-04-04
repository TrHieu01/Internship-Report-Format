---
title : "Job CI"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.5.1 </b> "
---

#### Tasks Included in Job CI

**Trigger**

- **Pull Request** when changes occur in: backend source code, formatting rules, CI/CD workflows, containerization, or IaC infrastructure.
- **Merge PR to Main** (push event) with the same scope of changes as above.
- **workflow_dispatch** in GitHub Actions (if needed).

**Main Task Groups**

1. **Pre-commit Checks**
   - Checkout source code and set up Python 3.11.
   - Leverage **pre-commit** cache to optimize runtime.
   - Execute **pre-commit** based on the standardized configuration in **.pre-commit-config.yaml**.

2. **Backend Test & Coverage**
   - Checkout source code with full history for testing/coverage.
   - Set up **uv** and Python 3.11, install dependencies using **uv sync --dev**.
   - Load **.env** from secret **BACKEND_ENV_FILE** (if available).
   - Execute **pytest** and export the **coverage.xml** report.

3. **Terraform Validate & Security Scan**
   - Set up Terraform **1.14.6**.
   - Check formatting with **terraform fmt -check -recursive**.
   - Execute **terraform init -backend=false** and **terraform validate**.
   - Scan Terraform security using Checkov, stopping the pipeline if violations are detected.

#### Role

Ensures the quality of the backend source code, adherence to infrastructure standards, and security of configurations before merging or deploying to staging/production environments.
