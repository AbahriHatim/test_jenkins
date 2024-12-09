pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install fastapi pytest uvicorn httpx'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pytest test_main.py --maxfail=1 --disable-warnings'
                }
            }
        }
    }
}
