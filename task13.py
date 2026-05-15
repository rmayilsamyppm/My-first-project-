import os

# User input
path = input("Enter directory path: ")

# Check path exists
if os.path.exists(path):

    print("\nFiles and Folders:\n")

    for item in os.listdir(path):
        print(item)

else:
    print("Directory not found")
