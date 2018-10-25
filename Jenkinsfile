pipeline {
  agent any 

options {
  ansiColor('xterm')
}
   stages{
     stage('Test') {
       steps {
        sh 'echo test' 
      }
       steps {
       sh 'uname'
       }

      }
    stage('Build'){
      steps{
        sh'echo building'
      }
    }
    

}


}


