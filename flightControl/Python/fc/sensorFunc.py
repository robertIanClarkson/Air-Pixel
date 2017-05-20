def write( bus, master, register, val ):
	# (addr,cmd,val)
	bus.write_byte_data(master, register, val) # Data rate = 95Hz, Power ON
	bus.write_byte_data(master, register, val) # DPS = 2000, Continuous update
	# print("   --- Wrote to Gyro")
	return;

def convert( data0, data1 ):
	data = data1 * 256 + data0
	if data > 32767 :
		data -= 65536
	# print("   --- Converted Data")
	return data;

def read( bus, master, slaveLow, slaveHigh ):
	# (addr,cmd)
	data0 = bus.read_byte_data(master, slaveLow)
	data1 = bus.read_byte_data(master, slaveHigh)
	# print("   --- Read")
	return convert(data0=data0, data1=data1);
