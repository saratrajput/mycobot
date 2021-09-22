"""
Script to receive EMG signal intensity from SpikerBox's Arduino, classify it
and send it to myCobot through zmq.

Author: Suraj Pattar
Date: 23/09/2021
"""


import time
import serial
import zmq

# Define zmq port
port = "8001"
# Setup zmq
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

# Setup serial port address and baud rate for your SpikerBox's Arduino
ser = serial.Serial("/dev/ttyACM0", 9600)
level1 = 100

# Classify EMG signals in two levels and send it to the robot
while True:
    cc=str(ser.readline())
    inten = cc[2:][:-8]

    try:
        inten = int(float(inten))
        if inten > 0 and inten < level1:
            print("level 1")
            socket.send_string("1")
        elif inten > level1:
            print("level 2")
            socket.send_string("2")
    except:
        print("Values not ready yet!")

