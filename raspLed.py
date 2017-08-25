import RPi.GPIO as GPIO #This first line import the library GPIO for use the raspberry pins
import time #This library import time for pause the script later on
#from led import leD

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) #This line tell python not print GPIO warning messages to the screen
GPIO.setup(18,GPIO.OUT) #Choice your port in output
print "Led ON"
GPIO.output(18, GPIO.HIGH)
time.sleep(1)
print "Led OFF"
GPIO.output(18,GPIO.LOW)
