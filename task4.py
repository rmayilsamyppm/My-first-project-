import secrets

# 16 bytes secure token generate
token = secrets.token_hex(16)
print("Secure Token:")
print(token)
