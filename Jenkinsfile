pipeline {
    agent {
    node {
        label 'slave_1' && 'slave_2'
    }
}
    stages {
        stage('Build') {
            steps {
                input ('Running os-level operations do you prcees?')
                echo 'Building..'
                sh '''
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

