FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        openssh-server \
        rsyslog \
        bash && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd
RUN useradd -m -s /bin/bash demo

COPY sshd_config /etc/ssh/sshd_config
COPY entrypoint.sh /entrypoint.sh

RUN sed -i 's/\r$//' /entrypoint.sh && chmod 755 /entrypoint.sh

CMD ["/bin/bash", "/entrypoint.sh"]