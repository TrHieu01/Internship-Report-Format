---
title : "Frontend Deployment & Security"
date : 2024-01-01 
weight : 6
chapter : true
pre : " <b> 4.6. </b> "
---

#### Overview

<p style="text-align: justify;">
This section focuses on deploying the frontend on AWS Amplify, configuring user authentication with Cognito, and enabling WAF to protect the edge layer. When a custom domain is attached to Amplify, the system automatically creates DNS records; on the domain provider side, you only need to update the nameservers so that Route 53 manages the DNS and ACM validates TLS. This setup reduces manual steps, limits errors, and ensures HTTPS operation remains stable.
</p>

#### Content

1. [Frontend Deployment with Amplify](4.7.1-setup-amplify-frontend/)
2. [Cognito (User Authentication)](4.7.2-cognito/)
3. [Custom Domain & HTTPS](4.7.3-custom-domain-https/)
4. [WAF Frontend](4.7.4-waf-frontend/)
