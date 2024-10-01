pipeline {
    agent {
        docker {
            image 'python:3.11-slim' 
            args '''-v C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\CheckingDocker:C:\\app'''
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
                sh 'python -m black . --check' // Optional: Check code formatting with Black
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest discover tests'
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