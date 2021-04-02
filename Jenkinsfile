node("node1"){
    stage('build') {
        echo "build ${env.NODE_NAME}!"
        sh 'ls -l'
        sh "docker build -t almogtsarfati/liverpoolimg:v${env.BUILD_ID} ."
        // sh "docker push almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
        // build new docker img from docker file 
    }
    stage('stg') {
        sh "docker rm -f test"
        sh "docker run --name test -p 5000:5000 -dit almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
        // sh "curl localhost:5000"
        // sh "docker tag testimg almogtsarfati/liverpoolimg:v${env.BUILD_ID}"
        // deploy on staging namespace
        // run tests
    }
    stage('deploy') {
        echo 'Hello deploy'
        // deploy on prod namespace
    }
}