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
 -        display.show('L')
 -        leftfwd.write_digital(1)
 -        rightfwd.write_digital(0)
 -    if signal=='R':
 -        display.show('R')
 -        leftfwd.write_digital(0)
 -        rightfwd.write_digital(1)
 -    if signal=='F':
 -        display.show('F')
 -        rightbck.write_digital(0)
 -        leftbck.write_digital(0)
 -        leftfwd.write_digital(1)
 -        rightfwd.write_digital(1)
 -    if signal=='B':
 -        display.show('B')
 -        leftfwd.write_digital(0)
 -        rightfwd.write_digital(0)    
 -        rightbck.write_digital(1)
 -        leftbck.write_digital(1)
 -    if signal=='-':
 -        leftfwd.write_digital(0)
 -        rightfwd.write_digital(0)    
 -        rightbck.write_digital(0)
 -        leftbck.write_digital(0)
 -
        
