// 



pipeline {
    agent {
        docker {
            image 'python:3.11-slim'
        }
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                    # Install AWS CLI
                    apt-get update && apt-get install -y awscli
                    
                    # Install Python dependencies
                    pip install --no-cache-dir -r requirements.txt
                    
                    # Build the package
                    python setup.py sdist
                '''
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest discover -s tests'
            }
        }

        stage('Deploy to S3 (Optional)') {
            steps {
                withCredentials([
                    [$class: 'AmazonS3CredentialsBinding',
                    credentialsId: 'aws-jenkin-user',
                    accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                    secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']
                ]) {
                    script {
                        // Replace with your actual package name
                        sh 'aws s3 cp dist/simple_calculator-1.0.tar.gz s3://my-app-bucke/simple_calculator-1.0.tar.gz'
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Tests passed and deployment successful!'
        }
        failure {
            echo 'Tests failed or deployment failed!'
        }
    }
}
