pipeline {
    agent none
    stages {
        stage('Build') {
            agent { 
                label 'slave_2'
            }
            steps {
                checkout scm
                echo 'sudo yum install ansible -y' 
            }
        }
        stage('Test on Linux') {
            when {
              expression {
                currentBuild.result == currentBuild.result == 'SUCCESS' 
              }
            }
            agent { 
                label 'slave_1'
            }
            steps {
                sh 'sudo yum remove ansible -y'
            }
        }
        stage('Deploy') {
            agent any
            steps {
                echo 'Excess statement'
            }
        }
    }
}

