
import serial
import numpy as np
ser = serial.Serial('/dev/cu.usbmodem11301', 9600, timeout=1)


sensors = [[-17,33],[45,39],[36,0],[0,0],[8,69]]
def read_serial():
    a = ''
    vals = []
    while(a == ''):
        ser.write(b'123\n')
        print(a)
        a = ser.readline().decode().strip()
    print(a)
    out = []
    ss = []
    for idx,x in enumerate(a.split(",")):
        if int(x) < 60:
                out.append(int(x))
                ss.append(sensors[idx])
    return out,ss
    for i in range(10):
        a = ser.readline().decode().strip()
        vals.append([int(x) for x in a.split(",")])
    vals = np.array(vals)
    out = []
    ss = []
    for i in range(5):
        avg = np.average(vals[:,i]+5)
        if avg < 50:
            out.append(avg)
            ss.append(sensors[i])
    print(out)
    # print(type(a))
    # print(a.split(","))
    return out,ss

read_serial()
