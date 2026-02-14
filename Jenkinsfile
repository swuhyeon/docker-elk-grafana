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

    // Jenkins 워크스페이스에 entrypoint.sh가 실제로 있는지 확인
    stage('Debug workspace (ssh-server files)') {
      steps {
        bat '''
          cd /d "%WORKSPACE%"
          echo ==== PWD ====
          cd
          echo ==== List ssh-server directory ====
          dir ssh-server
          echo ==== Find entrypoint in ssh-server ====
          dir ssh-server | findstr /i entrypoint
        '''
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

    // ssh-server 이미지를 단독 빌드하고, 이미지 안에 /entrypoint.sh가 있는지 확인
    stage('Debug docker build (ssh-server entrypoint)') {
      steps {
        bat '''
          cd /d "%WORKSPACE%"
          docker compose build --no-cache ssh-server
          docker run --rm docker-elk-grafana-ssh-server:latest ls -al /entrypoint.sh
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