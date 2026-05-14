import hashlib

# User password
password = input("Enter Password: ")

# Convert password to bytes
password_bytes = password.encode()

# SHA256 hash generate
hash_object = hashlib.sha256(password_bytes)

# Hexadecimal hash value
hashed_password = hash_object.hexdigest()

print("SHA256 Hashed Password:")
print(hashed_password)
