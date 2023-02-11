# from mock_serial import MockSerial

# device = MockSerial()
# device.open()

# device.stub(
#   receive_bytes=b'123',
#   send_bytes=b'456'
# )

import serial
ser = serial.Serial('/dev/cu.usbmodem11201', 115200, timeout=1)
# ser = serial.Serial(device.port)


# a = ser.readline()
# print(a)

def read_serial():
    ser.write(b'123')
    a = ser.readline().decode()
    b = ser.readline().decode()
    c = ser.readline().decode()
    d = ser.readline().decode()
    return a,b,c,d
