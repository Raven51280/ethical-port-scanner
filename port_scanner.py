import socket

# Get the target IP or domain from the user
target = input("Enter target IP address or domain: ")

# Define the port range to scan
port_range = range(1, 1025)

print(f"\n🔍 Starting scan on {target}...\n")

# Loop through each port
for port in port_range:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)  # Set connection timeout
    result = sock.connect_ex((target, port))
    if result == 0:
        print(f"✅ Port {port} is open")
    sock.close()

print("\n✅ Scan completed.")
