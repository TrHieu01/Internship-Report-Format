---
title : "S3 Storage for Terraform State Files"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 4.5.3.4 </b> "
---

#### Objectives

Create a storage location for Terraform state files before running `terraform init`, ensuring that the management of resources created by IaC remains consistent and traceable.

<small><i>A Terraform state file is a record of the current infrastructure state, used to compare and determine changes when running Terraform; therefore, it needs separate, secure, and controlled storage.</i></small>

#### Main Content

Terraform's state file is a critical source of truth reflecting the actual infrastructure state and is used to calculate changes during the apply process. Thus, the state must be stored in a separate, stable, and secure backend. In this project, S3 is chosen as the state storage through the **Ensure Terraform State Bucket Exists** step.

Explanation of the logic:

1. Check if the bucket already exists.
2. If not, create the bucket with the appropriate `LocationConstraint`.
3. Mandatory hardening: block public access, enable versioning, and enable AES256 encryption.

💡 This is an important best practice because the state bucket must exist before `terraform init` runs and must always be secured.

**Relevant Configuration Snippet**

```yaml
- name: Ensure Terraform State Bucket Exists
  shell: bash
  run: |
    set -euo pipefail
    bucket="${TF_STATE_BUCKET}"
    region="${TF_STATE_REGION}"
    if aws s3api head-bucket --bucket "${bucket}" --region us-east-1 2>/dev/null; then
      echo "Bucket exists, skipping create."
    else
      if [ "${region}" = "us-east-1" ]; then
        aws s3api create-bucket --bucket "${bucket}" --region "${region}"
      else
        aws s3api create-bucket \
          --bucket "${bucket}" \
          --region "${region}" \
          --create-bucket-configuration LocationConstraint="${region}"
      fi
    fi
    aws s3api put-public-access-block \
      --bucket "${bucket}" \
      --public-access-block-configuration '{
        "BlockPublicAcls": true,
        "IgnorePublicAcls": true,
        "BlockPublicPolicy": true,
        "RestrictPublicBuckets": true
      }'
    aws s3api put-bucket-versioning \
      --bucket "${bucket}" \
      --versioning-configuration Status=Enabled
    aws s3api put-bucket-encryption \
      --bucket "${bucket}" \
      --server-side-encryption-configuration '{
        "Rules": [
          { "ApplyServerSideEncryptionByDefault": { "SSEAlgorithm": "AES256" } }
        ]
      }'
```
