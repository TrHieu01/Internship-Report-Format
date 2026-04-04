---
title : "CloudWatch Logs Monitoring"
date : 2024-01-01
weight : 1
chapter : false
pre : " <b> 4.7.1 </b> "
---

#### Overview

CloudWatch is used to collect and monitor system logs, helping to detect errors and track operational trends over time.

#### Logs to Monitor

1. **Application logs**: requests, errors, API latency.
2. **ALB logs**: 4xx/5xx errors and latency.
3. **System metrics**: CPU, memory, disk (via CloudWatch Agent).

#### Why Monitor?

1. **Application logs**: To detect business logic errors, API failures, and bottlenecks.
2. **ALB logs**: To track access quality and user-side error rates.
3. **System metrics**: To provide early warnings when resource overloads might cause downtime.

#### Note

Setting up alarms and SNS will be covered in detail in section 4.7.2.
