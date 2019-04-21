pipeline {
    agent none
    parameters {
        choice(
            choices: ['slave_1' , 'slave_2'],
            description: '',
            name: 'REQUESTED_ACTION')
    }

    stages {
        stage ('Speak') {
            agent { label 'slave_1' }
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
