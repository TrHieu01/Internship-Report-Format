---
title : "System Checks"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.8.2 </b> "
---

#### Health check commands

+ Check API: `curl -I <backend_url>/health`.
+ Check frontend: open Amplify URL.

#### Local tests

+ Run backend with `.env`.
+ Run frontend with `npm run dev`.

#### Create Cognito user

+ Create a test user in AWS Console.
+ Assign to the correct group.
