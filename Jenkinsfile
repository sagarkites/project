pipeline {
    agent {
    node {
        label 'sagar_master'
        customWorkspace '/var/lib/jenkins'
    }
}
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
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
post {
        always {
            echo 'Running tasks'
        }

        success {
            echo "SUCCESSFUL"
        }

        failure {
            echo "FAILED"
        }
    }

