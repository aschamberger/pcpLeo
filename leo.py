#!/usr/bin/python
import logging, sys
import RPi.GPIO as GPIO
import time
from LMSTools import LMSDiscovery, LMSServer, LMSPlayer

logging.basicConfig(stream=sys.stdout, level=logging.WARNING)

# player control
pin_play_pause     = 25
pin_track_previous = 5
pin_track_next     = 6
pin_volume_lower   = 12
pin_volume_raise   = 13
playing = False
pause = False

# status led
pin_led_red = 17
pin_led_green = 27
led_blink_interval = 0.25 # in seconds

# iButton
w1_slave_dir = "/sys/devices/w1_bus_master1/w1_master_slaves"
active_button = False

# mac id
mac_id_dir = "/sys/class/net/wlan0/address"
f = open(mac_id_dir, "r")
mac_id = f.read().strip()
f.close()

def doPlayPause(channel):
    global playing, pause
    logging.debug ("button play/pause")
    if playing == False:
        playing = True
        logging.debug(">> play first playlist item")
        playButtonId()
    elif playing == True and pause == False:
        pause = True
        logging.debug(">> pause")
        player.pause()
    else:
        pause = False
        logging.debug(">> play")
        player.play()

def doTrackPrevious(channel):
    logging.debug ("button previous track")
    player.prev()

def doTrackNext(channel):
    logging.debug ("button next track")
    player.next()

def doVolumeLower(channel):
    logging.debug ("button lower volume")
    player.volume_down()

def doVolumeRaise(channel):
    logging.debug ("button raise volume")
    player.volume_up()

def playButtonId(button_id=""):
    global player, playing, active_button
    # search for player name folder in favorites
    r = searchFavorites("", player.name)
    # strip obsolete id from beginning
    id = r[0]["id"].split(".")[1]
    # search for iButton id
    r = searchFavorites(id, button_id)
    if len (r) > 0:
        # play returned item
        playFavorite(r[0]["id"])
        playing = True
        active_button = button_id
    
def playFavorite(item_id):
    global player
    player.request("favorites playlist play item_id:{}".format(item_id))

def searchFavorites(item_id, search=""):
    global player
    try:
        response = player.parse_request("favorites items 0 item_id:{}".format(item_id), "loop_loop")
    except:
        response = []   
    favorites = []
    for item in response:
        if search == "" or search in item['name']:
            favorites.append(item)
    return favorites    
    
def main():
    global player, playing, pause
    
    # LMSTools
    servers = LMSDiscovery().all()
    logging.debug("LMS host = {}".format(servers[0]["host"]))
    logging.debug("LMS port = {}".format(servers[0]["port"]))
    server = LMSServer(servers[0]["host"], servers[0]["port"])
    logging.debug("MAC ID = {}".format(mac_id))
    player = LMSPlayer(mac_id, server)
    logging.debug("Player name = {}".format(player.name))
    
    # GPIO settings
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_play_pause, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(pin_track_previous, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(pin_track_next, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(pin_volume_lower, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(pin_volume_raise, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(pin_led_red, GPIO.OUT)
    GPIO.setup(pin_led_green, GPIO.OUT)
    GPIO.add_event_detect(pin_play_pause, GPIO.RISING, callback = doPlayPause, bouncetime = 200)
    GPIO.add_event_detect(pin_track_previous, GPIO.RISING, callback = doTrackPrevious, bouncetime = 200)
    GPIO.add_event_detect(pin_track_next, GPIO.RISING, callback = doTrackNext, bouncetime = 200)
    GPIO.add_event_detect(pin_volume_lower, GPIO.RISING, callback = doVolumeLower, bouncetime = 200)
    GPIO.add_event_detect(pin_volume_raise, GPIO.RISING, callback = doVolumeRaise, bouncetime = 200)

    while True:
        # init player state
        if player.mode == "play":
            playing = True
            pause = False
        elif player.mode == "pause":
            playing = True
            pause = True

        # status led
        # player ready: led blink slow (2x interval)
        if playing == False and pause == False:
            GPIO.output(pin_led_red, True)
            GPIO.output(pin_led_green, False)
            time.sleep(2*led_blink_interval)
            GPIO.output(pin_led_red, False)
            time.sleep(2*led_blink_interval)
        # player pause: led blink fast (1x interval)
        elif pause == True:
            GPIO.output(pin_led_red, False)
            GPIO.output(pin_led_green, True)
            time.sleep(led_blink_interval)
            GPIO.output(pin_led_green, False)
            time.sleep(led_blink_interval)
            GPIO.output(pin_led_green, True)
            time.sleep(led_blink_interval)
            GPIO.output(pin_led_green, False)
            time.sleep(led_blink_interval)
        # playing: led on (just wait 4x interval)
        else:
            GPIO.output(pin_led_red, False)
            GPIO.output(pin_led_green, True)
            time.sleep(4*led_blink_interval)

        # detect iButton
        f = open(w1_slave_dir, "r")
        current_button = f.read().strip()
        f.close()
        if current_button != 'not found.':
            logging.debug("iButton ID = {}".format(current_button))
            if current_button != active_button:
                # change track
                playButtonId(current_button)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()