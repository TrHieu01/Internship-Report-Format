---
title : "Job Build ECR"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 4.6.4 </b> "
---

#### Overview

<div align="justify">
The **Build & Push backend image** job is responsible for packaging the application's source code into a Docker image and pushing it to Amazon ECR. In this project, the build process is optimized using Docker Buildx to leverage layer caching, which significantly saves resources and reduces build time.
</div>

#### Key Components of the Workflow

1. **Docker Tag Computation**
   The system utilizes a flexible combination of tags:
   - **SHA Tag**: Attaches the commit SHA (`${{ github.sha }}`) to ensure uniqueness and traceability between the image and the code.
   - **Latest Tag**: (If `ecr_tag_immutable` is set to false) Automatically updates the `latest` tag for rapid testing purposes.

2. **Docker Buildx & GHA Caching**
   Uses `docker/setup-buildx-action` to initialize a modern builder. Integrates `cache-from: type=gha` and `cache-to: type=gha,mode=max` to store intermediate layers directly on GitHub Actions, allowing subsequent builds to take seconds instead of minutes.

#### Representative YAML Configuration

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
        # Tagging logic for SHA and Latest
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

#### Technical Role
+ **Artifact Management**: Manages software versions as secure container images on ECR.
+ **Performance Optimization**: Acceleration of its own development (Feedback loop) thanks to intelligent caching mechanisms.
