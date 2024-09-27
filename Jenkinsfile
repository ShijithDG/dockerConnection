pipeline {
    agent {
        docker {
            image 'python:3.9-slim' // Specify the Python Docker image
            args '-u root' // Run as root if needed
        }
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your Git repository
                git 'https://github.com/ShijithDG/dockerConnection.git'
            }
        }

        stage('Build') {
            steps {
                // Install dependencies (if you have a requirements.txt file)
                sh 'pip install --no-cache-dir -r requirements.txt' // Change if you have requirements
            }
        }
        
        stage('Test') {
            steps {
                // run the test cases here
                sh 'python -m unittest test_addition.py'
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
