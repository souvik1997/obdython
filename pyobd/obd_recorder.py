#!/usr/bin/env python

import obd_io
import serial
import obd_sensors

from obd_utils import scanSerial

class OBD_Recorder():
	def __init__(self, sensors):
		self.port = None
		self.sensorlist = []
		for item in sensors:
			self.addsensor(item)
		connect()

	def connect(self):
		portnames = scanSerial()
		print(portnames)
		for port in portnames:
			self.port = obd_io.OBDPort(port, None, 2, 2)
			if(self.port.State == 0):
				self.port.close()
				self.port = None
			else:
				break
		if(self.port):
			print("Connected to "+self.port.port.name)

	def is_connected(self):
		return self.port

	def addsensor(self, item):
		for index, e in enumerate(obd_sensors.SENSORS):
			if(item == e.shortname):
				self.sensorlist.append(index)
				break

	def record_data(self, callback):
		if(self.port is None):
			return None
		while 1:
			results = {}
			for index in self.sensorlist:
				(name, value, unit) = self.port.sensor(index)
				results[obd_sensors.SENSORS[index].shortname] = value;
			callback(results)
