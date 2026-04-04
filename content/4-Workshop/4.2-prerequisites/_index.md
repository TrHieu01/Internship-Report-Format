---
title : "Prerequisites"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 4.2. </b> "
---

#### Tools to Install

+ Terraform 1.14.6
+ Python 3.11
+ Node.js
+ uv
+ Docker

#### Why these tools are needed

+ **Terraform 1.14.6**: Manages AWS infrastructure as code.
+ **Python 3.11**: Runs backend services and support scripts.
+ **Node.js**: Builds and runs the frontend.
+ **uv**: Efficiently manages Python environments and dependencies.
+ **Docker**: Builds images and ensures consistent service execution.

#### Installing Necessary Packages (Windows)

1. **Install Chocolatey (if not already installed)**
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
2. **Install Docker Desktop**
```powershell
choco install docker-desktop -y
```
3. **Install Node.js (LTS)**
```powershell
choco install nodejs-lts -y
```
4. **Install Python 3.11**
```powershell
choco install python --version=3.11.9 -y
```
5. **Install uv**
```powershell
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
6. **Install Terraform 1.14.6**
```powershell
choco install terraform --version=1.14.6 -y
```
