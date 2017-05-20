from time import sleep
import pigpio
import RPi.GPIO as GPIO

# Init
GPIO.setmode(GPIO.BCM)
pi = pigpio.pi()

# USER
ESC_GPIO = input("------ Set Pin: ")
startPower = input("------ Set Power( 1130 - 1805 ): ")

# Calibrate ESC
pi.set_servo_pulsewidth(ESC_GPIO, 1860) # Maximum throttle.
print("------ Init Throttle 1860")
sleep(2)
pi.set_servo_pulsewidth(ESC_GPIO, 1060) # Minimum throttle.
print("------ Init 1060")
sleep(2)
print("------ Pause")
pi.set_servo_pulsewidth(ESC_GPIO, 0)
sleep(1)
print("------ Starting Wait 3")
pi.set_servo_pulsewidth(ESC_GPIO, 1130)
sleep(3)
try:
	print("   --- Starting at %s")%startPower
	pi.set_servo_pulsewidth(ESC_GPIO, int(startPower))
	power = startPower
	while 1:
		user = input("   --- Enter new Power ( 1130 - 1805 | 0 to quit)\t:")
		if(user == 0):
			print("   --- Leaving")
			break
		elif(user == 6):
			power += 5
			print("   --- +5")
		elif(user == 4):
			power -= 5
			print("   --- -5")
		elif(user == 8):
			power += 100
			print("   --- +100")
		elif(user == 2):
			power -= 100
			print("   --- -100")
		else:
			power = user
		print("   --- Starting at %s")%power
		pi.set_servo_pulsewidth(ESC_GPIO, power)
finally:
	pi.set_servo_pulsewidth(ESC_GPIO, 1130)
	print("   --- Stopping")
	sleep(3)
	pi.set_servo_pulsewidth(ESC_GPIO, 0)
	pi.stop()
	print("------ Stop")
