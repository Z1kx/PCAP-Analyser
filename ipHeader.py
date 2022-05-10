from struct import *
import socket

class ipHeader:

    def __init__(self,data):
        
        #On récupère le numéro du protocol
        self.protocol = int.from_bytes(data[23:24],"little")
    
    #fonction d'identification du protocol pour affichage dans la console
    def identifierProtocol(self):
        if self.protocol == 1:
            print("IPv4 => 1 => ICMP\n")
        elif self.protocol == 17:
            print("IPv4 => 17 => UDP\n")
        elif self.protocol == 6:
            print("IPv4 => 6 => TCP\n")
        else:
            print("IPv4 => "+ str(self.protocol) + " => ???\n")