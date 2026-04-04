---
title : "Job Packer"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.5.2 </b> "
---

#### Tasks Included in Job Packer

**Trigger**

- Manual execution via workflow_dispatch (when necessary).
- Automatically runs when the previous workflow completes successfully (workflow_run = success).

**Main Task Groups**

1. **Environment Preparation**
   - Checkout source code and set up Packer.
   - Configure AWS credentials to create temporary build resources.

2. **Initialization and Build Condition Check**
   - Packer init in the configuration directory.
   - Calculate template hash and check if the AMI already exists to avoid rebuilding.

3. **Create Temporary VPC for Packer**
   - Create a VPC, Internet Gateway, Subnet, and Route for the build process.

4. **Clean up Old AMI and Build New AMI**
   - Deregister old AMIs with the same name and delete associated snapshots.
   - Build the new AMI and attach a hash for configuration tracking.

5. **Cleanup after Build**
   - Delete temporary network infrastructure in reverse order.

**Workflow Flow**

- Job is triggered via workflow_dispatch or workflow_run (success).
- Set up Packer and AWS credentials to gain permission for temporary resource creation.
- Packer init, compute configuration hash; if the corresponding AMI exists and build is not forced, stop.
- Create temporary network (VPC, IGW, Subnet, Route) to build the AMI.
- Deregister old AMI with same name, delete snapshot, then build new AMI with hash tag.
- Clean up all temporary network resources after the build.

#### Role

Standardizes the backend runtime environment and ensures consistent deployment images between builds.
