---
title : "Terraform Environment Preparation"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.5.3.2 </b> "
---

#### Objectives

Set up the Terraform environment according to CI/CD standards to ensure consistency and configuration security.

#### Execution Steps

1. Checkout code.
2. Cache Terraform plugins to optimize runtime.
3. Setup Terraform version 1.14.6.
4. Write `terraform.tfvars` from GitHub Secrets to inject sensitive variables.

💡 Do not commit `terraform.tfvars` to the repository to avoid information leaks. GitHub Secrets is the standard mechanism for injecting sensitive configurations in CI/CD.

**Relevant Configuration Snippet**

```yaml
- name: Checkout code
  uses: actions/checkout@v4

- name: Cache Terraform plugins
  uses: actions/cache@v4
  with:
    path: ~/.terraform.d/plugin-cache
    key: ${{ runner.os }}-terraform-${{ hashFiles('.github/terraform/*.tf') }}
    restore-keys: |
      ${{ runner.os }}-terraform-

- name: Setup Terraform
  uses: hashicorp/setup-terraform@v3
  with:
    terraform_version: "1.14.6"
    terraform_wrapper: false

- name: Write terraform.tfvars from secret
  working-directory: ${{ env.TF_DIR }}
  env:
    TF_PLUGIN_CACHE_DIR: ~/.terraform.d/plugin-cache
  run: printf "%s\n" "$TERRAFORM_VARS" > terraform.tfvars
```
