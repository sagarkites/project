pipeline {
  agent any
  stages {
   stage('Build') {
    steps {
     echo 'Running Build'
     sudo chmod 777 test.py
     ./test_1.py
   }               
  }
 }
}
