#MicroBit Sender Bobbot
from microbit import *
import radio
radio.on()
radio.config(channel=30)
while True:
    reading_x = accelerometer.get_x()
    reading_y = accelerometer.get_y()
    if reading_x > 200:
        display.show('R')
        radio.send('R')
    elif reading_x < -200:
        display.show('L')
        radio.send('L')
    elif reading_y > 200:
        display.show('B')
        radio.send('B')
    elif reading_y < -200:
        display.show('F')
        radio.send('F')
    else:
        display.show('-')
        radio.send('-')
    sleep(100)
        