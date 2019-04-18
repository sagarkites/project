pipeline {
    agent {
    node {
        label 'slave'
        customWorkspace '/home/scott/slave'
    }
}
    parameters {
        choice(
            choices: ['slave' , 'silence'],
            description: '',
            name: 'REQUESTED_ACTION')
    }
    stages {
        stage('Build') {
            when {
                // Only say hello if a "greeting" is requested
                expression { params.REQUESTED_ACTION == 'slave' }
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

