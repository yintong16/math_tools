#this is a timing side channel attack is implemented on Resberry Pi 5
#to attack Analog Device MAX78000FTHR


import time
import serial
# import gpiod

# chip = gpiod.Chip('gpiochip4')
# BUTTON_PIN = 27
# button_line = chip.get_line(BUTTON_PIN)
# button_line.request(consumer="Button", type=gpiod.LINE_REQ_DIR_IN)

tic = time.perf_counter()
toc = time.perf_counter()

def debug():
    try:
       while True:
           button_state = button_line.get_value()
           print(button_state)
    finally:
        led_line.release()
        button_line.release()

def brute_force(num):
    a = 0
    for i in range(0, 1):
        serialPort = serial.Serial(port="COM8", baudrate=115200)
        serialPort.write(b"replace\n")
        print(serialPort.read())
#         serialPort.write(num)
#         for line in serialPort.read():
#             print(chr(line))
            
#         tic = time.perf_counter()
#         while button_line.get_value()!=0:
#             continue
#         toc = time.perf_counter()
#         a += toc - tic
    
#     return a / 100

brute_force(b"000000\n")

    
# array = []
# print(array)
# array.append(brute_force(b"000000\n"))
# print(array)
# array.append(brute_force(b"100000\n"))
# print(array)
# array.append(brute_force(b"200000\n"))
# print(array)
# array.append(brute_force(b"300000\n"))
# print(array)
# array.append(brute_force(b"400000\n"))
# print(array)
# array.append(brute_force(b"500000\n"))
# print(array)
# array.append(brute_force(b"600000\n"))
# print(array)
# array.append(brute_force(b"700000\n"))
# print(array)
# array.append(brute_force(b"800000\n"))
# print(array)
# array.append(brute_force(b"900000\n"))
# print(array)