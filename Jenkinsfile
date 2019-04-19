pipeline {
    agent none
    stages {
        stage('Build') {
            agent { 
                label 'slave_2'
            }
            steps {
                checkout scm
                sh 'sudo yum install ansible -y'
                 
            }
        }
        stage('Test on Linux') {
            agent { 
                label 'slave_1'
            }
            steps {
                sh 'sudo yum install ansible -y'
            }
            
                }
            }
        }
   
