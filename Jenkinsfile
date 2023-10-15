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
                sh 'sudo /usr/local/bin/docker login -u $usr -p $pass | echo "Shehryar718."'
              }
                        
            // steps {
            //     sh "sudo /usr/local/bin/docker login -u shehryar718 -p **** | echo '****'"
            // }
        }
        stage('Build and Push Docker Image') {
            steps {
                sh "sudo /usr/local/bin/docker build -t mlops:assignment-1  . | echo '****'"
                sh "sudo /usr/local/bin/docker push shehryar718/mlops:assignment-1 | echo '****'"
            }
        }
    }
}
