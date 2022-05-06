from socket import *
import time
import sys
from pathlib import Path

class PortScanner:

    def __init__(self):

        if len(sys.argv) > 0:

            print(" ______          _     _____                                  ")
            print(" | ___ \        | |   /  ___|                                 ")
            print(" | |_/ /__  _ __| |_  \ `--.  ___ __ _ _ __  _ __   ___ _ __  ")
            print(" |  __/ _ \| '__| __|  `--. \/ __/ _` | '_ \| '_ \ / _ \ '__| ")
            print(" | | | (_) | |  | |_  /\__/ / (_| (_| | | | | | | |  __/ |    ")
            print(" \_|  \___/|_|   \__| \____/ \___\__,_|_| |_|_| |_|\___|_|    ")
            print(" ")


            self.hostip = sys.argv[1]
            self.ScanNetwork(self.hostip)
        else:
            print(" Enter valid IP address ")
            sys.exit()


    
    def ScanNetwork(self, ipaddr):
        try:
            self.startTime = time.time()

            self.t_IP = gethostbyname(ipaddr)
            print(f" Starting scan on host: {self.t_IP} ")
            print("")

            self.outputArr = []
            
            for i in range(0, 65535):
                self.s = socket(AF_INET, SOCK_STREAM)
                self.s.settimeout(0.01)
                self.conn = self.s.connect_ex((self.t_IP, i))
                if(self.conn == 0):
                    print (f" Port {i}: OPEN ")
                    print("")
                    self.outputArr.append(f"PORT {i}")
                self.s.close()

            print(f" Time taken: {round(time.time() - self.startTime, 2)} seconds ")

            print("")

            self.txtOutput = input(" Would you like a txt file with the results? (y/n)")


            if self.txtOutput.lower() == "y":
                self.dateTime = int(time.time())
                self.downloads_path = str(Path.home() / "Downloads")

                with open(f"{self.downloads_path}/Port_Scanner_Results-{self.dateTime}.txt", 'w') as f:
                    for a in self.outputArr:
                        f.write(a + ": OPEN" + "\n")

                print("")
                print(f" File has been created at {self.downloads_path}")

            else:
                pass

        except:
            print(" An error occurred")




PortScanner()
