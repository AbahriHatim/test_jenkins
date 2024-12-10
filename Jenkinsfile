pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies
                    sh 'pip install fastapi uvicorn pytest'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run the tests
                    sh 'pytest test_main.py --maxfail=1 --disable-warnings'
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline finished.'
        }
        success {
            echo 'Tests passed successfully!'
        }
        failure {
            echo 'Tests failed. Please check the logs.'
        }
    }
}
