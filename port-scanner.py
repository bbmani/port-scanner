# Manipulate Runtine
import sys

# Node to Node Connection
import socket

# Regular Expression
import re

# Threading
from concurrent.futures import ThreadPoolExecutor

# Datetime
from datetime import datetime

# Floor function
import math

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

def port_scanner(target, port):
    '''
        @input: Target IP address
        @output: None
        @return: Return true if the port is open
    '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result==0: return True
        s.close()
    except:
        # If there was a hostname resolution error or server connection error, this one statement will be able to handle it. 
        return False

def executor(host, ports):
    '''
        @input: Target, Ports [ List ]
        @output: Ports that are open
        Using ThreadPoolExecutor Function to Run Faster
    '''
    print(f"Scanning Target : {host}")
    
    start_time = datetime.now()
    with ThreadPoolExecutor(len(ports)) as e:
        res = e.map(port_scanner, [host]*len(ports), ports)
        for port, isOpen in enumerate(res):
            if isOpen:
                print(f"Port {port+1} is Open")
    end_time = datetime.now()
    
    print(f"Total Time : {math.floor((end_time - start_time).total_seconds())}")
    

# MAIN FUNCTION
def main():
    target, ports = get_target(), range(1, 65536)
    executor(target, ports)
        
if __name__ == "__main__" : 
    main()