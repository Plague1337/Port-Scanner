#!/bin/python3
#Written by Pl4gue
import socket
import sys
from datetime import datetime

#Defining our target/syntax
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #$1 same in bash #Translating hostname to IPv4
else:
    print("Invalid amount of arguments.")
    print("Syntax : python3 port_scanner.py <ip>")

##Banner
print("#" * 50)
print("Scanning Target: " + target)
print("Time Started: " +str(datetime.now()))
print("#" * 50)


try:
        for port in range(1,65535): #from 50 to 85 port range
            s=socket.socket(socket.AF_INET, socket.SOCK_STREAM) #establish a connection of IPV4
            socket.setdefaulttimeout(1) #Default time out 1 sec
            result = s.connect_ex((target,port)) #returns an error indicator, storing in var result
            print("Checking port {}" .format(port))
            if result == 0:
                    print("Port {} is open".format(port))
            s.close()


except KeyboardInterrupt: #if the program is Controlled'd C
        print("\nExiting Program")
        sys.exit

except socket.gaierror: #if there is no HOSTNAME Resolution
        print("Hostname could not be resolved")
        sys.exit()

except socket.error: #cannot connect to IP
        print("Couldn't connect to the server")
        sys.exit()
