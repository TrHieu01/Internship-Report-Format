---
title : "Custom Domain & HTTPS"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.6.1 </b> "
---

#### Overview

In this section, you configure a custom domain following the Name.com → Route 53 → ACM → Amplify flow to enable HTTPS and ensure secure access.

Execution Sequence:

1. Set up Route 53 and update nameservers at Name.com.
2. Provision ACM certificates using DNS validation.
3. Attach the domain to Amplify and verify HTTPS.

#### Content

1. [Set up Route 53 for Name.com domain](4.6.1.1-acm-route53-cicd/)
2. [Provision ACM certificate for domain](4.6.1.2-nameserver-domain-provider/)