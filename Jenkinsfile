pipeline {
    agent any

    stages {
        stage('Install Python') {
            steps {
                sh '''
                    sudo -E apt-get update
                    sudo -E apt-get install -y python3 python3-pip python3-venv
                '''
            }
        }

        stage('Checkout') {
            steps {
                git branch: 'main', url:'https://github.com/AbahriHatim/test_jenkins.git'
            }
        }

        stage('Install Dependencies') {
            steps {
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