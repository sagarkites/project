pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                      sudo yum install epel-release -y
                      sudo yum install python-pip -y
                      sudo pip install flask
                    '''
            }
        }
        stage('Test') {
            steps {
                input('Do you want toproceed ?')
            }
        }    
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
