pipeline {
    agent none
      parameters {
            choice(name: 'choice', choices:"slave_1\nslave_2", description: "" )
    }
    stages {
        stage('Build') {
            agent {
                label 'slave_1'
            }
            steps {
                script {
                    if ("${params.choice}" == "slave_1") {
                        echo 'Building..'
                        sh '''
                            sudo yum install epel-release -y
                            sudo yum install python-pip -y 
                            sudo pip install flask
                            sudo yum remove ansible -y 
                           '''
                    }
                }
                
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
