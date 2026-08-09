# DevOps Accelerator: End-to-End Cloud-Native DevSecOps Platform

A fully integrated cloud-native DevOps and DevSecOps platform demonstrating real-world software delivery practices including Infrastructure as Code, CI/CD automation, containerized deployment, serverless architecture, security automation, AI integration, and monitoring.

The project implements an enterprise-style workflow using AWS, Terraform, Jenkins, Docker, Kubernetes, and multiple DevSecOps security tools to automate infrastructure provisioning, application deployment, vulnerability detection, and continuous security monitoring.

---

## 1. Project Overview

The DevOps Accelerator Platform enables users to:

* Upload files securely through a frontend application hosted on AWS.
* Generate temporary secure upload links using API Gateway and AWS Lambda pre-signed URLs.
* Store files securely in Amazon S3.
* Process uploaded files automatically using S3 Events and AWS Lambda.
* Receive upload notifications through Amazon SNS.
* Deploy a containerized FastAPI File Management API using Docker and Amazon EKS.
* Provision AWS infrastructure using Terraform Infrastructure as Code.
* Automate CI/CD workflows using Jenkins.
* Perform continuous security validation using multiple DevSecOps tools.
* Monitor application and infrastructure health using Prometheus, Grafana, and CloudWatch.
* Integrate an AI service using FastAPI, Ollama, and the Gemma LLM.

---

## 2. What Is the DevOps Accelerator Platform?

The DevOps Accelerator Platform is a cloud-native application platform that demonstrates how modern applications can be designed, deployed, secured, and monitored using DevOps and DevSecOps practices.

### Core Components

* Web frontend application
* Serverless file upload workflow
* Secure S3 upload mechanism using pre-signed URLs
* AWS Lambda-based file processing
* FastAPI File Management API
* Docker containerization
* Amazon ECR container registry
* Amazon EKS Kubernetes deployment
* Terraform Infrastructure as Code
* Jenkins CI/CD pipeline
* Automated security scanning
* AI integration using FastAPI + Ollama
* Gemma LLM integration
* Prometheus monitoring
* Grafana dashboards
* AWS CloudWatch monitoring

---

## 3. High-Level Architecture

```text
                         Developer
                             |
                             v
                    GitHub Repository
                             |
                             v
                       Jenkins CI/CD
                             |
              +--------------+--------------+
              |       DevSecOps Pipeline    |
              +--------------+--------------+
                             |
        +--------------------+--------------------+
        |                    |                    |
        v                    v                    v
     Gitleaks          Terraform Validate      Checkov
        |                    |                    |
        +--------------------+--------------------+
                             |
                             v
                       Docker Build
                             |
                             v
                      Trivy Container Scan
                             |
                             v
                        Amazon ECR
                             |
                             v
                         Amazon EKS
                             |
                             v
                  FastAPI File Management API
                             |
              +--------------+--------------+
              |                             |
              v                             v
        File Management API            AI API Server
              |                             |
              v                             v
        Amazon S3                      Ollama Server
              |                             |
              v                             v
       Lambda Processing              Gemma LLM
              |
              v
             SNS
              |
              v
       Email Notification

Additional Security:
- OWASP Dependency-Check
- SonarQube SAST
- OWASP ZAP DAST
- Security Report Generation

Monitoring:
- Prometheus
- Grafana
- Amazon CloudWatch
```

---

## 4. Secure File Upload Workflow

```text
User Browser
     |
     v
Frontend Application
     |
     v
API Gateway
     |
     v
Lambda - Generate Pre-Signed URL
     |
     v
Amazon S3
     |
     v
S3 Object Created Event
     |
     v
Processing Lambda
     |
     v
Amazon SNS
     |
     v
Email Notification
```

### Workflow

1. The user accesses the frontend application.
2. The user selects a JPG, PNG, or PDF file.
3. The frontend requests a temporary upload URL.
4. API Gateway invokes the Lambda function.
5. Lambda generates an S3 pre-signed URL.
6. The frontend uploads the file directly to Amazon S3.
7. S3 generates an object-created event.
8. The processing Lambda validates and processes the uploaded file.
9. Amazon SNS sends an upload notification.

### Security Benefits

* No public S3 write access
* Temporary upload permissions
* Controlled file uploads
* Reduced attack surface
* Direct browser-to-S3 upload

---

## 5. Containerized Application Flow

```text
Developer
    |
    v
GitHub
    |
    v
Jenkins Pipeline
    |
    v
Docker Build
    |
    v
Trivy Security Scan
    |
    v
Amazon ECR
    |
    v
Amazon EKS
    |
    v
FastAPI File Management API
```

---

## 6. Technology Stack

| Category               | Technology             |
| ---------------------- | ---------------------- |
| Cloud Platform         | AWS                    |
| Source Control         | GitHub                 |
| CI/CD                  | Jenkins                |
| Infrastructure as Code | Terraform              |
| Containers             | Docker                 |
| Container Registry     | Amazon ECR             |
| Orchestration          | Amazon EKS             |
| Backend API            | Python FastAPI         |
| Serverless             | AWS Lambda             |
| API Management         | Amazon API Gateway     |
| Storage                | Amazon S3              |
| Notifications          | Amazon SNS             |
| Monitoring             | Prometheus             |
| Visualization          | Grafana                |
| Cloud Monitoring       | Amazon CloudWatch      |
| SAST                   | SonarQube              |
| Secret Detection       | Gitleaks               |
| Dependency Scanning    | OWASP Dependency-Check |
| Container Security     | Trivy                  |
| IaC Security           | Checkov                |
| DAST                   | OWASP ZAP              |
| AI Service             | Ollama                 |
| LLM                    | Gemma                  |

---

## 7. What Is Covered in This DevOps Accelerator Platform?

