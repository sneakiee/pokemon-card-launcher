from machine import Pin, SoftI2C, SPI
from mfrc522 import MFRC522
import time
import nfcwriter
import bitmaps
import ssd1306
import framebuf

i2c = SoftI2C(scl=Pin(1), sda=Pin(2))

oled_width = 128
oled_height = 128
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

spi = SPI(0, baudrate=1_000_000, polarity=0, phase=0,
          sck=Pin(9), mosi=Pin(10), miso=Pin(6))
rdr = MFRC522(spi=spi, gpio_rst=Pin(5), gpio_cs=Pin(7))

key = b'\xff\xff\xff\xff\xff\xff'
block = 8

last_seen_uid = None

def read_from_tag():
    (stat, _) = rdr.request(rdr.REQIDL)
    if stat == rdr.OK:
        (stat, uid) = rdr.anticoll()
        if stat == rdr.OK:
            if rdr.auth(rdr.AUTHENT1A, block, key, uid) == rdr.OK:
                data = rdr.read(block)
                string_from_tag = data.decode().strip()
                rdr.stop_crypto1()
                return string_from_tag
    return None

in3 = Pin(19, Pin.OUT)
in4 = Pin(20, Pin.OUT)

button = Pin(29, Pin.IN, Pin.PULL_DOWN)

motor_on = False

def motor_forward():
    in3.value(1)
    in4.value(0)

def motor_stop():
    in3.value(0)
    in4.value(0)

while True:
    # RFID check
    string = read_from_tag()
    
    if string:
        if string != last_seen_uid:
            if id == "pokeball":
                image = bitmaps.pokeball
            elif id == "trainercard":
                image = bitmaps.trainercard
            else:
                image = bitmaps.default

            fb = framebuf.FrameBuffer(image, 128, 128, framebuf.MONO_HLSB)

            oled.fill(0)
            oled.show()
    time.sleep(0.5)
    
	# motor check
    if button.value():
        motor_on = not motor_on 
        if motor_on:
            motor_forward()
        else:
            motor_stop()
        sleep(0.3)