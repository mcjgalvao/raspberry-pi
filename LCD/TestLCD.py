'''
Created on 11 de ago de 2017

@author: odp108109
'''
import os
from luma.core.interface.serial import i2c #@UnresolvedImport
from luma.core.render import canvas #@UnresolvedImport
from luma.oled.device import ssd1306 #@UnresolvedImport
from time import sleep
from PIL import ImageFont

def make_font(name, size):
    font_path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), 'fonts', name))
    print(font_path)
    return ImageFont.truetype(font_path, size)


# rev.1 users set port=0
# substitute spi(device=0, port=0) below if using that interface
serial = i2c(port=1, address=0x3C)

# substitute ssd1331(...) or sh1106(...) below if using that device
device = ssd1306(serial)

with canvas(device) as draw:
    font = make_font("OpenSans-Light.ttf",12)
    draw.rectangle(device.bounding_box, outline="white", fill="black")
    draw.text((2, 30), "Hello World", font=font, fill="white")


sleep(10.0)

