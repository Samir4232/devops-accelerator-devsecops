pipeline {
    agent any

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

        stage('Build Complete') {
            steps {
                echo 'DevSecOps pipeline completed successfully!'
            }
        }
    }
}
