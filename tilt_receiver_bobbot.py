#MicroBit Receiver Bobbot
from microbit import *
import radio
radio.on()
radio.config(channel=30)
rightfwd=pin16
leftfwd=pin12
rightbck=pin8
leftbck=pin0
while True:
    signal = radio.receive()
    if signal=='L':
        display.show('L')
        leftfwd.write_digital(1)
        rightfwd.write_digital(0)
    if signal=='R':
        display.show('R')
        leftfwd.write_digital(0)
        rightfwd.write_digital(1)
    if signal=='F':
        display.show('F')
        leftfwd.write_digital(1)
        rightfwd.write_digital(1)
    if signal=='B':
        display.show('B')
        leftfwd.write_digital(0)
        rightfwd.write_digital(0)    
        rightbck.write_digital(1)
        leftbck.write_digital(1)

