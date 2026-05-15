import socket

# Target IP / Website
target = input("Enter IP or website: ")

# Scan ports
print(f"\nScanning target: {target}\n")

for port in range(1, 101):   # 1 to 100 ports
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((target, port))

    if result == 0:
        print(f"Port {port} is OPEN")

    s.close()

print("\nScan Completed")
