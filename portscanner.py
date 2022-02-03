from socket import *
import time

class PortScanner:

    def __init__(self):
        self.ScanNetwork()

    
    def ScanNetwork(self):
        self.startTime = time.time()

        self.target = input("Enter the host to be scanned: ")
        self.t_IP = gethostbyname(self.target)
        print (f"Starting scan on host: {self.t_IP}")
        
        for i in range(50, 500):
            self.s = socket(AF_INET, SOCK_STREAM)
            
            self.conn = self.s.connect_ex((self.t_IP, i))
            if(self.conn == 0):
                print (f"Port {i}: OPEN")
            self.s.close()

        print(f"Time taken: {time.time() - self.startTime}s")


PortScanner()
