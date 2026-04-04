---
title : "SNS Email Alerts"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.7.2 </b> "
---

#### Objectives

Set up alerts to send emails when a CloudWatch Alarm exceeds a threshold, helping you respond early to incidents.

#### Set up SNS Topic

1. Create an SNS Topic for the alerting system.
2. Register an email address to receive alerts and confirm the subscription.

#### Create CloudWatch Alarm

1. Select the metrics to monitor (ALB 5xx, CPU/Memory, unhealthy instances).
2. Set an appropriate threshold and evaluation period.
3. Attach the alarm to the SNS Topic to send an email when the threshold is exceeded.

#### Verify Operation

1. Simulate conditions to exceed the threshold and trigger the alarm.
2. Confirm the alert email is sent successfully.
3. Check the alert content to ensure it provides enough information for tracing.
