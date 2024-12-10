pipeline {
    agent any
    stages {
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
