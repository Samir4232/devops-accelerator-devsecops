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
                    cat > security-summary.html <<EOF

                    <html>

                    <head>

                    <title>DevSecOps Security Report</title>

                    <style>

                    body {
                        font-family: Arial, sans-serif;
                        margin: 40px;
                    }

                    h1 {
                        color: #333;
                    }

                    table {
                        border-collapse: collapse;
                        width: 100%;
                    }

                    th, td {
                        border: 1px solid #ccc;
                        padding: 12px;
                        text-align: left;
                    }

                    th {
                        background-color: #eee;
                    }

                    </style>

                    </head>

                    <body>

                    <h1>DevSecOps Security Report</h1>

                    <p>
                    Jenkins Build: ${BUILD_NUMBER}
                    </p>

                    <p>
                    Build Date: $(date)
                    </p>

                    <table>

                    <tr>
                        <th>Security Tool</th>
                        <th>Report</th>
                    </tr>

                    <tr>
                        <td>Trivy Container Scan</td>
                        <td>
                            trivy-report.json
                        </td>
                    </tr>

                    <tr>
                        <td>OWASP Dependency Check</td>
                        <td>
                            dependency-check-report
                        </td>
                    </tr>

                    <tr>
                        <td>Checkov IaC Scan</td>
                        <td>
                            checkov-report.json
                        </td>
                    </tr>

                    <tr>
                        <td>OWASP ZAP DAST</td>
                        <td>
                            zap-report.html
                        </td>
                    </tr>

                    <tr>
                        <td>SonarQube</td>
                        <td>
                            <a href="${SONARQUBE_URL}">
                            Open SonarQube
                            </a>
                        </td>
                    </tr>

                    </table>

                    </body>

                    </html>

                    EOF
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
