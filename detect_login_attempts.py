# Counters
success_count = 0
failed_count = 0

# Read log file
with open("login_logs.txt", "r") as file:
    
    for line in file:
        
        # Remove extra spaces
        line = line.strip()

        # Detect success
        if "Success" in line:
            success_count += 1

        # Detect failed login
        elif "Failed" in line:
            failed_count += 1

# Print results
print("Successful Logins:", success_count)
print("Failed Logins:", failed_count)
