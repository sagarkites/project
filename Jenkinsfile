pipeline {
    agent none
    stages {
        stage('Build') {
         parallel {
                stage("windows") {
                    agent {
                        label "jenkins_master"
                    }    
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

