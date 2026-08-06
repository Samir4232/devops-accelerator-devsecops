pipeline {

    agent any

    environment {

        AWS_REGION = "us-east-1"

        ECR_REPOSITORY = "562590527524.dkr.ecr.us-east-1.amazonaws.com/devops-accelerator-file-management-api"

        IMAGE_TAG = "v1"
    }


    stages {


        stage('Checkout') {

            steps {

                echo 'Code has been checked out from GitHub'

            }
        }


        stage('Gitleaks Secret Scan') {

            steps {

                sh 'gitleaks detect --source . --redact --exit-code 1'

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


        kubectl rollout status deployment/file-management-api

        '''

    }
}


stage('OWASP Dependency Check') {

    steps {

        sh '''

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
        --soft-fail
        '''
    }
}



        stage('Build Complete') {

            steps {

                echo 'DevSecOps pipeline completed successfully!'

            }
        }

    }
}
