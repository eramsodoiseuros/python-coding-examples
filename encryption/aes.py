import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Generate a random key
password = b"password"
salt = b"salt"
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000
)
key = base64.urlsafe_b64encode(kdf.derive(password))

# Encrypt the message
fernet = Fernet(key)
message = "This is the message to be encrypted."
encrypted_message = fernet.encrypt(message.encode('utf-8'))

# Decrypt the message
decrypted_message = fernet.decrypt(encrypted_message).decode('utf-8')

print(decrypted_message)
