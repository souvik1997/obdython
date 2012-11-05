import obd_io
import serial
import platform
import logging

from obd_utils import scanSerial

class OBD_Recorder():
    def __init__(self, filename):
        self.port = None
        self.logger = logging.getLogger(__name__)
        log_handler = logging.FileHandler(filename)
        log_formatter = logging.Formatter('%(asctime)s %(message)s')
        log_handler.setFormatter(log_formatter)
        self.logger.addHandler(log_handler)
        self.logger.setLevel(logging.INFO)
        
    def connect(self):
        portnames = scanSerial()
        print portnames
        for port in portnames:
            self.port = obd_io.OBDPort(port, None, 2, 2)
            if(self.port.State == 0):
                self.port.close()
                self.port = None
            else:
                break

        if(self.port):
            print "Connected to "+self.port.port.name
            
    def is_connected(self):
        return self.port
        
#    def record_data(self):
#        for n in range(1,10):
#            self.logger.info('woo %s %s %s yay', n, n, n)
            
            
        
o = OBD_Recorder('bikestuff.log')
o.connect()
if not o.is_connected():
    print "Not connected"
    
#o.record_data()