// Корохова Полина 107В1

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Set up Python') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest lab11_2.py --junitxml=report.xml'
            }
        }

        stage('Archive Test Report') {
            steps {
                archiveArtifacts artifacts: 'report.xml', fingerprint: true
            }
        }
    }
}
