import os
import hashlib

# Hash function
def get_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as f:

        while chunk := f.read(4096):
            sha256.update(chunk)

    return sha256.hexdigest()


# User input
folder = input("Enter folder path: ")

hashes = {}

print("\nScanning...\n")

for root, dirs, files in os.walk(folder):

    for file in files:

        file_path = os.path.join(root, file)

        try:
            file_hash = get_hash(file_path)

            if file_hash in hashes:

                print("Duplicate Found:")
                print("Original :", hashes[file_hash])
                print("Duplicate:", file_path)
                print()

            else:
                hashes[file_hash] = file_path

        except:
            print("Cannot read:", file_path)

print("Scan Completed")
