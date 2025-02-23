#Question 4 - 2022
import serial # pyserial
ser=serial.Serial()
ser.baudrate=115200
ser.port='COM3'
ser.open()
file2=open("temperatures_q3.csv", "w")
file3=open("lightLevel_q3.csv", "w")
for x in range(-1, 31):
    data=str(ser.readline())
    data=data.replace("b", "")
    data=data.replace("'", "")
    data=data.replace(" ", "")
    data=data.replace("\\r\\n", "")

    if len(data)>0 and x in range(1,31,1):
        if x%2 == 0:
            print("Time:",x,"| Light level:", data)
            file3.write(data+",")
        else:
            print("Time:",x,"| Temperature:", data)
            file2.write(data+",")
file2.close()
file3.close()

file2=open("temperatures_q3.csv", "r")
temp2=file2.read()
file2.close()
temp2List=temp2.split(",")
temp2List.remove(temp2List[-1])
temp2List=[int(item5) for item5 in temp2List]

file3=open("lightLevel_q3.csv", "r")
light=file3.read()
file3.close()
lightList=light.split(",")
lightList.remove(lightList[-1])
lightList=[int(item1) for item1 in lightList]

import matplotlib.pyplot as plt
numL=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
plt.plot(numL, temp2List)
plt.plot(lightList)
plt.legend(["Temperature(*C)", "Light level(0-255)"])
plt.xlabel("Time")
plt.show()