pipeline {
    agent {
    node {
        label 'slave'
    }
}

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                      sudo pip install flask
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
