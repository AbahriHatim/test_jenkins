pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://your-repo-url.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip3 install fastapi uvicorn pytest'
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
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
