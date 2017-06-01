#!/usr/bin/python
import smbus;
import time;
import sys;
import datetime as timeStamp;

######################################################################
# Pi addresses
acclAddr 		= 0x1D;

######################################################################
#write addresses
CTRL_REG0_XM 	= 0x1F;
CTRL_REG1_XM 	= 0x20;
CTRL_REG2_XM	= 0x21;
CTRL_REG3_XM	= 0x22;
CTRL_REG4_XM	= 0x23;
CTRL_REG5_XM	= 0x24;
CTRL_REG6_XM	= 0x25;
CTRL_REG7_XM	= 0x26;
FIFO_CTRL_REG	= 0X2E;

# Read addresses

# accl
FIFO_SRC_REG	= 0X2F;
OUT_X_L_A		= 0x28;
OUT_X_H_A		= 0x29;
OUT_Y_L_A		= 0x2A;
OUT_Y_H_A		= 0x2B;
OUT_Z_L_A		= 0x2C;
OUT_Z_H_A 		= 0x2D;


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
bus.write_byte_data(acclAddr, CTRL_REG0_XM, 0x40);
bus.write_byte_data(acclAddr, CTRL_REG1_XM, 0x47);
bus.write_byte_data(acclAddr, CTRL_REG2_XM, 0xCE);
bus.write_byte_data(acclAddr, CTRL_REG3_XM, 0x00);
bus.write_byte_data(acclAddr, CTRL_REG4_XM, 0x00);
bus.write_byte_data(acclAddr, CTRL_REG5_XM, 0x6C);
bus.write_byte_data(acclAddr, CTRL_REG6_XM, 0x20);
bus.write_byte_data(acclAddr, CTRL_REG7_XM, 0x00);
bus.write_byte_data(acclAddr, FIFO_CTRL_REG, 0x40);

time.sleep(2);

try:
	print "\n\nCalibrating";
	# before = "\n\n" + str(timeStamp.datetime.now().time()) + ":";
	# f.write(before);
	bus.read_i2c_block_data(acclAddr, OUT_X_L_A);
	bus.read_i2c_block_data(acclAddr, OUT_X_H_A);
	bus.read_i2c_block_data(acclAddr, OUT_Y_L_A);
	bus.read_i2c_block_data(acclAddr, OUT_Y_H_A);
	bus.read_i2c_block_data(acclAddr, OUT_Z_L_A);
	bus.read_i2c_block_data(acclAddr, OUT_Z_H_A);

	print bus.read_byte_data(acclAddr, FIFO_SRC_REG);
	while(bus.read_byte_data(acclAddr, FIFO_SRC_REG) != 0xDF):
		time.sleep(.1);
		print "write";
	print "full";
except KeyboardInterrupt:
	# after = "\n" + str(timeStamp.datetime.now().time()) + ":";
	# f.write(after);
	print("\n\nDone\n\n");
