---
title : "Custom Domain & HTTPS"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 4.7.3 </b> "
---

#### Two approaches

1. **Use existing ARN**: provide ACM certificate ARN.
2. **Terraform-managed**: create ACM + Route53.

#### Notes

+ Point DNS to Amplify/CloudFront.
+ Wait for certificate issuance before enabling HTTPS.
