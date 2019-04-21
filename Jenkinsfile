pipeline {
    agent { label 'slave_1' }
    parameters {
        choice(
            choices: ['slave_1' , 'slave_2'],
            description: '',
            name: 'REQUESTED_ACTION')
    }

    stages {
        stage ('Speak') {
            when {
                // Only say hello if a "greeting" is requested
                expression { params.REQUESTED_ACTION == 'slavegfhsgdhGDHsjgdh' }
            }
            steps {
                sh 'sudo cat /etc/*release'
            }
        }
    }
}
