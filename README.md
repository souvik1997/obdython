# obdython - An OBD-II compliant car diagnostic tool

obdython is designed to interface with low-cost ELM 32x OBD-II diagnostic interfaces. 

obdython is written in Python. It is based on code originally written by Donour Sizemore, maintained by SECONS Ltd., under the name 'pyobd'.

## What's new in this fork?

obdython has been rewritten to work as a Python module. You can now install obdython and import it in your code. obdython's GUI and capturing code has been removed and all code has been merged into one file to avoid complications. You can specify a sensor to read by its name instead of its index in the list, and everything has been updated to work with Python 3. 

Example:
	
	from obdython import Device, OBDPort  
	import time  
	dev = Device(Device.types['bluetooth'], bluetooth_mac="AA:BB:CC:11:22:33", bluetooth_channel=1)  
	port = OBDPort(dev)  
	time.sleep(0.1) # Program needs to wait for adapter to come online  
	port.connect()  
	time.sleep(0.1)  
	port.ready()  
	print(port.sensor('rpm'))  
