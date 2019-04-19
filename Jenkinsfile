pipeline {
    agent none
    stages {
        stage('Build') {
            agent { 
                label 'slave_1'
            }
            steps {
                input ('Running os-level operations do you prcees?')
                echo 'Building..'
                sh '''
                      sudo yum remove ansible -y 
                    '''
            }
        }
        stage('Test on Linux') {
            agent { 
                label 'slave_2'
            }
            steps {
                sh 'sudo yum install ansible -y'
            }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

