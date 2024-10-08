pipeline {
    agent {
        docker {
            image 'python:3.9-slim' // Specify the Docker image to use
            args '-u root:root'      // Optional: specify user and other Docker run options
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt' // Example command inside the Docker container
            }
        }
        stage('Test') {
            steps {
                sh 'python -m unittest test_calculator.py' // Run tests inside the container
            }
        }
        stage('Deploy to S3') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-jenkin-user']]) {
                    sh 'aws s3 cp your_file.txt s3://my-app-bucke --region eu-north-1'
                }
            }
        }
    }
    post {
        always {
            cleanWs()  // Clean workspace after pipeline execution
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
