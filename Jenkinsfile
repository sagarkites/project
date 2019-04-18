pipeline {
    agent {
    node {
        label 'slave_1'
        customWorkspace '/home/scott/slave'
    }
    node {
        label 'slave_2'
        customWorkspace '/home/scott/slave_2'
    }    
}
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
