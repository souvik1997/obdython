import obd_io
import serial
import platform

from obd_utils import scanSerial

class OBD_Recorder():
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
            
o = OBD_Recorder()
o.connect()