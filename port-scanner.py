import sys
import socket

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid Amount of Arguments. Refer the README for syntax")
    
try:
    for port in range(1, 65536):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close() 
except KeyboardInterrupt:
    print("\n Exiting Program...")
    sys.exit()
except socket.gaierror:
    print("Host anme cannot be resolved")
    sys.exit()
except socket.error:
    print("Couldnt connect to server")
    sys.exit()