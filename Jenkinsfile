pipeline {
  agent any
  options { timestamps() }

  stages {
    stage('Check Docker') {
      steps {
        bat '''
          docker version
          docker compose version
        '''
      }
    }

    stage('Provision .env (Jenkins Secret file)') {
      steps {
        withCredentials([file(credentialsId: 'docker-elk-grafana-env', variable: 'ENV_FILE')]) {
          bat '''
            cd /d "%WORKSPACE%"
            copy /Y "%ENV_FILE%" ".env" >nul
          '''
        }
      }
    }

    stage('Validate compose') {
      steps {
        bat '''
          cd /d "%WORKSPACE%"
          docker compose config
        '''
      }
    }

    stage('Up (detached)') {
      steps {
        bat '''
          cd /d "%WORKSPACE%"
          docker compose up -d --build
        '''
      }
    }

    stage('Status') {
      steps {
        bat '''
          cd /d "%WORKSPACE%"
          docker compose ps
        '''
      }
    }
  }

  post {
    always {
      bat '''
        del /f /q "%WORKSPACE%\\.env" 2>nul || exit /b 0
      '''
    }
  }
}