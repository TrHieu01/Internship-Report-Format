---
title : "Infrastructure Deployment & Output Collection"
date : 2024-01-01
weight : 6
chapter : false
pre : " <b> 4.5.3.6 </b> "
---

#### Objectives

Deploy infrastructure according to Terraform configuration and export outputs for subsequent build/deploy steps in the pipeline.

#### Main Content

1. Execute `terraform apply (-auto-approve -input=false)` to automatically update infrastructure based on IaC configurations in `.tf` files in the Terraform directory; variable values are sourced from `terraform.tfvars`, which is injected from GitHub Secrets. Terraform compares the current state with the desired configuration and creates/modifies/deletes resources based on the differences.

2. Read outputs from Terraform and write to `$GITHUB_OUTPUT` for consistent use by downstream jobs.

💡 `$GITHUB_OUTPUT` is the standard mechanism in GitHub Actions for passing data between jobs, helping link deployment steps without manual variable passing.

**Relevant Configuration Snippet**

```yaml
- name: Terraform Apply
  working-directory: ${{ env.TF_DIR }}
  run: terraform apply -auto-approve -input=false

- name: Get Terraform Outputs
  id: tf_output
  working-directory: ${{ env.TF_DIR }}
  run: |
    echo "asg_name=$(terraform output -raw backend_asg_name)" >> "$GITHUB_OUTPUT"
    echo "aws_region=$(terraform output -raw aws_region)" >> "$GITHUB_OUTPUT"
    echo "ecr_repository_url=$(terraform output -raw ecr_repository_url)" >> "$GITHUB_OUTPUT"
    echo "backend_port=$(terraform output -raw backend_port)" >> "$GITHUB_OUTPUT"
    echo "secrets_kms_key_arn=$(terraform output -raw secrets_kms_key_arn)" >> "$GITHUB_OUTPUT"
    echo "alb_dns_name=$(terraform output -raw alb_dns_name)" >> "$GITHUB_OUTPUT"
    echo "api_domain_name=$(terraform output -raw api_domain_name)" >> "$GITHUB_OUTPUT"
    echo "backend_target_group_arn=$(terraform output -raw backend_target_group_arn)" >> "$GITHUB_OUTPUT"
```
