import base64

# Original text
text = input("Enter Text: ")

# Encode
encoded = base64.b64encode(text.encode())

print("Encoded Text:")
print(encoded.decode())

# Decode
decoded = base64.b64decode(encoded)

print("Decoded Text:")
print(decoded.decode())
