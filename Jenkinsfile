pipeline {
    agent any

    stages {
        stage('build') {
            steps {
                echo "build ${env.BUILD_ID}"
                // sh "docker build -t almogtsarfati/liverpool:v${env.BUILD_ID}"
                // build new docker img from docker file 
            }
        }
        stage('stg') {
            steps {
                echo 'Hello stg'
                sh 'ls -l'
                // deploy on staging namespace
                // run tests
            }
        }
        stage('deploy') {
            steps {
                echo 'Hello deploy'
                // deploy on prod namespace
            }
        }
    }
}
