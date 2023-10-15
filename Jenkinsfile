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
                sh 'sudo /usr/local/bin/docker login -u $usr -p $pass | echo "***"'
              }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                sh 'sudo /usr/local/bin/docker build -t mlops:assignment-1  . | echo "***"'
                sh 'sudo /usr/local/bin/docker push shehryar718/mlops:assignment-1 | echo "***"'
            }
        }
    }
    post {
        failure {
            emailext(
                subject: "Failed: ${currentBuild.fullDisplayName}",
                body: "The build has failed. Please check the console output at ${BUILD_URL} to diagnose the issue.",
                to: 'hafizshehryar88@gmail.com',
            )
        }
        success {
            emailext(
                subject: "Successful: ${currentBuild.fullDisplayName}",
                body: "The build was successful. You can access the artifacts at ${BUILD_URL}",
                to: 'hafizshehryar88@gmail.com',
            )
        }
    }
}
