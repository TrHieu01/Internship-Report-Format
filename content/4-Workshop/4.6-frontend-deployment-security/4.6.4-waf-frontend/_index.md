---
title : "WAF Frontend"
date : 2024-01-01
weight : 4
chapter : false
pre : " <b> 4.6.4 </b> "
---

#### Objectives

Protect the frontend layer (CloudFront) using WAF.

#### Deployment Steps

1. Create a Web ACL on AWS WAF.
2. Select the CloudFront scope and add basic managed rule groups.
3. Attach the Web ACL to the Amplify CloudFront distribution.

#### Verify Rule Operation

1. Try applying a rate limit or IP block to confirm the rule is effective.
2. Monitor logs/metrics in CloudWatch to evaluate false positives.

1. Go to AWS WAF, create Web ACL.
2. Select CloudFront scope and add managed rule groups.
3. Open the Amplify CloudFront Distribution.
4. Select the newly created Web ACL in the WAF section.
5. Save the configuration and wait for the update to complete.

#### Note

1. Prioritize enabling monitor mode before switching to block.
