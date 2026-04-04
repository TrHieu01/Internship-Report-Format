---
title : "Job Build ECR"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 4.5.4 </b> "
---

#### Overview

The Job Build ECR is responsible for building and pushing the backend Docker image to Amazon ECR. This job only runs after the Terraform Job completes successfully, ensuring that the ECR repository and infrastructure parameters are ready.

#### Run Conditions & Outputs

**Trigger/Conditions**

- needs: terraform
- if: only runs if terraform succeeds and the workflow is triggered in the correct context.

**Outputs**

- image: ECR repository URL
- image_tag: tag based on commit SHA

**Relevant Configuration Snippet**

```yaml
needs: terraform
if: always() && needs.terraform.result == 'success' &&
    (github.event_name == 'workflow_dispatch' || github.event.workflow_run.conclusion == 'success')
outputs:
  image: ${{ steps.image_vars.outputs.image }}
  image_tag: ${{ steps.image_vars.outputs.image_tag }}
```

#### Main Task Groups

1. **AWS Preparation and Authentication**
   - Checkout code
   - Configure AWS credentials

   **Relevant Configuration Snippet**

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

2. **Set Image and Tag Variables**
   - Get ECR URL from Terraform outputs.
   - Tag based on commit SHA.

   **Relevant Configuration Snippet**

   ```yaml
   - name: Set image variables
     id: image_vars
     run: |
       echo "image=${ECR_REPOSITORY_URL}" >> "$GITHUB_OUTPUT"
       echo "image_tag=${{ github.sha }}" >> "$GITHUB_OUTPUT"
   ```

3. **Login to ECR**
   - Login to push image to registry.

   **Relevant Configuration Snippet**

   ```yaml
   - name: Login to Amazon ECR
     id: login_ecr
     uses: aws-actions/amazon-ecr-login@v2
   ```

4. **Compute Docker Tags**
   - If immutable=true: only use the SHA tag.
   - If immutable=false: add the `latest` tag for quick updates.

   **Relevant Configuration Snippet**

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
   - Use Buildx for multi-platform builds.
   - Push image to ECR with caching enabled.

   **Relevant Configuration Snippet**

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

#### Role

Standardizes and publishes backend images to ECR so that ASG/EC2 can pull them for automated deployment.
