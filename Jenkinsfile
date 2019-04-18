pipeline {
    agent {
    node {
        label 'slave'
        customWorkspace '/home/scott/slave'
    }
}
    stages {
        stage('Build') {
            steps {
                echo 'Done, Everything is okay'
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

