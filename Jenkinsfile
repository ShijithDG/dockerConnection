pipeline {
    agent {
        docker {
            image 'python:3.11-slim-buster'
            
        }
    }

    stages {
        stage('Build') {
            steps {
                bat 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover -s /app -p "test_*.py"'
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