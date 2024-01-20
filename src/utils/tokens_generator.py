"""token_generator.py

Keyword arguments:
argument -- description
Return: return_description
"""

import hashlib
import hmac
import secrets


class KeyManager:
    @staticmethod
    def generate_api_key():
        # Generate a random API key
        return secrets.token_urlsafe(16)

    @staticmethod
    def generate_secret_key():
        # Generate a random secret key
        return secrets.token_urlsafe(32)

    @staticmethod
    def hash_key(key, salt=None):
        # Hash the key using PBKDF2 with a random salt
        if salt is None:
            salt = secrets.token_bytes(32)

        key_bytes = key.encode('utf-8')
        hashed_key = hashlib.pbkdf2_hmac('sha256', key_bytes, salt, 100000)
        return hashed_key, salt

    @staticmethod
    def generate_api_key_pair():
        # Generate API key and secret key pair
        api_key = KeyManager.generate_api_key()
        secret_key = KeyManager.generate_secret_key()

        # Hash the secret key and return the pair
        hashed_secret_key, salt = KeyManager.hash_key(secret_key)
        return api_key, hashed_secret_key, salt

    @staticmethod
    def verify_key(api_key, hashed_secret_key, salt):
        # Verify the API key and secret key pair
        # In a real application, this should come from a secure source
        secret_key = input("Enter your secret key: ")

        # Hash the provided secret key with the stored salt
        hashed_key, _ = KeyManager.hash_key(secret_key, salt)

        # Compare the hashed secret keys
        return hmac.compare_digest(hashed_key, hashed_secret_key)


# # Example usage:
# api_key, hashed_secret_key, salt = KeyManager.generate_api_key_pair()

# # Store the hashed_secret_key, salt, 
# and api_key securely (e.g., in a database)

# # Later, when verifying a key:
# is_valid = KeyManager.verify_key(api_key, hashed_secret_key, salt)

# if is_valid:
#     print("Key is valid!")
# else:
#     print("Key is not valid!")
