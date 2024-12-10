pipeline {
    agent any // Use any available agent

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: 'main', url: 'https://github.com/AbahriHatim/test_jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
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
