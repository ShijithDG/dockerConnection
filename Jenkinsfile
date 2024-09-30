pipeline {
    agent {
        docker {
            image 'python:3.11-slim-buster'
            args '-w /app -v /c/ProgramData/Jenkins/.jenkins/workspace/CheckingDocker:/app'        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest discover -s . -p "test_*.py"'
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
