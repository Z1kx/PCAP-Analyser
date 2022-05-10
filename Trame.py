from struct import *
import socket

class Trame:

    def __init__(self,data):
        
        #unpack des 6 octets de l'adresse MAC dest, 6 octets de l'adresse MAC source, 2 octets EtherType
        unpacked = unpack('!6s6s2s', data[:14])

        #2 derniers octets (EtherType)
        self.protocol = socket.htons(int.from_bytes(data[12:14], "little")) #on aurait pu utiliser unpacked[2]

        #6 premiers octets (Adresse MAC destination)
        self.MACdest = data[:6]

        #les 6 octets suivant les 6 premiers (Adresse MAC source)
        self.MACsource = data[6:12]


    #fonction d'affichage de l'adresse mac destination au format XX:XX:XX:XX:XX:XX
    def afficherAdresseMacDest(self):
        macDestHex = str(self.MACdest.hex())
        maListe = []

        for i in range(0, len(macDestHex), 2):
            maListe.append(macDestHex[i:i+2])
            
        adresseMac = ":".join(maListe)
        adresseMac = adresseMac.upper()
        print("MAC Destination : " + adresseMac)

    #fonction d'affichage de l'adresse mac source au format XX:XX:XX:XX:XX:XX
    def afficherAdresseMacSrc(self):
        macSrcHex = str(self.MACsource.hex())
        maListe = []

        for i in range(0, len(macSrcHex), 2):
            maListe.append(macSrcHex[i:i+2])

        adresseMac = ":".join(maListe)
        adresseMac = adresseMac.upper()
        
        print("MAC Source : " + adresseMac)

        
    #fonction d'affichage dans la console suivant le protocol
    def afficherProtocol(self):
        if self.protocol == 2048:
            print("Protocol: 2048 => IPv4\n")
        elif self.protocol == 2054:
            print("Protocol: 2054 => ARP\n")
        elif self.protocol == 2114:
            print("Protocol: 2114 => WoL\n")
        elif self.protocol == 24579:
            print("Protocol: 24579 => DECnet\n")
        elif self.protocol == 32821:
            print("Protocol: 32821 => RARP\n")
        elif self.protocol == 32923:
            print("Protocol: 32923 => AppleTalk\n")
        elif self.protocol == 33011:
            print("Protocol: 33011 => AARP\n")
        elif self.protocol == 34525:
            print("Protocol: 34525 => IPv6\n")
        else:
            print("Protocol : " + str(self.protocol) + " => ???\n")
        
    



