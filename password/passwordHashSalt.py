"""Password key/hash example."""

import hashlib
import binascii

password = "QwE"
salt = "Saltet til Ola"

derived_key = hashlib.pbkdf2_hmac("sha1", password.encode(), salt.encode(), 2048)
print("Password key/hash: " + binascii.hexlify(derived_key).decode())
