pipeline {
    agent any

        stages {
            stage('build') {
                steps {
                    node("node1"){
                        echo "build ${env.NODE_NAME}!"
                        sh 'ls -l'
                        sh "docker build -t almogtsarfati/liverpoolimg:v${env.BUILD_ID} ."
                        // sh "docker push almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
                        // build new docker img from docker file 
                    }
                }
            }
            stage('stg') {
                steps {
                    sh "docker run --name test -p 5000:5000 -dit almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
                    sh "curl localhost:5000"
                    // sh "docker tag testimg almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
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
