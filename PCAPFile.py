from struct import pack
import time

class PCAPFile:
    def __init__(self, filename):
        self.fp = open(filename, "wb")
        header = pack('!IHHiIII', 0xa1b2c3d4, 2, 4, 8, 8, 65535, 1)
        #print(header.hex())
        self.fp.write(header)
    
    def write(self,data):
        seconds, mseconds = [int(part) for part in str(time.time()).split('.')]
        lenght = len(data)
        message = pack('!IIII', seconds, mseconds, lenght, lenght)
        self.fp.write(message)
        self.fp.write(data)
        #print(data)
    
    def close(self):
        self.fp.close()