import pygst
import gst
import time

player = gst.element_factory_make("playbin", "player");
player.set_property('uri', 'http://mp3channels.webradio.antenne.de/chillout')
player.set_state(gst.STATE_PLAYING)

while True:
    time.sleep(1)
