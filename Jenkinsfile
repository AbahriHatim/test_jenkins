pipeline {
    agent {
        docker {
            image 'my-python-app' // Use the Docker image
            args '-v /var/run/docker.sock:/var/run/docker.sock' // Optional: if you need Docker inside Docker
        }
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: 'main', url: 'https://github.com/AbahriHatim/test_jenkins.git'
            }
        }

        stage('Run Tests') {
            steps {
                // Run tests using pytest
                sh 'python -m pytest'
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
