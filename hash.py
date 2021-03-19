# import sha256
from hashlib import sha256

# text to hash
text = "Welcome to fardellaCoin"
hash_result = sha256(text.encode())

# print result
print(hash_result.hexdigest())
