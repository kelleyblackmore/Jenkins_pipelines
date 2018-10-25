pipeline {
  agent any 
   stages{
     stage('Test') {
       steps {
        sh 'echo test' 
      }
      }
     stage('Build'){
      steps{
        sh'echo building'
      }
    }
    stage('Deploy'){
      steps{
        sh'echo deploy'
      }
    }
    stage('Run app'){
      steps{
        sh'python app.py'
      }
    }
    

}


}


