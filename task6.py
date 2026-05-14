import hashlib

# Original password
original_password = "Mayil@1234"

# Create original hash
original_hash = hashlib.sha256(original_password.encode()).hexdigest()

# User login password
login_password = input("Enter Password: ")

# Create login hash
login_hash = hashlib.sha256(login_password.encode()).hexdigest()

# Compare hashes
if original_hash == login_hash:
    print("Hashes Match")
    print("Password Correct")
else:
    print("Hashes Do Not Match")
    print("Wrong Password")
