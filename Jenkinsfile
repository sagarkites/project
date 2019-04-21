pipeline {
    agent none
     parameters {
        choice(
            choices: ['slave_1' , 'slave_2'],
            description: '',
            name: 'REQUESTED_ACTION')
    }
    stages {
        stage('Build') {
            agent {
                label 'slave_1'
            }
            steps {
                echo 'Building..'
                sh '''
                      sudo yum install epel-release -y
                      sudo yum install python-pip -y 
                      sudo pip install flask
                      sudo yum remove ansible -y 
                    '''
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
