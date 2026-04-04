---
title : "Terraform State Initialization & Import"
date : 2024-01-01
weight : 5
chapter : false
pre : " <b> 4.5.3.5 </b> "
---

#### Objectives

Establish a backend state connection and synchronize the Terraform state with actual infrastructure to prevent deployment drift.

#### Main Content

1. Execute `terraform init` to link the state storage backend (S3), ensuring state is read/written to the correct location.
2. Import the ECR repository if the resource already exists, bringing it into the state to avoid conflicts during apply.

💡 State drift occurs when the state record differs from the actual infrastructure. Importing helps synchronize state and reduces the risk of "resource already exists" errors.

**Explanation**

- Initialize the backend so Terraform can read/write the state to the correct storage location.

  ```bash
  terraform init
  ```

- Read the ECR repository name from `terraform.tfvars` (if available), then check if the repository exists in AWS.

  ```bash
  REPO_NAME="$(awk -F= '... ecr_repository_name ...' terraform.tfvars || true)"
  aws ecr describe-repositories --repository-names "$REPO_NAME"
  ```

- The goal is to determine if the resource was created manually or from a previous run, thereby avoiding name conflicts and minimizing errors when Terraform recreates the repository.

- If the ECR exists but is not yet in the state, perform an import to synchronize; if it does not exist, let Terraform create it during apply.

  ```bash
  terraform state show aws_ecr_repository.backend
  terraform import aws_ecr_repository.backend "$REPO_NAME"
  ```

**Relevant Configuration Snippet**

```yaml
- name: Terraform Init
  working-directory: ${{ env.TF_DIR }}
  run: terraform init

- name: Import existing ECR repository (if already created)
  working-directory: ${{ env.TF_DIR }}
  run: |
    set -euo pipefail
    if [ -f terraform.tfvars ]; then
      REPO_NAME="$(awk -F= '
        $1 ~ /^[[:space:]]*ecr_repository_name[[:space:]]*$/ {
          v=$2
          gsub(/^[[:space:]]+|[[:space:]]+$/, "", v)
          gsub(/\"/, "", v)
          print v
          exit
        }' terraform.tfvars || true)"
    fi
    REPO_NAME="${REPO_NAME:-edutrust-backend}"
    if aws ecr describe-repositories --repository-names "$REPO_NAME" >/dev/null 2>&1; then
      if terraform state show aws_ecr_repository.backend >/dev/null 2>&1; then
        echo "ECR repo already in Terraform state, skipping import."
      else
        terraform import aws_ecr_repository.backend "$REPO_NAME"
      fi
    else
      echo "ECR repo not found in AWS; Terraform will create it."
    fi
```
