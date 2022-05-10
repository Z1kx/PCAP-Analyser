import socket
from PCAPFile import PCAPFile
from Trame import Trame
from ipHeader import ipHeader


def main():
    conn = socket.socket(socket.AF_PACKET,socket.SOCK_RAW,socket.ntohs(3))
    pcap = PCAPFile('packets3.pcap')
    numeroTrame =0

    while True:
        try:
            raw_data, addr = conn.recvfrom(65535)

            pcap.write(raw_data)

            #j'incrémente mon numéro de trame
            numeroTrame +=1
            print(f"Trame numéro [{numeroTrame}]")

            #j'appelle ma classe Trame avec raw_data comme données
            maTrame = Trame(raw_data)
            

            #affichage des adresse MAC
            Trame.afficherAdresseMacSrc(maTrame)
            Trame.afficherAdresseMacDest(maTrame)

            #si mon protocol est le protocol IPv4 j'identifie le protocol associé
            if maTrame.protocol == 2048:
                monIpHeader = ipHeader(raw_data)
                ipHeader.identifierProtocol(monIpHeader)
        except KeyboardInterrupt:
            pcap.close()
            exit()
    

if __name__ == '__main__':
    main() 