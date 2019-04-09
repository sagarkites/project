pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                python /var/lib/jenkins/workspace/pipeline/test.py
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
