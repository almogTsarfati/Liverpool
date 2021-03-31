pipeline {
    agent any

        stages {
            stage('build') {
                node("node1") {
                    // echo "build ${env.BUILD_ID}"
                    sh "docker build -t almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
                    // build new docker img from docker file 
                }
            }
            stage('stg') {
                node("node1") {
                    sh "docker run --name test -p 5000:5000 -dit almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
                    sh "curl localhost:5000"
                    // deploy on staging namespace
                    // run tests
                }
            }
            stage('deploy') {
                node("node1") {
                    echo 'Hello deploy'
                    // deploy on prod namespace
                }
            }
        }
}
