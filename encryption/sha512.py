import hashlib

hash_object = hashlib.sha512()

message = "This is the message to be encrypted."
hash_object.update(message.encode('utf-8'))
encrypted_message = hash_object.hexdigest()

print(encrypted_message)
