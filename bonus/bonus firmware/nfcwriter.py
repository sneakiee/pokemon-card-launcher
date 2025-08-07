from mfrc522 import MFRC522
from machine import Pin, SPI
import time

spi = SPI(0, baudrate=1_000_000, polarity=0, phase=0, 
          sck=Pin(6), mosi=Pin(7), miso=Pin(4))
rdr = MFRC522(spi=spi, gpio_rst=Pin(22), gpio_cs=Pin(5))

key = b'\xff\xff\xff\xff\xff\xff' # default RFID key
block = 8

def write_to_tag(string_data):
    print("Place tag to write...")

    while True:
        (stat, _) = rdr.request(rdr.REQIDL)
        if stat == rdr.OK:
            (stat, uid) = rdr.anticoll()
            if stat == rdr.OK:
                print("Tag UID:", uid)

                if rdr.auth(rdr.AUTHENT1A, block, key, uid) == rdr.OK:
                    data = bytearray(string_data.ljust(16))
                    rdr.write(block, data)
                    print("Written:", data.decode().strip())
                    rdr.stop_crypto1()
                    break
                else:
                    print("Auth failed")
        time.sleep(0.5)

# interchangeable bewtween pokeball/trainer card
write_to_tag("pokeball")