import sys
import socket
import re
# -------------------------------------------------------------
def is_IPv4(ip_address):
    ipv4 = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
    pattern_ipv4 = re.compile(r'^(' + ipv4 + r'\.){3}' + ipv4 + r'$')
    
    if re.search(pattern=pattern_ipv4, string=ip_address):
        return 1
    else:
        return 0
# -------------------------------------------------------------
def port_scanner(target):
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
    
# -------------------------------------------------------------
def get_target():
    if len(sys.argv) == 2:
        if is_IPv4(sys.argv[1]) :
            return sys.argv[1]
        else:
            print("The IP address structure is not valid")
            sys.exit()
    else:
        print("Invalid Amount of Arguments. Refer the README for syntax")
        sys.exit()
def main():
    
    port_scanner(get_target())
    
if __name__ == "__main__" : 
    main()