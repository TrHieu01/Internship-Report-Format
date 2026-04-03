---
title : "Job Packer"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.6.2 </b> "
---

#### Job Packer gồm những task

**Trigger**

- Chạy thủ công qua workflow_dispatch (khi cần)
- Tự động chạy khi workflow trước đó kết thúc thành công (workflow_run = success)

**Các nhóm tác vụ chính**

1. **Chuẩn bị môi trường**
   - Checkout mã nguồn và thiết lập Packer
   - Cấu hình AWS credentials để tạo tài nguyên build tạm thời

   **Cấu hình tham chiếu**

   ```yaml
   - name: Checkout code
     uses: actions/checkout@v4
   - name: Setup Packer
     uses: hashicorp/setup-packer@v3
   - name: Configure AWS credentials
     uses: aws-actions/configure-aws-credentials@v4
     with:
       aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
       aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
       aws-region: ap-southeast-1
   ```

2. **Khởi tạo và kiểm tra điều kiện build**
   - Packer init trong thư mục cấu hình
   - Tính hash template, kiểm tra AMI đã tồn tại để tránh build lại

   **Cấu hình tham chiếu**

   ```yaml
   - name: Run Packer Init
     working-directory: .github/packer
     run: packer init .
   - name: Run Packer Build
     working-directory: .github/packer
     run: |
       PACKER_HASH=$(sha256sum base-ami.pkr.hcl | awk '{print $1}')
       EXISTING_AMI=$(aws ec2 describe-images --owners self --filters "Name=tag:PackerHash,Values=$PACKER_HASH" --query "Images[0].ImageId" --output text)
       FORCE_BUILD="${{ github.event.inputs.build_ami }}"
       if [ "$FORCE_BUILD" != "true" ] && [ "$EXISTING_AMI" != "None" ] && [ -n "$EXISTING_AMI" ]; then
         exit 0
       fi
   ```

3. **Tạo VPC tạm cho Packer**
   - Tạo VPC, Internet Gateway, Subnet và Route phục vụ build

   **Cấu hình tham chiếu**

   ```yaml
   - name: Run Packer Build
     working-directory: .github/packer
     run: |
       VPC_ID=$(aws ec2 create-vpc --cidr-block 10.99.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=PackerTempVPC}]' --query Vpc.VpcId --output text)
       IGW_ID=$(aws ec2 create-internet-gateway --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=PackerTempIGW}]' --query InternetGateway.InternetGatewayId --output text)
       aws ec2 attach-internet-gateway --vpc-id "$VPC_ID" --internet-gateway-id "$IGW_ID"
       SUBNET_ID=$(aws ec2 create-subnet --vpc-id "$VPC_ID" --cidr-block 10.99.1.0/24 --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=PackerTempSubnet}]' --query Subnet.SubnetId --output text)
       aws ec2 modify-subnet-attribute --subnet-id "$SUBNET_ID" --map-public-ip-on-launch
       RTB_ID=$(aws ec2 describe-route-tables --filters "Name=vpc-id,Values=$VPC_ID" --query "RouteTables[0].RouteTableId" --output text)
       aws ec2 create-route --route-table-id "$RTB_ID" --destination-cidr-block 0.0.0.0/0 --gateway-id "$IGW_ID" >/dev/null
   ```

4. **Dọn dẹp AMI cũ và build AMI mới**
   - Huỷ đăng ký AMI cũ trùng tên, xoá snapshot liên quan
   - Build AMI mới và gắn hash để truy vết cấu hình

   **Cấu hình tham chiếu**

   ```yaml
   - name: Run Packer Build
     working-directory: .github/packer
     run: |
       OLD_AMIS_JSON=$(aws ec2 describe-images --owners self --filters "Name=tag:Name,Values=EduTrust-Base-AMI" --query "Images[*].[ImageId,BlockDeviceMappings[*].Ebs.SnapshotId]" --output json || echo "[]")
       if [ "$OLD_AMIS_JSON" != "[]" ] && [ -n "$OLD_AMIS_JSON" ]; then
         IMAGE_IDS=$(echo "$OLD_AMIS_JSON" | jq -r '.[][0]')
         for ami_id in $IMAGE_IDS; do aws ec2 deregister-image --image-id "$ami_id" || true; done
         SNAPSHOT_IDS=$(echo "$OLD_AMIS_JSON" | jq -r '.[][1][]')
         for snap_id in $SNAPSHOT_IDS; do aws ec2 delete-snapshot --snapshot-id "$snap_id" || true; done
       fi
       packer build -var "vpc_id=$VPC_ID" -var "subnet_id=$SUBNET_ID" -var "packer_hash=$PACKER_HASH" base-ami.pkr.hcl
   ```

5. **Cleanup sau build**
   - Xoá hạ tầng mạng tạm theo thứ tự ngược

   **Cấu hình tham chiếu**

   ```yaml
   - name: Cleanup Packer Build Network
     if: always() && env.VPC_ID != ''
     run: |
       sleep 10
       aws ec2 delete-subnet --subnet-id "$SUBNET_ID" || true
       aws ec2 detach-internet-gateway --internet-gateway-id "$IGW_ID" --vpc-id "$VPC_ID" || true
       aws ec2 delete-internet-gateway --internet-gateway-id "$IGW_ID" || true
       aws ec2 delete-vpc --vpc-id "$VPC_ID" || true
   ```

**Luồng hoạt động**

- Job kích hoạt theo workflow_dispatch hoặc workflow_run (success).
- Thiết lập Packer và AWS credentials để có quyền tạo tài nguyên tạm.
- Packer init, tính hash cấu hình; nếu AMI tương ứng đã tồn tại và không ép build thì dừng.
- Tạo mạng tạm (VPC, IGW, Subnet, Route) để build AMI.
- Huỷ AMI cũ trùng tên, xoá snapshot, sau đó build AMI mới có tag hash.
- Dọn dẹp toàn bộ tài nguyên mạng tạm sau build.


#### Vai trò

+ Chuẩn hoá môi trường chạy backend và bảo đảm image triển khai nhất quán giữa các lần build.
