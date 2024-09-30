pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-v C:/ProgramData/Jenkins/.jenkins/workspace/CheckingDocker:/app -w /app'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh 'pip install --no-cache-dir -r requirements.txt' // Use 'sh' for Unix commands
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest discover -s . -p "test_*.py"' // Use 'sh' for Unix commands
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
