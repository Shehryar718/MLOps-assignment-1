pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Logging into Docker hub') {

            withCredentials([string(credentialsId: 'docker-hub-credentials', Username: 'usr', Password: 'pass')]) {
                sh 'sudo /usr/local/bin/docker login -u $usr -p $pass | echo "Shehryar123."'
              }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                sh 'sudo /usr/local/bin/docker build -t mlops:assignment-1  . | echo "Shehryar123."'
                sh 'sudo /usr/local/bin/docker push shehryar718/mlops:assignment-1 | echo "Shehryar123."'
            }
        }
    }
}
