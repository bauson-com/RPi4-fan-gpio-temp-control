import sys, os, RPi.GPIO as GPIO
pin=12
max=45
min=50

def startup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT)

def getStatus():
    with open('/home/pi/project/fan/log.txt', 'r') as file:
        data = file.read().replace('\n', '')
    return data

def updateStatus(str):
    status = open("/home/pi/project/fan/log.txt", "w")
    status.write(str)
    status.close()

def getTemp():
    temp = os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("temp=","")
    temp = temp.replace("'C","")
    temp = temp.replace("\n","")
    return int(float(temp))

def fanOn(pin):
    GPIO.output(pin,True)

def fanOff(pin):
    GPIO.output(pin,False)    

status=getStatus()
temp=getTemp()
startup()

if temp > max and status!="ON":
    updateStatus("ON")
    #print("Changed to ON")
    fanOn(pin)

if temp < min and status!="OFF":
    updateStatus("OFF")
    #print("Changed to OFF")
    fanOff(pin)
