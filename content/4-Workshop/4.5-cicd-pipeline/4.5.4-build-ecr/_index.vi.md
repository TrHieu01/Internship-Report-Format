---
title : "Job Build ECR"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 4.5.4 </b> "
---

#### Tổng quan

Job Build ECR chịu trách nhiệm build và push Docker image của backend lên Amazon ECR. Job này chỉ chạy sau khi Job Terraform hoàn tất thành công, nhằm bảo đảm ECR repository và các thông số hạ tầng đã sẵn sàng.

#### Điều kiện chạy & Outputs

**Trigger/Điều kiện**

- needs: terraform
- if: chỉ chạy khi terraform thành công và workflow được kích hoạt đúng ngữ cảnh

**Outputs**

- image: URL của ECR repository
- image_tag: tag theo commit SHA

**Trích đoạn cấu hình liên quan**

```yaml
needs: terraform
if: always() && needs.terraform.result == 'success' &&
    (github.event_name == 'workflow_dispatch' || github.event.workflow_run.conclusion == 'success')
outputs:
  image: ${{ steps.image_vars.outputs.image }}
  image_tag: ${{ steps.image_vars.outputs.image_tag }}
```

#### Các nhóm tác vụ chính

1. **Chuẩn bị và xác thực AWS**
   - Checkout code
   - Configure AWS credentials

   **Trích đoạn cấu hình liên quan**

   ```yaml
   - name: Checkout code
     uses: actions/checkout@v4

   - name: Configure AWS credentials
     uses: aws-actions/configure-aws-credentials@v4
     with:
       aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
       aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
       aws-region: ${{ needs.terraform.outputs.aws_region }}
   ```

2. **Đặt biến image & tag**
   - Lấy URL ECR từ outputs của Terraform
   - Tag theo commit SHA

   **Trích đoạn cấu hình liên quan**

   ```yaml
   - name: Set image variables
     id: image_vars
     run: |
       echo "image=${ECR_REPOSITORY_URL}" >> "$GITHUB_OUTPUT"
       echo "image_tag=${{ github.sha }}" >> "$GITHUB_OUTPUT"
   ```

3. **Đăng nhập ECR**
   - Login để push image lên registry

   **Trích đoạn cấu hình liên quan**

   ```yaml
   - name: Login to Amazon ECR
     id: login_ecr
     uses: aws-actions/amazon-ecr-login@v2
   ```

4. **Tính toán tags Docker**
   - Nếu immutable=true: chỉ dùng tag theo SHA
   - Nếu immutable=false: thêm tag latest để cập nhật nhanh

   **Trích đoạn cấu hình liên quan**

   ```yaml
   - name: Compute Docker tags
     id: docker_tags
     env:
       IMAGE: ${{ steps.image_vars.outputs.image }}
       IMAGE_TAG: ${{ steps.image_vars.outputs.image_tag }}
       ECR_TAG_IMMUTABLE: ${{ needs.terraform.outputs.ecr_tag_immutable }}
     run: |
       set -euo pipefail
       SHA_TAG="${IMAGE}:${IMAGE_TAG}"
       if [ "$ECR_TAG_IMMUTABLE" = "true" ]; then
         TAGS="$SHA_TAG"
       else
         TAGS="$SHA_TAG\n${IMAGE}:latest"
       fi
       {
         echo "tags<<EOF"
         printf "%b\n" "$TAGS"
         echo "EOF"
       } >> "$GITHUB_OUTPUT"
   ```

5. **Build & Push**
   - Dùng Buildx để build đa nền tảng
   - Push image lên ECR, có cache để tăng tốc

   **Trích đoạn cấu hình liên quan**

   ```yaml
   - name: Set up Docker Buildx
     uses: docker/setup-buildx-action@v3

   - name: Build and push Docker image
     uses: docker/build-push-action@v6
     with:
       context: .
       file: Dockerfile
       push: true
       tags: ${{ steps.docker_tags.outputs.tags }}
       cache-from: type=gha
       cache-to: type=gha,mode=max
   ```

#### Vai trò

+ Chuẩn hoá và phát hành image backend lên ECR để ASG/EC2 có thể kéo về triển khai tự động.
