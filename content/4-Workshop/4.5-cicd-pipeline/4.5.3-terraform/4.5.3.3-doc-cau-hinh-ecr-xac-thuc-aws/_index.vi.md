---
title : "Đọc cấu hình ECR & Xác thực AWS"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 4.5.3.3 </b> "
---

#### Mục tiêu

Làm rõ cách đọc cấu hình ECR để phục vụ logic build image và cách xác thực AWS nhằm bảo đảm job có đủ quyền thao tác hạ tầng theo nguyên tắc truy cập tối thiểu.

#### Nội dung chính

1. Read ECR tag immutability bằng awk để lấy giá trị ecr_tag_immutable. Trong pipeline hiện tại, tag được cấu hình ở chế độ **mutable** để cho phép ghi đè tag trong quá trình build/deploy.
2. Configure AWS credentials bằng action chính thức của AWS.

💡 Chế độ **mutable** phù hợp khi dùng tag như latest hoặc tag theo nhánh, giúp pipeline cập nhật nhanh phiên bản image mà không cần đổi tag liên tục. Đổi lại, khả năng truy vết theo tag sẽ kém chặt chẽ hơn so với **immutable**, vì một tag có thể trỏ tới nhiều image khác nhau theo thời gian.

**Trích đoạn cấu hình liên quan**

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

**Giải thích**

- Khối **Read ECR tag immutability** đọc file terraform.tfvars, trích giá trị ecr_tag_immutable bằng awk, chuẩn hoá về true/false và ghi ra $GITHUB_OUTPUT để job sau dùng.
- Khối **Configure AWS credentials** nạp quyền truy cập từ GitHub Secrets để các bước tiếp theo có thể gọi AWS API.
