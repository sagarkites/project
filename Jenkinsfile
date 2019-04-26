pipeline {
    agent none
    stages {
        stage('Build') {
            agent any
            steps {
                checkout scm
                echo 'sudo yum install ansible -y'     
            }
        }
        stage('Test on Linux') {
            agent any
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
                    emailext (
                        subject: "Jenkins Build status",
                        body: "Build job",
                        to: "vidyasagarchintaluri@gmail.com",
                        from: "sagarscott@gmail.com"
                             )
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
