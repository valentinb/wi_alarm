import pygst
import gst
import time

class RadioManager():
	'''Manage Radio'''

	MUSIC_STREAM_URI = 'http://mp3channels.webradio.antenne.de/chillout'

	def __init__(self, scheduler):
		self.player = gst.element_factory_make("playbin", "player");
		scheduler.add_job(self.update_radio, 'interval', minutes=0.01)

	def update_radio(self):
		hours   = int(time.strftime("%H", time.localtime()))
		minutes = int(time.strftime("%M", time.localtime()))
		if 22 == hours:
			if 19 == minutes:
				self.player.set_property('uri', 'http://mp3channels.webradio.antenne.de/chillout')
				self.player.set_state(gsp.STATE_PLAYING)
