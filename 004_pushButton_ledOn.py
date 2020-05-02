import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

ledPin = 11
buttonPin = 16
GPIO.setmode(GPIO.BOARD)

GPIO.setup(ledPin, GPIO.OUT)
GPIO.output(ledPin, GPIO.LOW)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(buttonPin, GPIO.FALLING) # Waits until the button is down 
    print("Button pressed")
    GPIO.output(ledPin, GPIO.HIGH)
    GPIO.wait_for_edge(buttonPin, GPIO.RISING) # Waits until the button is up
    GPIO.output(ledPin, GPIO.LOW)

GPIO.cleanup()
