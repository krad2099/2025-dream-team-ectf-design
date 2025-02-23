import argparse
import struct
import json
from cryptography.fernet import Fernet

class Encoder:
    def __init__(self, secrets: bytes, encryption_key: str):
        secrets = json.loads(secrets)
        encryption_key = encryption_key.encode('utf-8')
        self.cipher = Fernet(encryption_key)
        self.some_secrets = secrets["some_secrets"]


    def encode(self, channel: int, frame: bytes, timestamp: int) -> bytes:
        data = struct.pack("<IQ", channel, timestamp) + frame
        encrypted_frame = self.cipher.encrypt(data)
        return encrypted_frame

def main():
    parser = argparse.ArgumentParser(prog="ectf25_design.encoder")
    parser.add_argument("secrets_file", type=argparse.FileType("rb"), help="Path to the secrets file")
    parser.add_argument("key_file", type=argparse.FileType("rb"), help="Path to the encryption key file")
    parser.add_argument("channel", type=int, help="Channel to encode for")
    parser.add_argument("frame", help="Contents of the frame")
    parser.add_argument("timestamp", type=int, help="64b timestamp to use")
    args = parser.parse_args()

    encoder = Encoder(encryption_key=args.encryption_key, secrets=args.secrets.read())
    print(repr(encoder.encode(args.channel, args.frame.encode(), args.timestamp)))
    #args.secrets_file.read(), args.key_file.read() old Encoder args
if __name__ == "__main__":
    main()
