pipeline {
    agent none
     parameters {
        choice(
            name: 'choice'
            choices: ['slave_1' , 'slave_2'],
            description: 'Parameters')
    }
    stages {
        stage('Build') {
            agent {
                label 'slave_1'
            }
            steps {
                script {
                    if ("${params.Invoke_Parameters}" == "slave_1") {
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
            agent {
                label 'slave_2'
            }
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
