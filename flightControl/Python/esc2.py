from time import sleep
import pigpio
import RPi.GPIO as GPIO

# Init
GPIO.setmode(GPIO.BCM)
pi = pigpio.pi()

try:
	# USER
	ESC_GPIO_1 = input("------ Set Pin 1: ")
	ESC_GPIO_2 = input("------ Set Pin 2: ")
	startPower = input("------ Set Power( 1130 - 1805 ): ")

	# Calibrate ESC
	pi.set_servo_pulsewidth(ESC_GPIO_1, 1860) # Maximum throttle.
	pi.set_servo_pulsewidth(ESC_GPIO_2, 1860) # Maximum throttle.
	print("------ Init Throttle 1860")
	sleep(2)
	pi.set_servo_pulsewidth(ESC_GPIO_1, 1060) # Minimum throttle.
	pi.set_servo_pulsewidth(ESC_GPIO_2, 1060) # Minimum throttle.
	print("------ Init 1060")
	sleep(2)
	print("------ Pause")
	pi.set_servo_pulsewidth(ESC_GPIO_1, 0)
	pi.set_servo_pulsewidth(ESC_GPIO_2, 0)
	sleep(1)
	print("------ Starting Wait 3")
	pi.set_servo_pulsewidth(ESC_GPIO_1, 1130) # start throttle
	pi.set_servo_pulsewidth(ESC_GPIO_2, 1130) # start throttle
	sleep(3)

	print("   --- Starting at %s")%startPower
	pi.set_servo_pulsewidth(ESC_GPIO_1, int(startPower))
	pi.set_servo_pulsewidth(ESC_GPIO_2, int(startPower))
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
		pi.set_servo_pulsewidth(ESC_GPIO_1, power)
		pi.set_servo_pulsewidth(ESC_GPIO_2, power)
except NameError:
	print("\n   --- NameError")
finally:
	pi.set_servo_pulsewidth(ESC_GPIO_1, 1130)
	pi.set_servo_pulsewidth(ESC_GPIO_2, 1130)
	print("\n   --- Stopping")
	sleep(3)
	pi.set_servo_pulsewidth(ESC_GPIO_1, 0)
	pi.set_servo_pulsewidth(ESC_GPIO_2, 0)
	pi.stop()
	print("------ Stop")
