pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'  
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest debugg.py '  
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
