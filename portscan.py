#importing requiered modules
import sys
import socket
import time
import threading

#banner
print("Port Scanner")
print("By: Kr.Vikash")
print("")
ussage="python3 portsc.py <target> <port start> <port end>"
#checking for the arguments
if(len(sys.argv) != 4):
    print(ussage)
    print("Enter the arugments Manually")
    #asking for the target
    target = input("Enter the target(URL/IP) : ")
    try:
        #resolving the target
        target = socket.gethostbyname(target)
    except socket.gaierror:  
        #could not resolve
        print("Target name invalid")
        sys.exit()
    #asking for the port range
    port_range = input("Enter the port range (ex: 1-100): ")
    #splitting the port range
    low_port = int(port_range.split("-")[0])
    high_port = int(port_range.split("-")[1])
else:
    #getting the target
    target = sys.argv[1]
    try:
        #resolving the target
        target = socket.gethostbyname(target)
    except socket.gaierror:
        #could not resolve
        print("Target name invalid")
        sys.exit()
    #getting the port range
    low_port = int(sys.argv[2])
    high_port = int(sys.argv[3])

#scanning the ports
def scan(port):
    #creating a socket
    s = socket.socket()
    #setting the timeout
    s.settimeout(2) 
    #connecting to the target
    con=s.connect_ex((target, port))
    #printing the open port
    if(not con):
        print(f"Port {port} is open")
    #closing the socket
    s.close()

for port in range(low_port, high_port):
    #creating a thread
    thread = threading.Thread(target=scan, args=(port,))
    
    #starting the thread
    thread.start()
#exiting the program
sys.exit()

#end of the program
