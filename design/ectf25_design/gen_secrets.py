import json
import base64
import os
from cryptography.fernet import Fernet

def generate_secret_key():
    return base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')

def main():
    encryption_key = Fernet.generate_key()
    secrets = {
        "some_secrets": generate_secret_key(),
        "encryption_key": encryption_key.decode('utf-8')
    }
    
    with open("secrets.json", "w") as f:
        json.dump(secrets, f, indent=4)
    
    with open("encryption_key.key", "wb") as f:
        f.write(encryption_key)

if __name__ == "__main__":
    main()
