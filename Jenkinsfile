pipeline {
    agent none
    stages {
        stage('Node_1') {
            agent { 
                label 'slave_2'
            }
            steps {
                echo 'Building..'
                sh 'sudo yum install epel-release -y'
            }
        }
        stage('Node_2') {
            agent { 
                label 'slave_1'
            }
            steps {
                echo 'Testing..'
                sh 'sudo yum install epel-release -y'
                sh 'sudo yum install python-pip'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
           }
            post {
                always {
                    echo 'Whatever, i was doing something...!'
                }
                success {
                   echo 'Congrats, Bulid sucess..!'
                }
                failure {
                   echo 'Something wnt wroung..!'
                }
            }
         }
     }
