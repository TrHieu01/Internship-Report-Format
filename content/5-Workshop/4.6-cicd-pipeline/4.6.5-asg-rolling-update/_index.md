---
title : "Job ASG Rolling Update"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 4.6.5 </b> "
---

#### Overview

<div align="justify">
The **Deploy to ASG** job is responsible for updating the application to the new version on the live infrastructure without service interruption. This process combines configuration management (SSM), infrastructure blueprint updates (Terraform Launch Template), and gradual instance replacement (ASG Instance Refresh).
</div>

#### Deployment Phases

1. **Configuration Update (SSM Parameter Store)**
   The system loads sensitive environment variables into the `SSM Parameter Store` as a `SecureString`. This ensures complete separation between configuration and source code while allowing instances to automatically load settings upon startup.

2. **Launch Template Update (Terraform)**
   Instead of manual intervention, the pipeline calls Terraform to update the `Launch Template` with the latest ECR image tag. This is the "blueprint" that the Auto Scaling Group will use to create new instances.

3. **Instance Refresh & Monitoring**
   Uses AWS's `start-instance-refresh` feature to replace old instances with new ones. The pipeline integrates an intelligent Bash script loop to monitor the `% complete` status and automatically abort/fail if the refresh process encounters issues.

4. **Rollout Verification**
   After the refresh is complete, the pipeline performs final verification steps:
   - Checks the response code from the `/health` endpoint.
   - Verifies that the number of Healthy Instances in the Target Group meets expectations.

#### Technical Roles
+ **Zero Downtime**: Ensures the service remains available throughout the update process.
+ **Safety Net**: Automatically detects deployment failures and halts the update process to protect the system.
+ **Traceability**: Every version change is recorded via Terraform state and ECR tags.
