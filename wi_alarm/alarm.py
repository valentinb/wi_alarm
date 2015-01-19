import __init__
from cross import time_printer_7seg
from apscheduler.schedulers.background import BackgroundScheduler
import time_manager
import time

printer = time_printer_7seg.TimePrinter()
scheduler = BackgroundScheduler()
time_manager = time_manager.TimeManager(printer, scheduler)
while 1:
    command = raw_input("command\n")
    if command == "q":
        break
