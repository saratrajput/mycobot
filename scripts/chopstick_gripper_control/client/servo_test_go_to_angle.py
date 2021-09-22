"""
Test script to control servo motor with RaspberryPi.

Source: https://youtu.be/xHDT4CwjUQE
"""


import time
import RPi.GPIO as GPIO

# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11, GPIO.OUT)
servo1 = GPIO.PWM(11, 50) # Note 11 is pin, 50 = 50Hz pulse

# Start PWM running, but with value of 0 (pulse off)
servo1.start(0)

# Loop to allow user to set servo angle. Try/finally allows exit with execution of
# servo.stop and GPIO cleanup
try:
    while True:
        # Ask user for angle and turn servo to it
        angle = float(input('Enter angle between 0 & 180: '))
        servo1.ChangeDutyCycle(2+(angle/18))
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)

finally:
    # Clean things up at the end
    servo1.stop()
    GPIO.cleanup()
    print("Goodbye!")