### 7.1 Infrastructure Automation with Terraform

Infrastructure as Code is implemented using Terraform.

### AWS Resources

* Amazon VPC
* IAM Roles and Policies
* Amazon EKS Cluster
* Amazon ECR Repository
* Amazon S3 Buckets
* AWS Lambda Functions
* Amazon API Gateway
* Amazon SNS Topics

Terraform provides:

* Repeatable infrastructure deployment
* Version-controlled infrastructure
* Automated cloud provisioning
* Consistent infrastructure configuration

---

### 7.2 End-to-End DevSecOps CI/CD Pipeline

A complete Jenkins pipeline is implemented covering source management, security validation, containerization, deployment, and reporting.

### Pipeline Workflow

```text
GitHub
   |
   v
Jenkins
   |
   +--> Gitleaks Secret Scan
   |
   +--> Terraform Validate
   |
   +--> Checkov IaC Scan
   |
   +--> SonarQube Analysis
   |
   +--> OWASP Dependency-Check
   |
   +--> Docker Build
   |
   +--> Trivy Container Scan
   |
   +--> Push Image to Amazon ECR
   |
   +--> Deploy to Amazon EKS
   |
   +--> OWASP ZAP DAST Scan
   |
   +--> Generate Security Reports
```

---

### 7.3 Cloud-Native Application Deployment

The platform uses both serverless and container-based architecture.

#### Serverless Components

* Frontend hosted on Amazon S3
* Amazon API Gateway
* AWS Lambda Functions
* S3 Event Processing
* Amazon SNS Notifications

#### Containerized Component

The File Management API is:

* Developed using FastAPI
* Containerized using Docker
* Stored in Amazon ECR
* Deployed on Amazon EKS
* Managed using Kubernetes manifests

---

### 7.4 Secure File Upload System

The secure file upload system uses:

* Amazon API Gateway
* AWS Lambda
* Amazon S3
* S3 pre-signed URLs

This architecture provides temporary and controlled access to S3 without requiring public write permissions.

---

### 7.5 AI Integration Module

An independent AI service is integrated into the platform.

```text
User Request
     |
     v
FastAPI AI API
     |
     v
Ollama Server
     |
     v
Gemma LLM
     |
     v
AI Response
```

### AI Features

* AI-based responses
* Independent microservice architecture
* FastAPI-based API
* Ollama LLM integration
* Gemma model integration
* Future-ready architecture for RAG implementation

---

### 7.6 Monitoring and Observability

The platform implements monitoring using Prometheus, Grafana, and AWS CloudWatch.

### Kubernetes Monitoring

* Cluster health
* Node metrics
* Pod status
* CPU utilization
* Memory utilization
* Application metrics

### AWS Monitoring

* CloudWatch Logs
* CloudWatch Metrics

### CI/CD Monitoring

* Jenkins build history
* Jenkins reports
* Build artifacts
* Security reports

---

### 7.7 Automated Security Reporting

The Jenkins pipeline generates security reports from multiple security tools.

### Security Reports

* Trivy Container Report
* Checkov IaC Report
* OWASP Dependency-Check Report
* OWASP ZAP DAST Report
* SonarQube Analysis

Security reports can be archived as Jenkins build artifacts for review and auditing.

---

## 8. Project Repository Structure

```text
devops-accelerator-devsecops/
│
├── .github/
│   └── workflows/
│       ├── backend-deploy.yml
│       ├── frontend.yml
│       └── terraform.yml
│
├── backend/
│   └── lambda/
│       ├── generate-presigned-url/
│       │   └── main.py
│       │
│       └── process-uploaded-file/
│           └── main.py
│
├── frontend/
│   └── index.html
│
├── file-management-api/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── __init__.py
│       └── main.py
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── infra/
│   └── terraform/
│       ├── main.tf
│       ├── outputs.tf
│       ├── variables.tf
│       └── .terraform.lock.hcl
│
├── Jenkinsfile
├── zap.yaml
├── .gitignore
└── README.md
```

---

# 9. Project Screenshots

## Screenshot 1

<img src="./screenshots/image1.png" width="800">

## Screenshot 2

<img src="./screenshots/image2.png" width="800">

## Screenshot 3

<img src="./screenshots/image3.png" width="800">

## Screenshot 4

<img src="./screenshots/image4.png" width="800">

## Screenshot 5

<img src="./screenshots/image5.png" width="800">

## Screenshot 6

<img src="./screenshots/image6.png" width="800">

## Screenshot 7

<img src="./screenshots/image7.png" width="800">

## Screenshot 8

<img src="./screenshots/image8.png" width="800">

## Screenshot 9

<img src="./screenshots/image9.png" width="800">

## Screenshot 10

<img src="./screenshots/image10.png" width="800">

## Screenshot 11

<img src="./screenshots/image11.png" width="800">

## Screenshot 12

<img src="./screenshots/image12.png" width="800">

## Screenshot 13

<img src="./screenshots/image13.png" width="800">

## Screenshot 14

<img src="./screenshots/image14.png" width="800">

## Screenshot 15

<img src="./screenshots/image15.png" width="800">

## Screenshot 16

<img src="./screenshots/image16.png" width="800">

---

## 10. Project Highlights

This project demonstrates an end-to-end DevOps and DevSecOps implementation covering:

* Cloud infrastructure automation
* Infrastructure as Code
* CI/CD automation
* Containerization
* Kubernetes deployment
* Serverless architecture
* Secure file uploads
* Automated security testing
* Container vulnerability scanning
* IaC security scanning
* Static application security testing
* Dynamic application security testing
* AI integration
* Monitoring and observability
* Automated security reporting

The platform provides a practical demonstration of how modern cloud-native applications can be **built, secured, deployed, monitored, and continuously improved using DevOps and DevSecOps practices.**
