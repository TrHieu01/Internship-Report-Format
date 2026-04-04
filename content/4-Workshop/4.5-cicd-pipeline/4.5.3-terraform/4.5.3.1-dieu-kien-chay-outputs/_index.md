---
title : "Run Conditions & Outputs"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.5.3.1 </b> "
---

#### Objectives

Clarify the trigger conditions for the Terraform Job and the group of outputs published to pass data to downstream jobs.

#### Main Content

The Terraform Job only runs when the `needs` and `if` conditions are met, ensuring that the Packer job has completed with a valid status and the workflow is triggered in the correct context. Upon completion, the job publishes outputs such as ASG name, ECR repository URL, ALB DNS, and backend target group ARN for consistent use in subsequent deployment steps.

**Relevant Configuration Snippet**

```yaml
needs: packer
if: always() && (needs.packer.result == 'success' || needs.packer.result == 'skipped') &&
    (github.event_name == 'workflow_dispatch' || github.event.workflow_run.conclusion == 'success')
outputs:
  asg_name: ${{ steps.tf_output.outputs.asg_name }}
  ecr_repository_url: ${{ steps.tf_output.outputs.ecr_repository_url }}
  alb_dns_name: ${{ steps.tf_output.outputs.alb_dns_name }}
  backend_target_group_arn: ${{ steps.tf_output.outputs.backend_target_group_arn }}
```

#### Note

- Bind run conditions using `needs` and `if` to ensure the correct execution order as designed in the pipeline.
- Outputs should only contain data needed for the next job; avoid including values from configuration secrets or sensitive identification information (e.g., access key, secret key, token, password, private key, connection string, API key).
- Name outputs clearly for easy tracking and tracing throughout the workflow.
