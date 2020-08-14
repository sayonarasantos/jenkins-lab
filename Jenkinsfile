pipeline {
  agent {
    node {
      label 'Node1-ssh'
    }

  }
  stages {
    stage('s1') {
      steps {
        echo 'Hello World'
        sh 'pwd'
      }
    }

  }
}