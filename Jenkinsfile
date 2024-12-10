pipeline {
    agent {
        docker { 
            image 'python:3.9-slim' 
        }
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url:'https://github.com/AbahriHatim/test_jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python3 -m pytest
                '''
            }
        }
    }

    post {
        success {
            echo 'All stages completed successfully!'
        }
        failure {
            echo 'One or more stages failed.'
        }
    }
}