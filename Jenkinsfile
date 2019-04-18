pipeline {
    agent {
    node {
        label 'jenkins_master'
        customWorkspace '/home/scott/slave'
    }
}
    stages {
        stage('Build') {
            steps {
                sh 'sudo yum install ansible -y'
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

