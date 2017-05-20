import smbus
import time

ESC_ADDR = 0x29

THROTTLE_ADDR_L = 0x00
THROTTLE_ADDR_H = 0X01

arm = 0x00
start = 0x0A
stop = 0x00

bus = smbus.SMBus(1)

bus.write_byte_data(ESC_ADDR, THROTTLE_ADDR_L, arm)
bus.write_byte_data(ESC_ADDR, THROTTLE_ADDR_H, arm)

time.sleep(1)

bus.write_byte_data(ESC_ADDR, THROTTLE_ADDR_L, start)
bus.write_byte_data(ESC_ADDR, THROTTLE_ADDR_H, start)

time.sleep(2)

bus.write_byte_data(ESC_ADDR, THROTTLE_ADDR_L, stop)
bus.write_byte_data(ESC_ADDR, THROTTLE_ADDR_H, stop)
