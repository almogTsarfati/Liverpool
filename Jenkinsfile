pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                echo 'build'
                sh 'ls'
            }
        }
        stage('stg') {
            steps {
                echo 'Hello stg'
                sh 'ls -l'
            }
        }
        stage('deploy') {
            steps {
                echo 'Hello deploy'
                sh 'll'
            }
        }
    }
}
