pipeline {
  agent {
    node {
      label 'Node1'
    }

  }

  stages {
    stage('stage1') {
      steps {
        echo '1st stage'
        sh 'pwd'
        cd projects
      }
    }

    stage('stage2') {
      steps {
        echo '2st stage'
        sh pwd
        python hw.p y
      }
    }

    stage('stage3') {
      steps {
        echo '3st stage'
        sh 'pwd'
        sh 'virtualenv -p /usr/bin/python3.8 envTest'
        sh '''. envTest/bin/activate
        pip install poetry
        deactivate'''
      }
    }
  }
}