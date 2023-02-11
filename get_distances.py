import serial

ser = serial.Serial('/dev/cu.usbmodem11201', 115200, timeout=1)

def read_serial():
    a = ser.readline()
    b = ser.readline()
    c = ser.readline()
    d = ser.readline()
    return a,b,c,d