---
title : "Job Build ECR"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 4.6.4 </b> "
---

#### Tổng quan

<div align="justify">
Job **Build & Push backend image** chịu trách nhiệm đóng gói mã nguồn ứng dụng thành Docker image và đẩy lên Amazon ECR. Trong dự án này, quy trình đóng gói được tối ưu hoá bằng cách sử dụng Docker Buildx để tận dụng tính năng layer caching, giúp tiết kiệm tài nguyên và thời gian build đáng kể.
</div>

#### Các thành phần chính của quy trình

1. **Tính toán Docker Tags**
   Hệ thống sử dụng tổ hợp thẻ (tags) linh hoạt:
   - **SHA Tag**: Gắn mã commit SHA (`${{ github.sha }}`) để đảm bảo tính duy nhất và khả năng truy vết (traceability).
   - **Latest Tag**: (Nếu cấu hình `ecr_tag_immutable` là false) Tự động cập nhật tag `latest` để phục vụ các mục đích kiểm thử nhanh.

2. **Docker Buildx & GHA Caching**
   Sử dụng `docker/setup-buildx-action` để khởi tạo trình xây dựng (builder) hiện đại. Tích hợp `cache-from: type=gha` và `cache-to: type=gha,mode=max` để lưu trữ mã máy (intermediate layers) trực tiếp trên GitHub Actions, giúp các lần build sau chỉ mất vài chục giây thay vì vài phút.

#### Cấu hình YAML tiêu biểu

```yaml
build:
  name: Build & Push backend image (ECR)
  runs-on: ubuntu-latest
  needs: terraform
  steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Login to Amazon ECR
      id: login_ecr
      uses: aws-actions/amazon-ecr-login@v2

    - name: Compute Docker tags
      id: docker_tags
      run: |
        # Logic tính toán tag SHA và latest
        IMAGE="${{ needs.terraform.outputs.ecr_repository_url }}"
        TAGS="${IMAGE}:${{ github.sha }}\n${IMAGE}:latest"
        echo "tags=$(printf "$TAGS")" >> "$GITHUB_OUTPUT"

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

#### Vai trò kỹ thuật
+ **Artifact Management**: Quản lý phiên bản phần mềm dưới dạng container images an toàn trên ECR.
+ **Performance Optimization**: Tăng tốc chu trình phát triển (Feedback loop) nhờ cơ chế cache thông minh.
