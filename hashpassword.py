import hashlib

def hash_password(password):
    hash_f = hashlib.sha256(password.encode())
    return hash_f.hexdigest()