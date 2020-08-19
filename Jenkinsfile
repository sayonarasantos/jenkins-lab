pipeline {
  agent {
    node {
      label 'Node1-ssh'
    }

  }
  stages {
    stage('build') {
      steps {
        echo 'Build stage'
        sh 'pwd'
        cd projects
      }
    }

    stage('test') {
      steps {
        echo 'Test stage'
        sh pwd
        python hw.p 
      }
    }

  }
}