pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url:'https://github.com/AbahriHatim/test_jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Use python -m pip to ensure pip is used from the correct Python installation
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    python3 -m pip install -r requirements.txt
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