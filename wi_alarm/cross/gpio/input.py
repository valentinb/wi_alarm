import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

class Input:

  def GetState(self):
    return (GPIO.input(23) == 1)


