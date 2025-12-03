import hashlib
import secrets

class AuthManager:
    def hash_secret(self, secret: str) -> str:
        salt = secrets.token_hex(16)
        hashed = hashlib.sha256((salt + secret).encode()).hexdigest()
        return f"{salt}:{hashed}"
