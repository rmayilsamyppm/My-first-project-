import hashlib

# File hash function
def calculate_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:

        while True:
            data = f.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


# User input
file_name = input("Enter file name: ")

# Calculate hash
file_hash = calculate_hash(file_name)

print("\nSHA256 Hash:")
print(file_hash)
