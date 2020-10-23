#
#   Author:         Sebastien Parent-Charette (support@robotshop.com)
#   Version:        1.0.0
#   Licence:        LGPL-3.0 (GNU Lesser General Public License version 3)
#   
#   Desscription:   Basic example of the LSS moving back and forth.
#

# Import required liraries
import time
import serial
from time import sleep
# Import LSS library
import lss
import lss_const as lssc

# Constants
CST_LSS_Port = "/dev/serial/by-id/usb-FTDI_FT232R_USB_UART_AE4O4BBL-if00-port0"      # For Linux/Unix platforms
#CST_LSS_Port = "COM230"             # For windows platforms
CST_LSS_Baud = lssc.LSS_DefaultBaud

# Create and open a serial port
lss.initBus(CST_LSS_Port, CST_LSS_Baud)

# Create an LSS object
myLSS = lss.LSS(1)

# Initialize LSS to position 0.0 deg
myLSS.reset()
myLSS.move(0)
sleep(3)
print(myLSS.getPosition())
myLSS.move(3600*600)
i=0
while i<700:
    sleep(1)
    print(i," f ",myLSS.getPosition()," ",myLSS.getTemperature(),"C ",myLSS.getVoltage(),"V ",myLSS.getCurrent(),"A")
    i+=1
sleep(5)
print(myLSS.getPosition())

myLSS.move(0)
i=0
while i<700:
    sleep(1)
    print(i," b ",myLSS.getPosition()," ",myLSS.getTemperature(),"C ",myLSS.getVoltage(),"V ",myLSS.getCurrent(),"A")
    i+=1
print(myLSS.getPosition())


# Wait for it to get there
time.sleep(2)

exit(0)

# Loops between -180.0 deg and 180 deg, taking 1 second pause between each half-circle move.
while 1:
    # Send LSS to half a turn counter-clockwise from zero (assumes gyre = 1)
    myLSS.move(3600*10)
    
    # Wait for two seconds
    time.sleep(60)
    
    # Send LSS to half a turn clockwise from zero (assumes gyre = 1)
    myLSS.move(0)
    
    # Wait for two seconds
    time.sleep(2)

### EOF #######################################################################
