import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

ledPin = 11  # Pin to be used
GPIO.setmode(GPIO.BOARD) # Set the pins enumerated in default order
GPIO.setup(ledPin, GPIO.OUT) # Set pin 11 as output

for x in range(10): # repeat 10 times
    GPIO.output(ledPin, GPIO.HIGH) #Turns led on
    time.sleep(1) #waits one second
    GPIO.output(ledPin, GPIO.LOW) #turns led off
    time.sleep(1)

GPIO.cleanup(); #Clean all to finish
print("Finished")