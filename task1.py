import platform
import socket

# OS Information
os_name = platform.system()
os_version = platform.version()

# Hostname
hostname = socket.gethostname()

# IP Address
ip_address = socket.gethostbyname(hostname)

# Print Details
print("=== System Information ===")
print("Operating System :", os_name)
print("OS Version       :", os_version)
print("Hostname         :", hostname)
print("IP Address       :", ip_address)
