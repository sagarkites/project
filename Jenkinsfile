pipeline {
    agent none
    stages {
        stage('Build') {
            agent { 
                label 'slave_2'
            }
            steps {
                checkout scm
                sudo 'sudo yum install ansible -y'
                 
            }
        }
        stage('Test on Linux') {
            agent { 
                label 'slave_1'
            }
            steps {
                sh 'sudo yum install ansible -y'
            }
            post {
                always {
                    echo 'Whatever, i was doing something...!'
                }
               success {
                 mail(from: "sagarscott@gmail.com", 
                 to: "vidyasagarchintaluri@gmail.com", 
                 subject: "That build failed!", 
                 body: "Nothing to see here")
               }
            }
        }
    }
}
   
