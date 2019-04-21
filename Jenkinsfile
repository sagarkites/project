pipeline {
    agent none
    
    stages {
        stage ('Speak') {
            agent { label 'slave_1' }
            parameters {
            choice(
                choices: ['slave_1' , 'slave_2'],
                description: '',
                name: 'REQUESTED_ACTION')
                       }

            when {
                // Only say hello if a "greeting" is requested
                expression { params.REQUESTED_ACTION == 'slave_1' }
            }
            steps {
                echo "Hello, bitwiseman!"
            }
        }
    }
}
