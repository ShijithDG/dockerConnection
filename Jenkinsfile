pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
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
                bat 'python -m unittest debugg.py '  
            }
        }
    }

    post {
        success {
            echo 'Tests passed!'
            archiveArtifacts artifacts: 'dist/*.tar.gz', fingerprint: true
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
