---
title : "Custom Domain & HTTPS"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.6.1 </b> "
---

#### Overview

In this section, you set up Route 53 for a domain purchased at a 3rd-party registrar (e.g. Name.com). This enables you to manage DNS records in Route 53 for later steps (including Amplify custom domain & HTTPS in section 4.6.2).

#### Steps

1. Create a Hosted Zone in Route 53 for your domain.

   ![Route 53 hosted zones](create.png)

   *In Route 53 → **Hosted zones**, choose **Create hosted zone**.*

   ![Create hosted zone form](fill-info.png)

   *Enter your domain name, keep **Type = Public hosted zone**, then choose **Create hosted zone**.*

2. Get the Nameservers (NS) from the Hosted Zone.

   ![Hosted zone NS records](ns.png)

   *Open the Hosted Zone and copy the 4 NS values from the **NS** record.*

3. Update Nameservers on your domain registrar (Name.com) to point to Route 53.

   ![Name.com manage nameservers](domain.png)

   *Paste the 4 NS values into **Manage Nameservers** on Name.com and save changes.*

4. Confirm DNS propagation is complete.

   You can verify using Route 53 **Test record** or via terminal:

   ```bash
   nslookup -type=ns <your-domain>
   ```
