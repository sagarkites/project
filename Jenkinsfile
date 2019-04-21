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
            agent { 
                label 'slave_1'
            }
            steps {
                sh 'sudo yum install ansible -y'
            }
        }
        stage('Deploy') {
            agent any
            steps {
                echo 'Excess statement'
            }
            post {
                always {
                    echo 'Whatever, i was doing something...!'
                }
                success {
                   echo 'Congrats, Bulid sucess..!'
                }
                failure {
                   echo 'Something went wroung..!'
                }
            }
        }
    }
}

