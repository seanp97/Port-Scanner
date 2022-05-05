from socket import *
import time
import sys

class PortScanner:

    def __init__(self):

        if len(sys.argv) > 0:

            print("______          _     _____                                 ")
            print("| ___ \        | |   /  ___|                                ")
            print("| |_/ /__  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __ ")
            print("|  __/ _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__|")
            print("| | | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |   ")
            print("\_|  \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|   ")
            print("")


            self.hostip = sys.argv[1]
            self.ScanNetwork(self.hostip)
        else:
            print("Enter valid IP address")
            sys.exit()


    
    def ScanNetwork(self, ipaddr, timeout = 0.1, portlimit = 65535):
        self.startTime = time.time()

        self.t_IP = gethostbyname(ipaddr)
        print(f"Starting scan on host: {self.t_IP}")
        print("")
        
        for i in range(1, 65535):
            self.s = socket(AF_INET, SOCK_STREAM)
            self.s.settimeout(0.01)
            self.conn = self.s.connect_ex((self.t_IP, i))
            if(self.conn == 0):
                print (f"Port {i}: OPEN")
            self.s.close()

        if time.time() - self.startTime >= 60:
            print(f"Time taken {time.time() - self.startTime / 60} minute(s)")
        else:
            print(f"Time taken: {time.time() - self.startTime} seconds")



PortScanner()
