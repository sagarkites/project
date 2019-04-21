pipeline {
    agent { label 'slave_1' && 'slave_2' }
     parameters {
        choice(
            choices: ['slave_1' , 'slave_2'],
            description: '',
            name: 'REQUESTED_ACTION')
    }
    stages {
        stage('Build') {
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
