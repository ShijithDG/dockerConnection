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
                git url: 'https://github.com/ShijithDG/dockerConnection.git', branch: 'main'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install dependencies listed in requirements.txt
                sh 'pip install --no-cache-dir -r requirements.txt'
                sh 'apt-get update && apt-get install -y awscli'
            }
        }
        stage('Build') {
            steps {
                echo 'Building application...'
                // Here you might want to create a distribution package or perform other build steps
                // For example, if you had a setup.py for a package, you would run that here.
            }
        }
        stage('Test') {
            steps {
                // Run unit tests inside the container
                sh 'python -m unittest debugg.py'
            }
        }
        stage('Package') {
            steps {
                // Create an artifact to deploy
                sh 'tar -cvf my_app.tar.gz add.py debugg.py requirements.txt' // Include necessary files
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
