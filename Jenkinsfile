pipeline {
    agent {
    node {
        label 'my-defined-label'
        customWorkspace '/some/other/path'
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
