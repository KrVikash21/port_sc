#importing requiered modules
import os
import sys
import socket

#clearing the screen
os.system("clear")

#banner
print("Port Scanner")
print("By: Kr.Vikash")
print("")

#asking for the target
target = input("Enter the target IP: ")

#asking for the port range
port_range = input("Enter the port range (ex: 1-100): ")

#splitting the port range
low_port = int(port_range.split("-")[0])
high_port = int(port_range.split("-")[1])

#scanning the ports
for port in range(low_port, high_port):
    try:
        #creating a socket
        s = socket.socket()

        #connecting to the target
        s.connect((target, port))

        #printing the open port
        print(f"Port {port} is open")

        #closing the socket
        s.close()

    except:
        #printing the closed port
        print(f"Port {port} is closed")

#exiting the program
sys.exit()

#end of the program
