pipeline {
    agent none
    stages {
        stage('Build') {
            agent { 
                label 'slave_2'
            }
            steps {
                checkout scm
                echo 'sudo yum install ansible -y' 
                emailext (
                    subject: "Job '${env.JOB_NAME} ${env.BUILD_NUMBER}'",
                    body: """<p>Check console output at <a href="${env.BUILD_URL}">${env.JOB_NAME}</a></p>""",
                    to: "report@code-maven.com",
                    from: "jenkins@code-maven.com")
            }
        }
        stage('Test on Linux') {
            when {
              expression {
                currentBuild.result == currentBuild.result == 'SUCCESS' 
              }
            }
            agent { 
                label 'slave_1'
            }
            steps {
                sh 'sudo yum remove ansible -y'
            }
        }
        stage('Deploy') {
            agent any
            steps {
                echo 'Excess statement'
            }
        }
    }
}

