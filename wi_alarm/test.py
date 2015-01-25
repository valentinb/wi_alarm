import time
import os
from cross import button_gpio

button = button_gpio.Button()

while True:
	if button.IsPressed():
		os.system("ls")
