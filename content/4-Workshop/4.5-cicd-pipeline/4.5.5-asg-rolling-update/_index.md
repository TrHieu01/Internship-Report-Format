---
title : "Job ASG Rolling Update"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 4.5.5 </b> "
---

#### Overview

The Deploy to ASG Job is responsible for deploying the new image into the Auto Scaling Group using a rolling update mechanism and verifying the rollout. This ensures the system updates stably without service disruption.

#### Run Conditions & Environment Variables

**Trigger/Conditions**

- needs: [terraform, build]
- if: only runs when both terraform/build succeed and the workflow is triggered in the correct context.

**Key Environment Variables**

- ASG_NAME, IMAGE_TAG, ECR_REPOSITORY_URL
- ALB_DNS_NAME, API_DOMAIN_NAME, BACKEND_TARGET_GROUP_ARN
- BACKEND_ENV_FILE, SECRETS_KMS_KEY_ARN, TF_DIR

```yaml
needs: [terraform, build]
if: always() && needs.terraform.result == 'success' && needs.build.result == 'success' &&
    (github.event_name == 'workflow_dispatch' || github.event.workflow_run.conclusion == 'success')
env:
  ASG_NAME: ${{ needs.terraform.outputs.asg_name }}
  IMAGE_TAG: ${{ needs.build.outputs.image_tag }}
  ECR_REPOSITORY_URL: ${{ needs.terraform.outputs.ecr_repository_url }}
  ALB_DNS_NAME: ${{ needs.terraform.outputs.alb_dns_name }}
  API_DOMAIN_NAME: ${{ needs.terraform.outputs.api_domain_name }}
  BACKEND_TARGET_GROUP_ARN: ${{ needs.terraform.outputs.backend_target_group_arn }}
  BACKEND_ENV_FILE: ${{ secrets.BACKEND_ENV_FILE }}
  SECRETS_KMS_KEY_ARN: ${{ needs.terraform.outputs.secrets_kms_key_arn }}
  TF_DIR: .github/terraform
```

#### Main Task Groups

1. **AWS Preparation and Authentication**
   - Checkout code
   - Configure AWS credentials

   ```yaml
   - name: Checkout code
     uses: actions/checkout@v4

   - name: Configure AWS credentials
     uses: aws-actions/configure-aws-credentials@v4
     with:
       aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
       aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
       aws-region: ${{ env.AWS_REGION }}
   ```

2. **Sync Backend Environment Variables**
   - Push BACKEND_ENV_FILE into SSM Parameter Store (SecureString, KMS).

   ```yaml
   - name: Update Environment Variables in SSM
     run: |
       aws ssm put-parameter \
         --name "/edutrust/backend/env" \
         --value "$BACKEND_ENV_FILE" \
         --type "SecureString" \
         --key-id "$SECRETS_KMS_KEY_ARN" \
         --overwrite
   ```

3. **Prepare Terraform for Rollout**
   - Setup Terraform.
   - Cache Terraform plugins.

   ```yaml
   - name: Setup Terraform
     uses: hashicorp/setup-terraform@v3
     with:
       terraform_version: "1.14.6"
       terraform_wrapper: false

   - name: Cache Terraform plugins
     uses: actions/cache@v4
     with:
       path: ~/.terraform.d/plugin-cache
       key: ${{ runner.os }}-terraform-${{ hashFiles('.github/terraform/*.tf') }}
   ```

4. **Update Launch Template**
   - Terraform plan with the new backend_image_tag.
   - Detect Launch Template changes.
   - Apply if changes exist.

   ```yaml
   - name: Update Launch Template with new tag
     run: |
       printf "%s\n" "$TF_VARS" > terraform.tfvars
       terraform init
       terraform plan -detailed-exitcode -input=false -out=tfplan -var="backend_image_tag=$IMAGE_TAG"
   ```

5. **ASG Rolling Update**
   - Start instance refresh when Launch Template changes.
   - Monitor refresh progress and handle failed/canceled states.

   ```yaml
   - name: Start ASG Instance Refresh
     run: |
       aws autoscaling start-instance-refresh \
         --auto-scaling-group-name "${ASG_NAME}" \
         --preferences '{"MinHealthyPercentage": 50, "InstanceWarmup": 90}'
   ```

6. **Skip Refresh when No Change**
   - Skip rolling update if Launch Template remains unchanged.

   ```yaml
   - name: Skip ASG Instance Refresh
     run: |
       echo "Launch template did not change in Terraform plan, so instance refresh is skipped."
       echo "ROLLING_REFRESH_STARTED=false" >> "$GITHUB_ENV"
   ```

7. **Verify Rollout**
   - Check image existence in ECR.
   - Check target group health.
   - Call /health via custom domain or ALB DNS.

   ```yaml
   - name: Verify rollout (ECR image exists, targets healthy, /health OK)
     run: |
       aws ecr describe-images --repository-name "${repo_name}" --image-ids imageTag="${tag}"
       aws elbv2 describe-target-health --target-group-arn "${BACKEND_TARGET_GROUP_ARN}"
       curl "${health_url}"
   ```

#### Note

- Refresh only when the Launch Template changes to avoid unnecessary churn.
- Always verify target health and /health to ensure a successful rollout.
- Record logs/diagnostics when fallout fails to quickly trace the cause.
