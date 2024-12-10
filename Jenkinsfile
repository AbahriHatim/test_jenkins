pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                git branch: 'main', url: 'https://github.com/AbahriHatim/test_jenkins.git'
            }
        }

        stage('Test') {
            matrix {
                axes {
                    axis {
                        name 'PYTHON_VERSION'
                        values '3.8', '3.9', '3.10', '3.11'
                    }
                }
                stages {
                    stage('Set up Python') {
                        steps {
                            script {
                                // Use Docker to set up Python environment
                                sh """
                                docker run --rm -v \$(pwd):/app -w /app python:${PYTHON_VERSION} bash -c "
                                    python -m pip install --upgrade pip &&
                                    pip install fastapi uvicorn pytest httpx
                                "
                                """
                            }
                        }
                    }

                    stage('Run Tests') {
                        steps {
                            script {
                                // Run tests inside the Docker container
                                sh """
                                docker run --rm -v \$(pwd):/app -w /app python:${PYTHON_VERSION} bash -c "pytest"
                                """
                            }
                        }
                    }
                }
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
