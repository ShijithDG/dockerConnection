pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '''-v C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\CheckingDocker:/workspace -w C:\\workspace'''
        }
    }

    stages {
        stage('Build') {
            steps {
                bat 'pip install --no-cache-dir -r requirements.txt'  // Use 'bat' for Windows commands
            }
        }

        stage('Test') {
            steps {
                bat 'python -m unittest discover -s . -p "test_*.py"'  // Use 'bat' for Windows commands
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
