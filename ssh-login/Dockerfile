FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir paramiko

COPY login.py .

CMD ["python", "-u", "login.py"]