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
        post {
            aborted {
                sh '''
                     sudo yum install ansible -y
                   '''
            }
        }
            
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
