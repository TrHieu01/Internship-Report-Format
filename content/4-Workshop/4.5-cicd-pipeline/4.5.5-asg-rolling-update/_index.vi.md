---
title : "Job ASG Rolling Update"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 4.5.5 </b> "
---

#### Tổng quan

Job Deploy to ASG chịu trách nhiệm triển khai image mới vào Auto Scaling Group theo cơ chế rolling update và xác thực rollout, bảo đảm hệ thống cập nhật ổn định mà không gián đoạn dịch vụ.

#### Điều kiện chạy & Biến môi trường

**Trigger/Điều kiện**

- needs: [terraform, build]
- if: chỉ chạy khi cả terraform/build thành công và workflow được kích hoạt đúng ngữ cảnh

**Biến môi trường chính**

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

#### Các nhóm tác vụ chính

1. **Chuẩn bị & xác thực AWS**
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

2. **Đồng bộ biến môi trường backend**
   - Đẩy BACKEND_ENV_FILE vào SSM Parameter Store (SecureString, KMS)

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

3. **Chuẩn bị Terraform cho rollout**
   - Setup Terraform
   - Cache Terraform plugins

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

4. **Cập nhật Launch Template**
   - Terraform plan với backend_image_tag mới
   - Detect thay đổi Launch Template
   - Apply nếu có thay đổi

   ```yaml
   - name: Update Launch Template with new tag
     run: |
       printf "%s\n" "$TF_VARS" > terraform.tfvars
       terraform init
       terraform plan -detailed-exitcode -input=false -out=tfplan -var="backend_image_tag=$IMAGE_TAG"
   ```

5. **Rolling Update ASG**
   - Start instance refresh khi Launch Template thay đổi
   - Theo dõi tiến độ refresh và xử lý các trạng thái fail/cancel

   ```yaml
   - name: Start ASG Instance Refresh
     run: |
       aws autoscaling start-instance-refresh \
         --auto-scaling-group-name "${ASG_NAME}" \
         --preferences '{"MinHealthyPercentage": 50, "InstanceWarmup": 90}'
   ```

6. **Skip refresh khi không thay đổi**
   - Bỏ qua rolling update nếu Launch Template không đổi

   ```yaml
   - name: Skip ASG Instance Refresh
     run: |
       echo "Launch template did not change in Terraform plan, so instance refresh is skipped."
       echo "ROLLING_REFRESH_STARTED=false" >> "$GITHUB_ENV"
   ```

7. **Verify rollout**
   - Kiểm tra image tồn tại trong ECR
   - Kiểm tra target group healthy
   - Gọi /health qua custom domain hoặc ALB DNS

   ```yaml
   - name: Verify rollout (ECR image exists, targets healthy, /health OK)
     run: |
       aws ecr describe-images --repository-name "${repo_name}" --image-ids imageTag="${tag}"
       aws elbv2 describe-target-health --target-group-arn "${BACKEND_TARGET_GROUP_ARN}"
       curl "${health_url}"
   ```

#### Lưu Ý

- Chỉ refresh khi Launch Template thay đổi để tránh churn không cần thiết.
- Luôn verify target health và /health để đảm bảo rollout thành công.
- Ghi log/diagnostics khi rollout fail để truy vết nhanh nguyên nhân.
