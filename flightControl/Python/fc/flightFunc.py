def offset( acclZ ):
	offset = abs(-1500 - acclZ)-50
	return offset;

def react( pi, pin, offset ):
	pwm = (offset + 1130)
	if (pwm < 1130):
		pi.set_servo_pulsewidth(pin, 1130)
		print "       Pin: %s\t\tPWM: LOW"%(pin)
	elif (pwm > 1805):
		pi.set_servo_pulsewidth(pin, 1805)
		print "       Pin: %s\t\tPWM: HIGH"%(pin)
	else:
		pi.set_servo_pulsewidth(pin, pwm)
		print "       Pin: %s\t\tPWM: %s"%(pin, pwm)
	return;

def logic( looper, pi, topPin, buttPin, gyro, accl, mag):
	if(looper['cycleCount'] != 10):
		looper['avg_accl_z'] += offset(acclZ=accl['z'])
		looper['cycleCount'] += 1
	else:
		looper['avg_accl_z'] = looper['avg_accl_z'] / looper['cycleCount']
		react( pi=pi, pin=topPin, offset=looper['avg_accl_z'] )
		react( pi=pi, pin=buttPin, offset=looper['avg_accl_z'] )
		looper['cycleCount'] = 0
		looper['avg_accl_z'] = 0
	return;
