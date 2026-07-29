pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Code has been checked out from GitHub'
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
                echo 'DevOps Accelerator pipeline completed successfully!'
            }
        }
    }
}
