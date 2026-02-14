FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openssh-server \
        rsyslog && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd

RUN useradd -m -s /bin/bash demo

COPY sshd_config /etc/ssh/sshd_config
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]