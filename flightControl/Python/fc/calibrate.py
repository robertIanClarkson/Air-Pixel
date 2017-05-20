#!/usr/bin/python
# CalibrateMotor.py
# Robert I Clarkson

from time import sleep
import pigpio
import RPi.GPIO as GPIO

# Sensor
import sensorFunc
import sensorAdres
import smbus

# Flight
import flightFunc

# User
gyroAdres = 0x6B
acclAdres = 0x1D
magAdres = 0x1D

topPin = input("\n------ Set First Pin: ")
buttPin = input("------ Set Second Pin: ")

GPIO.setmode(GPIO.BCM) # Initialize pins
pi = pigpio.pi() # Initialize pi
bus = smbus.SMBus(1) # Initialize bus

try:

	print "   --- Writing to Sensors"
	# write to Gyro
	sensorFunc.write(bus=bus, master=gyroAdres, register=sensorAdres.CTRL_REG1_G, val=0x0F)
	sensorFunc.write(bus=bus, master=gyroAdres, register=sensorAdres.CTRL_REG4_G, val=0x30)

	sleep(0.5)

	# write to Accl
	sensorFunc.write(bus=bus, master=acclAdres, register=sensorAdres.CTRL_REG1_XM, val=0x67)
	sensorFunc.write(bus=bus, master=acclAdres, register=sensorAdres.CTRL_REG2_XM, val=0x20)

	sleep(0.5)

	# write to Mag
	sensorFunc.write(bus=bus, master=magAdres, register=sensorAdres.CTRL_REG5_XM, val=0x70)
	sensorFunc.write(bus=bus, master=magAdres, register=sensorAdres.CTRL_REG6_XM, val=0x60)
	sensorFunc.write(bus=bus, master=magAdres, register=sensorAdres.CTRL_REG7_XM, val=0x00)

	sleep(0.5)

	# Initialize ESC then start at lowest power
	print("   --- Initializing ESCs")
	pi.set_servo_pulsewidth(topPin, 1860)
	pi.set_servo_pulsewidth(buttPin, 1860)
	sleep(2)
	pi.set_servo_pulsewidth(topPin, 1060)
	pi.set_servo_pulsewidth(buttPin, 1060)
	sleep(2)
	pi.set_servo_pulsewidth(topPin, 0)
	pi.set_servo_pulsewidth(buttPin, 0)
	print("   --- Motors ON")
	sleep(1)
	pi.set_servo_pulsewidth(topPin, 1130)
	pi.set_servo_pulsewidth(buttPin, 1130)
	sleep(1)

	# for averaging the data readings
	looper = {
		'cycleCount' : 0,
		'avg_gyro_x' : 0,
		'avg_gyro_y' : 0,
		'avg_gyro_z' : 0,
		'avg_accl_x' : 0,
		'avg_accl_y' : 0,
		'avg_accl_z' : 0,
		'avg_mag_x' : 0,
		'avg_mag_y' : 0,
		'avg_mag_z' : 0
	}

	print "   --- Reading from Sensors"
	sleep(1)
	print "   --- Starting Flight Routine"
	sleep(1)

	while True:
		# read from Gyro
		gyro = {
			'x' : sensorFunc.read(bus=bus, master=gyroAdres, slaveLow=sensorAdres.OUT_X_L_G, slaveHigh=sensorAdres.OUT_X_H_G),
			'y' : sensorFunc.read(bus=bus, master=gyroAdres, slaveLow=sensorAdres.OUT_Y_L_G, slaveHigh=sensorAdres.OUT_Y_H_G),
			'z' : sensorFunc.read(bus=bus, master=gyroAdres, slaveLow=sensorAdres.OUT_Z_L_G, slaveHigh=sensorAdres.OUT_Z_H_G)
		}
		# read from Accl
		accl = {
			'x' : sensorFunc.read(bus=bus, master=acclAdres, slaveLow=sensorAdres.OUT_X_L_A, slaveHigh=sensorAdres.OUT_X_H_A),
			'y' : sensorFunc.read(bus=bus, master=acclAdres, slaveLow=sensorAdres.OUT_Y_L_A, slaveHigh=sensorAdres.OUT_Y_H_A),
			'z' : sensorFunc.read(bus=bus, master=acclAdres, slaveLow=sensorAdres.OUT_Z_L_A, slaveHigh=sensorAdres.OUT_Z_H_A)
		}
		# read from Mag
		mag = {
			'x' : sensorFunc.read(bus=bus, master=magAdres, slaveLow=sensorAdres.OUT_X_L_M, slaveHigh=sensorAdres.OUT_X_H_M),
			'y' : sensorFunc.read(bus=bus, master=magAdres, slaveLow=sensorAdres.OUT_Y_L_M, slaveHigh=sensorAdres.OUT_Y_H_M),
			'z' : sensorFunc.read(bus=bus, master=magAdres, slaveLow=sensorAdres.OUT_Z_L_M, slaveHigh=sensorAdres.OUT_Z_H_M)
		}

		flightFunc.logic( looper=looper, pi=pi, topPin=topPin, buttPin=buttPin, gyro=gyro, accl=accl, mag=mag )

		#sleep(0.001)

except (KeyboardInterrupt, SystemExit):
	print "\n   --- Interrupt"
finally:
	pi.set_servo_pulsewidth(topPin, 1130)
	pi.set_servo_pulsewidth(buttPin, 1130)
	print("   --- Stopping")
	sleep(3)
	pi.set_servo_pulsewidth(topPin, 0)
	pi.set_servo_pulsewidth(buttPin, 0)
	pi.stop()
	print "------ Finished"
