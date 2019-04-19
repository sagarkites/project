pipeline {
    agent none
    stages {
        stage('Build') {
        agent { label 'slave_1' && 'slave_2' }
            steps {
                input ('Running os-level operations do you prcees?')
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

