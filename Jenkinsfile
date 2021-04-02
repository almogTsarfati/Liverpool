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
        sh "helm install liverpool liverpool-chart/ --namespace helm-stg-ns --set image=almogtsarfati/liverpoolimg:v${env.BUILD_ID} --set namespace=k8s-stg-ns"
        sh "helm uninstall liverpool --namespace helm-stg-ns"
    }
    stage('deploy') {
        sh "helm install liverpool liverpool-chart/ --namespace helm-prod-ns --set image=almogtsarfati/liverpoolimg:v${env.BUILD_ID} --set namespace=k8s-prod-ns"
    }
}
