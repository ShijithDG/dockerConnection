pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
            args '-v /c/ProgramData/Jenkins/.jenkins/workspace/CheckingDocker:/workspace'
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
