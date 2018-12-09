# pcpLeo

A [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) / [piCorePlayer](https://sites.google.com/site/picoreplayer/) based portable music streaming appliance I assembled for my son. 
Desired playlist is selected via [iButtons](https://datasheets.maximintegrated.com/en/ds/DS1990A.pdf) and playback can be controlled via push buttons.

[![Front](https://raw.githubusercontent.com/aschamberger/pcpLeo/master/img/front.jpg)](https://raw.githubusercontent.com/aschamberger/pcpLeo/master/img/front_full.jpg)
[![Back](https://raw.githubusercontent.com/aschamberger/pcpLeo/master/img/back.jpg)](https://raw.githubusercontent.com/aschamberger/pcpLeo/master/img/back_full.jpg)


## Parts list

* [Raspberry Pi Zero W](https://www.raspberrypi.org/products/raspberry-pi-zero-w/) [[Shop](https://buyzero.de/collections/boards-kits/products/raspberry-pi-zero-w)]
* [Header for Zero W (2,54 mm, 2X20)](https://www.reichelt.de/Stiftleisten/MPE-087-2-040/3/index.html?ACTION=3&GROUPID=7434&ARTICLE=119900)
* Micro SD Card
* USB Charger
* [USB Cable A to B](https://www.amazon.de/gp/product/B00NH11KIK/ref=oh_aui_detailpage_o01_s00?ie=UTF8&psc=1)
* [Neutrik NAUSB-W-B Reversibler USB-Adapter (Typ A und B)](https://www.amazon.de/gp/product/B003VSXQVI/ref=oh_aui_detailpage_o01_s01?ie=UTF8&psc=1)
* 2 x [Micro USB Cable 0.30m](https://www.amazon.de/gp/product/B00X61PN3O/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1)
* [Adafruit PowerBoost 1000 Charger](https://www.adafruit.com/product/2465) [[Shop](https://www.exp-tech.de/module/stromspannung/6462/adafruit-powerboost-1000-charger-rechargeable-5v-lipo-usb-boost-at-1a-1000c)]
* [LiPo 3,7V 2500mAh JST-PH Connector](https://eckstein-shop.de/LiPo-Akku-Lithium-Ion-Polymer-Batterie-37V-2500mAh-JST-PH-Connector)
* Stripboard + (4) pin strip + (4) socket strip
* [Reset / Enable Controller - KA75330 3.3V Voltage Detector](https://www.adafruit.com/product/3428) [[Shop](https://www.exp-tech.de/zubehoer/halbleiter/8017/reset/enable-controller-ka75330-3.3v-voltage-detector)]
* [Connector 3 pin male](https://www.reichelt.de/Platinen-Steckverbinder/PSS-254-3W/3/index.html?ACTION=3&LA=446&ARTICLE=14910&GROUPID=7525&artnr=PSS+254%2F3W)
* [Connector 3 pin female](https://www.reichelt.de/Platinen-Steckverbinder/PSK-254-3W/3/index.html?ACTION=3&LA=446&ARTICLE=14858&GROUPID=7525&artnr=PSK+254%2F3W)
* [Mini Panel Mount SPDT Toggle Switch](https://www.adafruit.com/product/3221) [[Shop](https://www.exp-tech.de/zubehoer/tasterschalter/7779/mini-panel-mount-spdt-toggle-switch)]
* [Adafruit Perma Proto Bonnet Mini Kit](https://www.adafruit.com/product/3203) [[Shop](https://www.exp-tech.de/zubehoer/breadboards/8279/adafruit-perma-proto-bonnet-mini-kit)]
* [GPIO Stacking Header for Pi A+/B+/Pi 2/Pi 3 - Extra-long 2x20 Pins](https://www.adafruit.com/product/2223) [[Shop](https://www.exp-tech.de/zubehoer/steckverbinder/6088/gpio-header-for-raspberry-pi-b-extra-long-2x20-female-header)]
* 4,7k Ohm resistor for 1-Wire
* 50 Ohm resistor for LED of 1-Wire reader
* 22 Ohm resistor for LED of push buttons
* [Connector JST XH4P ST90](https://www.reichelt.de/JST-Vielfachsteckverbinder/JST-XH4P-ST90/3/index.html?ACTION=3&GROUPID=7980&ARTICLE=185081)
* [Connector 2 pin male](https://www.reichelt.de/Platinen-Steckverbinder/PSS-254-2W/3/index.html?ACTION=3&LA=446&ARTICLE=14908&GROUPID=7525&artnr=PSS+254%2F2W)
* [Connector 2 pin female](https://www.reichelt.de/Platinen-Steckverbinder/PSK-254-2W/3/index.html?ACTION=3&LA=446&ARTICLE=14857&GROUPID=7525&artnr=PSK+254%2F2W)
* 2 x [Connector 3 pin male](https://www.reichelt.de/Platinen-Steckverbinder/PSS-254-3W/3/index.html?ACTION=3&LA=446&ARTICLE=14910&GROUPID=7525&artnr=PSS+254%2F3W) (combined for 6 pin female)
* [Connector 6 pin female](https://www.reichelt.de/Platinen-Steckverbinder/PSK-254-6W/3/index.html?ACTION=3&LA=446&ARTICLE=147625&GROUPID=7525&artnr=PSK+254%2F6W)
* [Crimp contacts for female connector](https://www.reichelt.de/Platinen-Steckverbinder/PSK-KONTAKTE/3/index.html?ACTION=3&GROUPID=7525&ARTICLE=14861)
* [iButton Reader for DS1990A with Built-in Bicolor LED](http://www.ebay.de/itm/222324752333)
* n x [iButton DS1990A-F5](http://www.ebay.de/itm/322338610975)
* 5 x [16mm Illuminated Pushbutton - White Momentary](https://www.adafruit.com/product/1479) [[Shop](https://www.exp-tech.de/zubehoer/tasterschalter/6443/16mm-illuminated-pushbutton-white-momentary)]
* [HifiBerry MiniAmp](https://www.hifiberry.com/shop/boards/miniamp/) [[Shop](https://www.reichelt.de/Erweiterungsboards/RPI-HB-MINI-AMP/3/index.html?ACTION=3&GROUPID=6669&ARTICLE=191036)]
* [VISATON SC 4.7 ND - 8 Ohm](http://www.visaton.de/de/produkte/chassiszubehoer/breitband-systeme/sc-47-nd-8-ohm) [[Shop](https://www.reichelt.de/Breitbandlautsprecher/VIS-SC-4-7ND-8/3/index.html?ACTION=3&GROUPID=3579&ARTICLE=36872)]
* [MDF](https://holzladen.shop/mdf/roh/65/mdf-roh?c=56), [acoustic cloth](https://www.akustikstoff.com/Akustikstoff-Standard-in-verschiedenen-Abmessungen/Akustikstoff-Bespannstoff-42-verschiedene-Farben-50-x-30-cm::601.html), handle, screws, paint, washer, cable, ...

## Assembly / Wiring

### Adafruit Powerboost 1000C

The Powerboost is powered via micro USB and requires the included USB A connector to be soldered. Additionally I soldered a (4) pin strip beginning from EN to connect to a piggyback stripboard carrying a KA75330 and a connector to the On/Off switch (see image below).

![KA75330 Wiring](https://raw.githubusercontent.com/aschamberger/pcpLeo/master/img/KA75330.png)

[Info on Powerboost](https://learn.adafruit.com/adafruit-powerboost-1000c-load-share-usb-charge-boost/overview):
*PowerBoost 1000C is the perfect power supply for your portable project! With a built-in load-sharing battery charger circuit, you'll be able to keep your power-hungry project running even while recharging the battery! This little DC/DC boost converter module can be powered by any 3.7V LiIon/LiPoly battery, and convert the battery output to 5.2V DC for running your 5V projects.*

[On/Off Switch and battery monitoring](https://forums.adafruit.com/viewtopic.php?f=19&t=102032&start=45#p633781):  
*I made a very simple circuit to allow for both the low voltage sensor AND an on/off switch to be present, since (I found out the hard way) that the voltage sensor alone will kill a lipo battery in roughly 4-5 days of not being charged because of the voltage sensor's power usage. Wouldn't mind if you/someone added/updated the powerboost page to include this as well, this works great for us. Thanks for the great parts and recommendation. I think the only thing better I could do is create some a latch that when the low voltage alarm tripped, it would stop trying to check the voltage so it wouldn't keep draining the battery until USB is plugged in to charge the battery.*

![Powerboost + KA75330](https://raw.githubusercontent.com/aschamberger/pcpLeo/master/img/voltage-and-off-switch.png)

<sub>Image Source: https://forums.adafruit.com/download/file.php?id=52999</sub>

### HifiBerry MiniAmp

The amp is connected to the Zero W via GPIO and does not require additional power supply (compared to [JustBoom Amp Zero](https://www.justboom.co/product/justboom-amp-zero-phat/)). 

[GPIO usage](https://www.hifiberry.com/build/documentation/gpio-usage-of-hifiberry-boards/):
*GPIOs 18-21 (pins 12, 35, 38 and 40) are used for the sound interface. GPIO16 can be used to mute the power stage. GPIO26 shuts down the power stage. You can’t use these GPIOs for any other purpose.*

Speaker Connectors (from left to right):
* Left +
* Left -
* Right +
* Right -

### 1-Wire iButton reader for DS1990A

The iButton reader has a four pin JST connector for 1-Wire and a two-lead [bi-color LED](https://scienceprog.com/bi-color-led-indication/):
*Two leads bi-color LEDs have two LEDs connected in parallel but in opposite sides. One LEDs anode is connected o another LEDS cathode and other lead same way. So by applying power you will be able to light only one LED. For instance if you connect to microcontroller you will need to use two microcontroller pins to control both LEDs.*

![Two leads bi-color LED](https://raw.githubusercontent.com/aschamberger/pcpLeo/master/img/bicolor_two_lead.png)

<sub>Image Source: https://i0.wp.com/www.scienceprog.com/wp-content/uploads/2007i/bi_color/bicolor_two_lead.PNG?zoom=1.5&resize=188%2C189</sub>

[LED resistor calculation](http://ledcalc.com/#): The LED is 2.7V and with assumed 20mA current it would require a 30 Ohm resistor. I used a 50 Ohm lying around.

The JST connector is connected to the proto board with the LED resistor.

### Adafruit Perma Proto Bonnet Mini Kit

The Proto Bonnet is used to break out the GPIOs for the iButton reader and the push buttons to connectors and add resistors for 1-Wire and the LEDs. I used pre configured isolated jumper wires on the board. The LEDs of the push buttons are connected in parallel to the 2-pin connector.

![ProtoBonnet Wiring](https://raw.githubusercontent.com/aschamberger/pcpLeo/master/img/ProtoBonnet.png)

GPIO Usage:
* Pin07/GPIO04: 1-Wire
* Pin11/GPIO17: LED red
* Pin13/GPIO27: LED green
* Pin22/GPIO25: Button play/pause 
* Pin29/GPIO05: Button track prev
* Pin31/GPIO06: Button track next
* Pin32/GPIO12: Button volume lower 
* Pin33/GPIO13: Button volume raise
* Pin12/GPIO18: HifiBerry sound 
* Pin36/GPIO16: HifiBerry mute 
* Pin35/GPIO19: HifiBerry sound 
* Pin38/GPIO20: HifiBerry sound
* Pin40/GPIO21: HifiBerry sound
* Pin37/GPIO26: HifiBerry off

Raspberry Pi Pinout documentation can be found here:
http://www.pighixxx.com/test/2015/06/raspberry-pi-v2-mod-b-pinout/

## Installation / Configuration

1. [Download piCorePlayer](https://www.picoreplayer.org/how_to_download_pcp.shtml)
1. [Burn piCorePlayer onto a SD card](https://www.picoreplayer.org/how_to_burn_pcp_onto_a_sd_card.shtml)
1. [Setup wifi on piCorePlayer without Ethernet](https://www.picoreplayer.org/how_to_setup_wifi_on_pcp_without_ethernet.shtml)
1. [Access pCP via default hostname "*piCorePlayer*" or determine your piCorePlayer's IP Address](https://www.picoreplayer.org/how_to_determine_your_pcp_ip_address.shtml)
1. [Change pCP operation mode to "*Advanced*"](https://www.picoreplayer.org/how_to_use_pcp_mode_settings.shtml)
1. Configuration changes via web interface
    1. Expand SD card in "*Main Page*" via Button "*Resize FS*"
    1. Install extensions in "*Main Page*" via Button "*Extensions*"
        * from *piCore* repository: *python3.6* + *python-RPi.GPIO*
        * from *piCorePlayer* repository: *w1*
    1. Select proper audio output "*HiFiBerry DAC Zero/MiniAMP*" in "*Squeezelite Settings*"
	1. Change "*Name of your player*" to your desired "*<player_name>*" in "*Squeezelite Settings*"
    1. Set "*Power On/Off GPIO*" to "*16*" and toggle "*Active High*" for muting the MiniAMP in "*Squeezelite Settings*"
    1. Change "*Host name*" to your desired "*<player_name>*" in "*Tweaks*"
1. [Access piCorePlayer via ssh](https://www.picoreplayer.org/how_to_access_pcp_via_ssh.shtml)
1. Configuration changes via console
    1. Add device tree overlay for 1-Wire in *[config.txt](https://www.picoreplayer.org/how_to_edit_config_txt.shtml)*:
        ```
        m1
        c1
        sudo sh -c "sed -i '/#---End-Custom----------------------------------------/i dtoverlay=w1-gpio,gpiopin=4' config.txt"
        ```
    1. Add blacklist entry for *w1-gpio* kernel module in *cmdline.txt* (to prevent loading of *wire* module with [too long] default timing values)
        ```
        m1
        c1
        sudo sh -c "echo –n ' blacklist=w1-gpio' >> /mnt/mmcblk0p1/cmdline.txt"
        ```
    1. Edit *bootlocal.sh* to load required 1-Wire modules (with short [1 sec] timeout/ttl values)
        ```
        c2
        sudo sh -c "echo 'sudo modprobe wire timeout=1 slave_ttl=1' >> /opt/bootlocal.sh"
        sudo sh -c "echo 'sudo modprobe w1-gpio' >> /opt/bootlocal.sh"
        sudo sh -c "echo 'sudo modprobe w1-smem' >> /opt/bootlocal.sh"
        sudo filetool.sh –b
        ```
    1. Download/Install [LMSTools](https://github.com/elParaguayo/LMSTools) (development branch is required as the LMS server discovery function is used)
        ```
        c2
        cd /home/tc 
        mkdir LMSTools
		cd LMSTools
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/__init__.py
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/artworkresolver.py
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/callbackserver.py
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/discovery.py
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/menu.py
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/menuitems.py
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/player.py
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/server.py
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/tags.py
        wget https://raw.githubusercontent.com/elParaguayo/LMSTools/development/LMSTools/utils.py
        sudo filetool.sh -b
        ```
    1. Download/Install *leo.py* script (no configuration is required: LMS server is auto detected and mac id used for player selection)
        ```
        c2
        cd /home/tc 
        wget https://raw.githubusercontent.com/aschamberger/pcpLeo/master/leo.py
        sudo sh -c "echo 'sudo python /home/tc/leo.py&' >> /opt/bootlocal.sh"
        sudo filetool.sh -b
        ```
1. Set up favorites in LMS
    1. add folder "\<player_name>" to favorites
    1. add your music to folder "\<player_name>" and append [\<button_id>] to item name (e.g. "MyPlaylist [01-000000000000]")
