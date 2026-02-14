#!/bin/bash
set -e

if [ -z "${DEMO_PASSWORD:-}" ]; then
  echo "DEMO_PASSWORD is not set" >&2
  exit 1
fi

echo "demo:${DEMO_PASSWORD}" | chpasswd

/usr/sbin/rsyslogd
exec /usr/sbin/sshd -D