pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/AbahriHatim/test_jenkins.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'py -m pip3 install fastapi uvicorn pytest'
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
