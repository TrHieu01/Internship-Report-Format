---
title : "Fork & Clone Repo"
date : 2024-01-01
weight : 3
chapter : false
pre : " <b> 4.3. </b> "
---

Repository: https://github.com/AWS-FCJ-Project/EduTrust_origin.git

#### Basic Git Commands

1. **Fork the repository** on GitHub (if you do not have direct push permissions):
   + Open the repo: https://github.com/AWS-FCJ-Project/EduTrust_origin
   + Click the **Fork** button (top right corner).
   + Select your GitHub account to create a copy.
2. **Clone to your local machine**:
```bash
git clone https://github.com/AWS-FCJ-Project/EduTrust_origin.git
```
3. **Navigate to the project directory**:
```bash
cd EduTrust_origin
```
4. **Create a working branch**:
```bash
git checkout -b feature/<branch-name>
```
Example:
```bash
git checkout -b feature/setup-workshop
```
5. **Push the branch to GitHub for the first time**:
```bash
git push -u origin feature/<branch-name>
```
6. **Update with the latest code from main** (before starting work or creating a PR):
```bash
git fetch origin
git rebase origin/main
```
