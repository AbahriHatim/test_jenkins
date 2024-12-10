pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: 'main', url: 'https://github.com/AbahriHatim/test_jenkins.git'
            }
        }

        stage('Set up Python') {
            steps {
                script {
                    // Install Python dependencies
                    sh '''
                    python -m pip install --upgrade pip
                    pip install fastapi uvicorn pytest httpx
                    '''
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh 'pytest'
            }
        }
    }

    post {
        success {
            echo 'All tests passed successfully!'
        }
        failure {
            echo 'One or more tests failed.'
        }
    }
}
