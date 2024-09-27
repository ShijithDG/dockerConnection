pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root -w C:/app' // Use Windows path for working directory
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/ShijithDG/dockerConnection.git'
            }
        }
        
        stage('Build') {
            steps {
                bat 'pip install --no-cache-dir -r requirements.txt' // Use bat for Windows command
            }
        }
        
        stage('Test') {
            steps {
                bat 'python -m unittest discover -s . -p "test_*.py"' // Use bat for Windows command
            }
        }
    }
    
    post {
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
