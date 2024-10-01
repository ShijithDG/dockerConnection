pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-v C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\CheckingDocker:/app -w /app'
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
                bat 'python -m unittest discover -s . -p "test_*.py"'
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
