---
title : "Provision ACM certificate for domain"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.6.1.2 </b> "
---

#### Content

1. Create an ACM Certificate using DNS validation.
2. Note: Amplify uses CloudFront, so the ACM certificate must be located in **us-east-1**.
3. Create the DNS validation record in Route 53.
4. Wait for the certificate status to become **Issued**.
