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
                // checkout scm // Checkout the code from the SCM (Git)
                git url: 'https://github.com/ShijithDG/dockerConnection.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install dependencies listed in requirements.txt
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                // Example command for building your application if needed
                // If no specific build step is needed, you can skip this stage
                echo 'Building application...'
                // Add any build commands here, if applicable
            }
        }
        stage('Test') {
            steps {
                // Run unit tests inside the container
                sh 'python -m unittest test_calculator.py'
            }
        }
        stage('Package') {
            steps {
                // Create an artifact to deploy (if needed)
                sh 'tar -cvf my_app.tar.gz .'
            }
        }
        stage('Deploy to S3') {
            steps {
                // Use AWS credentials to deploy the artifact to S3
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-jenkin-user']]) {
                    sh 'aws s3 cp my_app.tar.gz s3://my-app-bucke --region eu-north-1'
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
