#!/usr/bin/python
import smbus;
import time;
import sys;
import datetime as timeStamp;

######################################################################
# Pi addresses
gyroAddr 		= 0x6B;
acclAddr 		= 0x1D;
magnAddr 		= 0x1D;

######################################################################
#write addresses
CTRL_REG1_G 	= 0x20;
CTRL_REG2_G 	= 0x21;
CTRL_REG3_G 	= 0x22;
CTRL_REG4_G 	= 0x23;
CTRL_REG5_G 	= 0x24;
CTRL_REG0_XM 	= 0x1F;
CTRL_REG1_XM 	= 0x20;
CTRL_REG2_XM	= 0x21;
CTRL_REG5_XM	= 0x24;
CTRL_REG6_XM	= 0x25;
CTRL_REG7_XM	= 0x26;

# Read addresses
# gyro
OUT_X_L_G		= 0x28;
OUT_X_H_G		= 0x29;
OUT_Y_L_G		= 0x2A;
OUT_Y_H_G		= 0x2B;
OUT_Z_L_G		= 0x2C;
OUT_Z_H_G		= 0x2D;
# accl
OUT_X_L_A		= 0x28;
OUT_X_H_A		= 0x29;
OUT_Y_L_A		= 0x2A;
OUT_Y_H_A		= 0x2B;
OUT_Z_L_A		= 0x2C;
OUT_Z_H_A 		= 0x2D;
# mag
OUT_X_L_M		= 0x08;
OUT_X_H_M		= 0x09;
OUT_Y_L_M		= 0x0A;
OUT_Y_H_M		= 0x0B;
OUT_Z_L_M		= 0x0C;
OUT_Z_H_M		= 0x0D;

######################################################################
# open file to for write
f = open('data.txt', 'a');
# Get I2C bus
bus = smbus.SMBus(1);

#

######################################################################
def convert(low, high):
	data = high * 256 + low;
	if (data > 32767) :
		data -= 65536;
	return data;

def show(msg, data):
	fin = msg + str(data);
	sys.stdout.write(fin);
	return;

def write(msg, data):
	fin = msg + str(data);
	f.write(fin);
	return;

######################################################################
# set chip
bus.write_byte_data(gyroAddr, CTRL_REG1_G,  0x6F);	# 0x0F		Data rate		 	= 95Hz, 		Power ON
bus.write_byte_data(gyroAddr, CTRL_REG2_G,  0x26);	# 0x30		DPS 				= 2000, 		Continuous update
bus.write_byte_data(gyroAddr, CTRL_REG4_G,  0x80);	# 0x30		DPS 				= 2000, 		Continuous update
bus.write_byte_data(gyroAddr, CTRL_REG5_G,  0x20);	# 0x30		DPS 				= 2000, 		Continuous update

bus.write_byte_data(acclAddr, CTRL_REG0_XM, 0xE7);
bus.write_byte_data(acclAddr, CTRL_REG1_XM, 0x4F);	# 0x67		Accel data rate 	= 100Hz, 		Power ON
bus.write_byte_data(acclAddr, CTRL_REG2_XM, 0xC8);	# 0xC8 		Accel Full scale 	= +/-4g, w/ 50Hz filter 		Accel Sensitivity
bus.write_byte_data(magnAddr, CTRL_REG5_XM, 0x70);	# 0x70 		Output data rate 	= 50Hz, 		Magnetic high resolution
bus.write_byte_data(magnAddr, CTRL_REG6_XM, 0x60);	# 0x60		Mag full scale 		= +/-12 gauss	Mag Sensitivity
bus.write_byte_data(magnAddr, CTRL_REG7_XM, 0xE0);	# 0x00		Normal mode, Magnetic continuous conversion mode

time.sleep(4);

try:
	print "\n\nCalibrating";
	before = "\n\n" + str(timeStamp.datetime.now().time()) + ":";
	f.write(before);
	
	while True:
		# Read --> Convert --> Print Gyro data
		write("\n", convert(bus.read_byte_data(gyroAddr, OUT_X_L_G), bus.read_byte_data(gyroAddr, OUT_X_H_G)));
		write(" | ", convert(bus.read_byte_data(gyroAddr, OUT_Y_L_G), bus.read_byte_data(gyroAddr, OUT_Y_H_G)));
		write(" | ", convert(bus.read_byte_data(gyroAddr, OUT_Z_L_G), bus.read_byte_data(gyroAddr, OUT_Z_H_G)));
		# Read --> Convert --> Print Accl data
		write(" | ", convert(bus.read_byte_data(acclAddr, OUT_Y_L_A), bus.read_byte_data(acclAddr, OUT_Y_H_A))/32);
		write(" | ", convert(bus.read_byte_data(acclAddr, OUT_Z_L_A), bus.read_byte_data(acclAddr, OUT_Z_H_A))/32);
		write(" | ", convert(bus.read_byte_data(acclAddr, OUT_X_L_A), bus.read_byte_data(acclAddr, OUT_X_H_A))/32);
		# Read --> Convert --> Print Magn data
		write(" | ", convert(bus.read_byte_data(magnAddr, OUT_X_L_M), bus.read_byte_data(magnAddr, OUT_X_H_M)));
		write(" | ", convert(bus.read_byte_data(magnAddr, OUT_Y_L_M), bus.read_byte_data(magnAddr, OUT_Y_H_M)));
		write(" | ", convert(bus.read_byte_data(magnAddr, OUT_Z_L_M), bus.read_byte_data(magnAddr, OUT_Z_H_M)));
		f.write(" | ");
		time.sleep(.1);
except KeyboardInterrupt:
	after = "\n" + str(timeStamp.datetime.now().time()) + ":";
	f.write(after);
	print("\n\nDone\n\n");
