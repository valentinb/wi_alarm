import time
import os

class RadioManager():
	'''Manage Radio'''

	def __init__(self, scheduler, button):
		self.button = button
		scheduler.add_job(self.update_radio, 'interval', minutes=0.01)

	def update_radio(self):
		hours   = int(time.strftime("%H", time.localtime()))
		minutes = int(time.strftime("%M", time.localtime()))
		if self.button.IsPressed():
			os.system("omxplayer -o local sogipong.mp3")
		if 10 == hours:
			if 0 == minutes:
				os.system("omxplayer -o local sogipong.mp3")
		if 11 == hours:
			if 0 == minutes:
				os.system("omxplayer -o local sogipong.mp3")
		if 14 == hours:
			if 30 == minutes:
				os.system("omxplayer -o local sogipong.mp3")
		if 15 == hours:
			if 30 == minutes:
				os.system("omxplayer -o local sogipong.mp3")
		if 16 == hours:
			if 30 == minutes:
				os.system("omxplayer -o local sogipong.mp3")
		if 17 == hours:
			if 30 == minutes:
				os.system("omxplayer -o local sogipong.mp3")
