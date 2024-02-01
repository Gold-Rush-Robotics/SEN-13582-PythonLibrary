from SEN13582.SEN13582 import SEN13582
from board import SCL, SDA
import busio

i2c = busio.I2C(SCL, SDA)

sensor = SEN13582(i2c, 0x3e)


while True:
    sensor.scan()