import socket
import sys
from datetime import datetime

# Define the target
if len(sys.argv) == 2:
    # Translate hostname to IPv4
    target = socket.gethostbyname(sys.argv[1]) 
else:
    print("Invalid amount of arguments.")
    print("Syntax: python port_scanner.py <ip>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print("Scanning target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    # Scan common ports (e.g., 21 FTP, 22 SSH, 80 HTTP, 443 HTTPS)
    # For a quick scan, we will check ports 20 to 100
    for port in range(20, 100):
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout so the script doesn't hang on dropped packets
        socket.setdefaulttimeout(1)
        
        # Connect to the target; returns 0 if successful
        result = s.connect_ex((target, port)) 
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
    
except socket.error:
    print("Could not connect to server.")
    sys.exit()
