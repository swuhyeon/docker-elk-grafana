# ELK Stack 및 Grafana 기반 실시간 로그 모니터링 시스템

> Authentication Security Overview

<br>
<img width="600" height="300" alt="Grafana" src="https://github.com/user-attachments/assets/a5dc8c7c-aa8f-4897-98a2-3778a1aae811" />
<br><br>

SSH 인증 로그를 기반으로 ELK 파이프라인을 구성하고, Grafana 대시보드/프로비저닝과 GitHub Webhook 기반 Jenkins 자동화를 포함한 로그 모니터링 시스템입니다.

---



## 1. Features
### 1) Log Pipeline
- Filebeat으로 `ssh-server` 컨테이너에서 생성되는 `auth.log`를 수집합니다.
- Logstash 파이프라인에서 필드 정규화를 수행합니다.
- Elasticsearch에 `ssh-auth-*` 인덱스 패턴으로 저장합니다.

### 2) Grafana Dashboard
- **Auth Events**: `success / failure / unknown` 비율을 그래프로 표현
- **Succeeded Auth Count**: 최근 15분 성공 인증 총합
- **Failed Auth Count**: 최근 15분 실패 인증 총합

### 3) Jenkins
- GitHub push → Webhook → Jenkins Pipeline 자동 실행
- Pipeline에서 `docker compose up -d` 실행으로 컨테이너 자동 기동



## 2. Layout
- Repository Layout은 다음과 같습니다.

```text
docker-elk-grafana/
  filebeat/
    filebeat.yml

  grafana/
    datasource.yml
    dashboards.yml
    authentication-security-overview.json

  logstash/
    pipelines.yml
    ssh-auth.conf

  ssh-login/
    Dockerfile
    login.py

  ssh-server/
    Dockerfile
    entrypoint.sh
    sshd_config

  docker-compose.yml
  Jenkinsfile
  .gitignore
```



## 3. Requirements
- Docker Desktop 설치 및 Docker Engine 실행
- Jenkins 설치
- .env 파일 생성 및 Jenkis 연동

```bash
# .env (예시)
USERS=root,admin,test,demo,user,guest
PASSWORDS=wrongpass,123456,password,mydemo
DEMO_USER=demo
DEMO_PASSWORD=mydemo
```
⚠️ .env 파일은 민감정보가 포함되어 있으므로, 반드시 .gitignore에 포함하세요.



## 4. How to Use
### 1) 컨테이너 기동 및 확인

```bash
docker compose up --build -d
docker ps -a
```

### 2) 접속
- Elasticsearch: `http://localhost:9200`
- Kibana:  `http://localhost:5601`
- Grafana: `http://localhost:3000` (기본: `admin / admin`)

### 3) Jenkins 연동
- Pipeline Job 생성
- SCM GitHub repository 연결
- Jenkinsfile 사용

### 4) GitHub Webhook
- Payload URL: `https://<domain>/github-webhook/`
- Content type: `application/json`
- Event: `Just the push event`

이후 코드를 GitHub에 push 하면 Webhook을 통해 Jenkins 파이프라인이 자동 실행됩니다.
