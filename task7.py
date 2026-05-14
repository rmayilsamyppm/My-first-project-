# Stored username and password
stored_username = "admin"
stored_password = "Mayil@1234"

# User input
username = input("Enter Username: ")
password = input("Enter Password: ")

# Check login
if username == stored_username and password == stored_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")
