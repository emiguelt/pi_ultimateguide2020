import RPi.GPIO as GPIO
import time

buttonPin = 16
GPIO.setmode(GPIO.BOARD)

GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

times = 0
while True:
  input_state = GPIO.input(buttonPin)
  if input_state == False:
    print("button pressed")
    times = times + 1
    time.sleep(0.3)
  if times == 10:
    break

GPIO.cleanup();
print("finished")
