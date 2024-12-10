pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root:root' // Optional: run as root if needed
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm // Use checkout scm for better compatibility
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
                    python -m pytest
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
