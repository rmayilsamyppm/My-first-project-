# Open a log file
log_file = open("sample.log", "r")

# Read contents
content = log_file.read()

print("Log File Content:")
print(content)

# Close file
log_file.close()
