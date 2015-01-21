import __init__
from cross import time_printer_7seg
from apscheduler.schedulers.background import BackgroundScheduler
import time_manager
import radio_manager
import time

printer = time_printer_7seg.TimePrinter()
scheduler = BackgroundScheduler()
time_manager = time_manager.TimeManager(printer, scheduler)
radio_manager = radio_manager.RadioManager(scheduler)
scheduler.start()
while 1:
    time.sleep(1)

