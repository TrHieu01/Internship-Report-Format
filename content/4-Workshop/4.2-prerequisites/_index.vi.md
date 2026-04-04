---
title : "Chuẩn bị"
date : 2024-01-01 
weight : 2
chapter : false
pre : " <b> 4.2. </b> "
---

#### Công cụ cần cài

+ Terraform 1.14.6
+ Python 3.11
+ Node.js
+ uv
+ Docker

#### Vì sao cần các công cụ này

+ **Terraform 1.14.6**: quản lý hạ tầng AWS bằng code.
+ **Python 3.11**: chạy backend services và script hỗ trợ.
+ **Node.js**: build và chạy frontend.
+ **uv**: quản lý môi trường và dependencies Python nhanh.
+ **Docker**: build image và chạy service nhất quán.

#### Cài đặt các gói cần thiết để sử dụng (Windows)

1. **Cài Chocolatey (nếu chưa có)**
```
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```
2. **Cài Docker Desktop**
```
choco install docker-desktop -y
```
3. **Cài Node.js (LTS)**
```
choco install nodejs-lts -y
```
4. **Cài Python 3.11**
```
choco install python --version=3.11.9 -y
```
5. **Cài uv**
```
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
6. **Cài Terraform 1.14.6**
```
choco install terraform --version=1.14.6 -y
```

