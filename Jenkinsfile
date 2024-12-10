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
         stages {
        stage('Test') {
            steps {
                script {
                    // Set up Python environment and run tests
                    sh '''
                        python3 -m venv venv
                        . venv/bin/activate
                        pip install pytest fastapi
                        pytest test_main.py
                    '''
                }
            }
    }
}
