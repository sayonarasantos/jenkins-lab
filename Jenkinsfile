pipeline {
  agent {
    node {
      label 'Node1-ssh'
    }

  }
  stages {
    stage('s1') {
      agent {
        node {
          label 'Node1-ssh'
        }

      }
      steps {
        echo 'Hello World'
        sh 'pwd'
      }
    }

  }
}