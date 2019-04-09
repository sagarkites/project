pipeline {
  agent any
  stages {
   stage('Build') {
    steps {
     echo 'Running Build'
     sudo chmod 777 test.py
     ./test.py
   }               
  }
 }
}
