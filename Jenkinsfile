pipeline {
  agent any 
   stages{
     stage('Test') {
       steps {
        sh 'pip list' 
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


