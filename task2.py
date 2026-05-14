import random
import string

# Password length
length = 12

# Characters
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ''.join(random.choice(characters) for i in range(length))

print("Generated Password:", password)
