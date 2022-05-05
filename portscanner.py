from socket import *
import time
import sys

class PortScanner:

    def __init__(self):

        if len(sys.argv) > 0:
            self.hostip = sys.argv[1]
            self.ScanNetwork(self.hostip)
        else:
            print("Enter valid IP address")
            sys.exit()


    
    def ScanNetwork(self, ipaddr, timeout = 0.1, portlimit = 65535):
        self.startTime = time.time()

        self.t_IP = gethostbyname(ipaddr)
        print(f"Starting scan on host: {self.t_IP}")
        
        for i in range(1, 65535):
            self.s = socket(AF_INET, SOCK_STREAM)
            self.s.settimeout(0.15)
            self.conn = self.s.connect_ex((self.t_IP, i))
            if(self.conn == 0):
                print (f"Port {i}: OPEN")
            self.s.close()

        if time.time() - self.startTime >= 60:
            print(f"Time taken {time.time() - self.startTime / 60} minute(s)")
        else:
            print(f"Time taken: {time.time() - self.startTime} seconds")



PortScanner()
