pipeline {
    agent {
    node {
        label 'sagar_master'
        customWorkspace '/var/lib/jenkins'
    }
}
    parameters {
        choice(
            choices: ['sagar_master' , 'silence'],
            description: '',
            name: 'REQUESTED_ACTION')
    }
    stages {
        stage('Build') {
            when {
                // Only say hello if a "greeting" is requested
                expression { params.REQUESTED_ACTION == 'sagar_master' }
            }
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

