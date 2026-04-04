---
title : "ECR Configuration & AWS Authentication"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 4.5.3.3 </b> "
---

#### Objectives

Clarify how to read ECR configuration for image build logic and how to authenticate with AWS to ensure the job has sufficient permissions for infrastructure operations following the principle of least privilege.

#### Main Content

1. Read ECR tag immutability using `awk` to retrieve the `ecr_tag_immutable` value. In the current pipeline, tags are configured in **mutable** mode to allow overwriting tags during the build/deploy process.
2. Configure AWS credentials using the official AWS action.

💡 **Mutable** mode is suitable when using tags like `latest` or branch-based tags, allowing the pipeline to quickly update image versions without constantly changing tags. In return, traceability by tag becomes less strict compared to **immutable**, as one tag can point to multiple different images over time.

**Relevant Configuration Snippet**

```yaml
- name: Read ECR tag immutability (ecr_tag_immutable)
  id: ecr_vars
  working-directory: ${{ env.TF_DIR }}
  run: |
    set -euo pipefail
    IMMUTABLE=""
    if [ -f terraform.tfvars ]; then
      IMMUTABLE="$(awk -F= '
        $1 ~ /^[[:space:]]*ecr_tag_immutable[[:space:]]*$/ {
          v=$2
          gsub(/^[[:space:]]+|[[:space:]]+$/, "", v)
          gsub(/\"/, "", v)
          print v
          exit
        }' terraform.tfvars || true)"
    fi
    IMMUTABLE="${IMMUTABLE:-true}"
    case "$IMMUTABLE" in
      true|false) ;;
      *) echo "Invalid ecr_tag_immutable value: $IMMUTABLE" >&2; exit 1 ;;
    esac
    echo "ecr_tag_immutable=$IMMUTABLE" >> "$GITHUB_OUTPUT"

- name: Configure AWS credentials
  uses: aws-actions/configure-aws-credentials@v4
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: ${{ env.AWS_DEFAULT_REGION }}
```

**Explanation**

- The **Read ECR tag immutability** block reads the `terraform.tfvars` file, extracts the `ecr_tag_immutable` value using `awk`, standardizes it to `true/false`, and writes it to `$GITHUB_OUTPUT` for use in subsequent jobs.
- The **Configure AWS credentials** block loads access permissions from GitHub Secrets so following steps can invoke AWS APIs.
