---
title : "Cleanup"
date : 2024-01-01
weight : 8
chapter : false
pre : " <b> 4.8. </b> "
---

#### Cleanup using terraform destroy

1. Navigate to the Terraform directory or run via CI/CD.
2. Execute the command:
```bash
terraform destroy
```
3. Confirm the operation when prompted.

#### Resources to Delete Manually

1. **ACM certificates**: Delete certificates that are no longer in use.
2. **CloudFront/Amplify**: Delete distributions or apps if they still exist.
3. **Logs/Snapshots**: Delete unnecessary log groups and snapshots.

#### Verify Successful Deletion Status

1. Check that the Terraform state contains no resources.
2. Access the AWS Console to confirm that no billable resources remain.
