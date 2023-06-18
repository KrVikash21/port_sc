# port_sc
For scanning the open port of any network 
### Code explanation
1. First we import some modules which we will use in our program.
2. Then we print the banner of our program.
3. Then we check if the user has entered the arguments or not. If not then we ask the user for the target and port range manually.
4. Then we scan the ports using the scan function. Inside the scan function:
    1. We create a socket and set the timeout to 2 seconds.
    2. We connect to the target using the connect_ex() method.
    3. If the port is open then we print that the port is open.
    4. Then we close the socket.
5. Then we create a thread for each port and start the thread.
6. Finally we exit the program.
###
### !!!Alert!!!
    There maybe some Limition on using this port scanner on Virtual machine 
    because of lesser hardware access, so try to scan the prot in the batch of 100 
###
