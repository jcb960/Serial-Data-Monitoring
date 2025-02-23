Project from 2022
Configure the micro:bit using the code given in the text file in MakeCode Python.
The module needed to run python script: pyserial (not serial)
Find the correct the COMx using this script below

import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print("Found port:", port.device, "-", port.description)

Get the COMx with USB connected to it.
