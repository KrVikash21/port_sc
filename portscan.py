#importing requiered modules
import sys
import socket
import time
import threading

#banner
print("Port Scanner")
print("By: Kr.Vikash")
print("")

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
threads = []

for port in range(low_port, high_port):
    #creating a thread
    thread = threading.Thread(target=scan, args=(port,))
    threads.append(thread)
    
    #starting the thread
    thread.start()

#waiting for all threads to complete
for thread in threads:
    thread.join()

#end of the program

