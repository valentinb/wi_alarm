import __init__
from cross import time_printer_7seg
from cross import button_gpio
from apscheduler.schedulers.background import BackgroundScheduler
import time_manager
import radio_manager
import time

printer = time_printer_7seg.TimePrinter()
scheduler = BackgroundScheduler()
time_manager = time_manager.TimeManager(printer, scheduler)
button = button_gpio.Button()
radio_manager = radio_manager.RadioManager(scheduler, button)
scheduler.start()
while 1:
    time.sleep(1)

