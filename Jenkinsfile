node("node1"){

    checkout scm

    stage('build') {
        echo "build ${env.NODE_NAME}!"
        sh 'ls -l'
        sh "docker build -t almogtsarfati/liverpoolimg:v${env.BUILD_ID} ."
        withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'PASSWORD', usernameVariable: 'USERNAME')]) {
            sh "docker login --username ${USERNAME} --password ${PASSWORD}"
            sh "docker push almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
        }
    }
    stage('stg') {
        sh "aws eks update-kubeconfig --name almogo --region eu-central-1"
        sh "kbuectl get pods"
        // sh "docker rm -f test"
        // sh "docker run --name test -p 5000:5000 -dit almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
        // sh "curl localhost:5000"
        // sh "docker tag testimg almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
        // deploy on staging namespace
        // run tests
    }
    stage('deploy') {
        // deploy on prod namespace
    }
}
