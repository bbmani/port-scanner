# Manipulate Runtine
import sys

# Node to Node Connection
import socket

# Regular Expression
import re

def is_IPv4(ip_address):
    '''
        @input: IP Address 
        
        @output: Return 1 -> if IP address matches
                 Return 0 -> if IP address doesn't match
        
    '''
    ipv4 = r"(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
    pattern_ipv4 = re.compile(r'^(' + ipv4 + r'\.){3}' + ipv4 + r'$')
    
    if re.search(pattern=pattern_ipv4, string=ip_address):
        return 1
    else:
        return 0

def get_target():
    '''
        @input : None
        
        @output : Print statements if the IP address is invalid or invalid amount of arguments
        
        @return : Return Target if valid IP address, else None
    '''
    if len(sys.argv) == 2:
        if is_IPv4(sys.argv[1]) :
            return sys.argv[1]
        else:
            print("The IP address structure is not valid")
            sys.exit()
    else:
        print("Invalid Amount of Arguments. Refer the README for syntax")
        sys.exit()

def port_scanner(target):
    '''
        @input: Target IP address
        
        @output: Ports open in the Target Machine
    '''
    print(f"---------- Scanning Target : {target} ----------")
    try:
        for port in range(1, 100):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port} is open")
            s.close() 

    except KeyboardInterrupt:
        print("\nExiting Program (Clean Exit).")
        sys.exit()

    except socket.gaierror:
        print("Host name cannot be resolved.")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server.")
        sys.exit()

# MAIN FUNCTION
def main():
    target = get_target()
    port_scanner(target)
        
if __name__ == "__main__" : 
    main()