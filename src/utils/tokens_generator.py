import secrets
import hashlib
import hmac


class KeyManager:
    @staticmethod
    def generate_api_key():
        return secrets.token_urlsafe(32)

    @staticmethod
    def generate_secret_key():
        return secrets.token_urlsafe(32)

    @staticmethod
    def hash_key(key, salt=None):
        if salt is None:
            salt = secrets.token_bytes(16)

        key_bytes = key.encode('utf-8')
        hashed_key = hashlib.pbkdf2_hmac('sha256', key_bytes, salt, 100000)
        return hashed_key.hex(), salt

    @staticmethod
    def generate_api_key_pair():
        api_key = KeyManager.generate_api_key()
        secret_key = KeyManager.generate_secret_key()

        hashed_secret_key, salt = KeyManager.hash_key(secret_key)
        return api_key, hashed_secret_key, salt

    @staticmethod
    def verify_key(secret_key, hashed_secret_key, salt):
        hashed_key, _ = KeyManager.hash_key(secret_key, salt)
        return hmac.compare_digest(hashed_key, hashed_secret_key)
