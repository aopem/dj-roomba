"""Class for serial I2C communication with microcontroller

Sends/Receives raw data over serial bus to microcontroller.
"""
import serial

class Serial:
  
  def __init__(self):
    self.ser = serial.Serial(
        port='/dev/ttyACM0', 
        baudrate = 9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1
    )

  #write to serial with data
  def write(self, left, right):
    self.ser.write(bytes(str(left) + "," + str(right) + "\n", 'utf-8'))
    print('sent: ' + str(left) + ', ' + str(right))

  #keep reading until value is received, then return 
  def read(self):
    received = self.ser.readline().decode('utf-8')

    # while(not received):
    #   received = self.ser.readline()

    # print('recieved: ' + received)
    # received_int = int(received) - 48
    return received

  def close(self):
    self.ser.close()

