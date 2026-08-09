pipeline {

    agent any

    triggers {
        cron('H H * * *')
    }

    environment {

        AWS_REGION = "us-east-1"

        ECR_REPOSITORY = "562590527524.dkr.ecr.us-east-1.amazonaws.com/devops-accelerator-file-management-api"

        IMAGE_TAG = "v1"

        SONARQUBE_URL = "http://10.0.0.148:9000"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Code has been checked out from GitHub'
            }
        }


        stage('Gitleaks Secret Scan') {
            steps {
                sh '''
                    gitleaks detect \
                    --source . \
                    --redact \
                    --exit-code 1
                '''
            }
        }


        stage('Terraform Validate') {
            steps {

                dir('infra/terraform') {

                    sh 'terraform init -backend=false'

                    sh 'terraform validate'
                }
            }
        }


        stage('Docker Build') {
            steps {

                sh '''
                    docker build \
                    -t file-management-api:${IMAGE_TAG} \
                    file-management-api
                '''
            }
        }


        stage('Trivy Image Scan') {
            steps {

                sh '''
                    trivy image \
                    --severity HIGH,CRITICAL \
                    --exit-code 0 \
                    --format json \
                    --output trivy-report.json \
                    file-management-api:${IMAGE_TAG}
                '''
            }
        }


        stage('Push Image To ECR') {
            steps {

                sh '''

                    aws ecr get-login-password \
                    --region ${AWS_REGION} | \
                    docker login \
                    --username AWS \
                    --password-stdin ${ECR_REPOSITORY}


                    docker tag \
                    file-management-api:${IMAGE_TAG} \
                    ${ECR_REPOSITORY}:${IMAGE_TAG}


                    docker push \
                    ${ECR_REPOSITORY}:${IMAGE_TAG}

                '''
            }
        }


        stage('Deploy to Kubernetes') {
            steps {

                sh '''

                    aws eks update-kubeconfig \
                    --region ${AWS_REGION} \
                    --name devops-accelerator-cluster


                    kubectl apply -f k8s/


                    kubectl rollout status \
                    deployment/file-management-api

                '''
            }
        }


        stage('OWASP Dependency Check') {
            steps {

                sh '''

                    rm -rf dependency-check-report

                    dependency-check \
                    --project DevOps-Accelerator \
                    --scan file-management-api \
                    --format HTML \
                    --out dependency-check-report

                '''
            }
        }


        stage('SonarQube Analysis') {
            steps {

                withSonarQubeEnv('SonarQube') {

                    sh '''
                        sonar-scanner \
                        -Dsonar.projectKey=devops-accelerator \
                        -Dsonar.projectName=devops-accelerator \
                        -Dsonar.sources=.
                    '''
                }
            }
        }


        stage('Checkov IaC Scan') {
            steps {

                sh '''

                    /var/lib/jenkins/checkov-venv/bin/checkov \
                    -d infra/terraform \
                    -o json \
                    > checkov-report.json || true

                '''
            }
        }


        stage('OWASP ZAP DAST Scan') {
            steps {

                sh '''

                    rm -f zap-report.html

                    docker run --rm \
                    --user root \
                    -v $(pwd):/zap/wrk/:rw \
                    zaproxy/zap-stable \
                    zap-baseline.py \
                    -t http://10.0.0.148:8001 \
                    -r zap-report.html \
                    -I

                '''
            }
        }


        stage('Generate Security Summary') {
            steps {

                sh '''
cat > security-summary.html <<HTMLREPORT

<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>DevSecOps Security Report</title>

<style>

body {
    font-family: Arial, Helvetica, sans-serif;
    background: #f4f6f8;
    margin: 0;
    padding: 40px;
}

.container {
    max-width: 1000px;
    margin: auto;
    background: white;
    padding: 35px;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h1 {
    color: #1f2937;
    margin-bottom: 5px;
}

.subtitle {
    color: #6b7280;
    margin-bottom: 30px;
}

.info {
    background: #f8fafc;
    padding: 15px;
    border-radius: 6px;
    margin-bottom: 25px;
}

table {
    width: 100%;
    border-collapse: collapse;
}

th {
    background: #1f2937;
    color: white;
    padding: 14px;
    text-align: left;
}

td {
    padding: 14px;
    border-bottom: 1px solid #ddd;
}

tr:hover {
    background: #f9fafb;
}

.status {
    color: #15803d;
    font-weight: bold;
}

a {
    color: #2563eb;
    text-decoration: none;
    font-weight: bold;
}

a:hover {
    text-decoration: underline;
}

.footer {
    margin-top: 30px;
    color: #6b7280;
    font-size: 13px;
}

</style>

</head>


<body>

<div class="container">

<h1>DevSecOps Security Report</h1>

<div class="subtitle">
Daily Security Monitoring Report
</div>


<div class="info">

<strong>Jenkins Build:</strong> #${BUILD_NUMBER}<br>

<strong>Build Date:</strong> $(date -u)<br>

<strong>Project:</strong> DevOps Accelerator

</div>


<table>

<tr>

<th>Security Tool</th>

<th>Status</th>

<th>Report</th>

</tr>


<tr>

<td>Gitleaks Secret Scan</td>

<td class="status">Completed</td>

<td>Secrets scan executed during pipeline</td>

</tr>


<tr>

<td>Trivy Container Scan</td>

<td class="status">Completed</td>

<td>
<a href="trivy-report.json">
View Trivy Report
</a>
</td>

</tr>


<tr>

<td>OWASP Dependency Check</td>

<td class="status">Completed</td>

<td>
<a href="dependency-check-report/dependency-check-report.html">
View Dependency Report
</a>
</td>

</tr>


<tr>

<td>SonarQube</td>

<td class="status">Analysis Completed</td>

<td>
<a href="${SONARQUBE_URL}">
Open SonarQube
</a>
</td>

</tr>


<tr>

<td>Checkov IaC Scan</td>

<td class="status">Completed</td>

<td>
<a href="checkov-report.json">
View Checkov Report
</a>
</td>

</tr>


<tr>

<td>OWASP ZAP DAST</td>

<td class="status">Completed</td>

<td>
<a href="zap-report.html">
View ZAP Report
</a>
</td>

</tr>


</table>


<div class="footer">

Generated automatically by Jenkins DevSecOps Security Pipeline.

</div>


</div>

</body>

</html>

HTMLREPORT
                '''
            }
        }


        stage('Archive Security Reports') {
            steps {

                archiveArtifacts artifacts: '''
                    trivy-report.json,
                    checkov-report.json,
                    zap-report.html,
                    security-summary.html,
                    dependency-check-report/**
                ''',
                allowEmptyArchive: true,
                fingerprint: true

            }
        }


        stage('Build Complete') {
            steps {

                echo 'DevSecOps daily security pipeline completed successfully!'

            }
        }

    }

}
