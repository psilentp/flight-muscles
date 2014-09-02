import panelcom as pc
import time
import numpy as np
from analog_out import *
leds = pc.LEDPanels()
fixation_pattern = 1

#Closed loop
leds.panel_com('stop');
leds.panel_com('laser_off');
leds.panel_com('set_pattern_id',fixation_pattern)
leds.panel_com('set_mode',1, 1)#pause(0.05); ##set closed loop X closed loop Y
leds.panel_com('set_velfunc_id',0, 0)#pause(0.01); ##use default function on x and y channel (is this nessessary?)
leds.panel_com('send_gain_bias',-100,0,0,0)#pause(0.005);#
leds.panel_com('set_position',48, 0)#pause(0.005); # start at close to fixation
leds.panel_com('start');
analog.setVoltage(0, -1)
analog.setVoltage(1, 0.5)
time.sleep(30);
analog.setVoltage(0, 1)

for cycle in range(20):
    print cycle
    for phase_level in np.linspace(0.5,10,50):
        analog.setVoltage(1, phase_level)
        time.sleep(0.05)

try:
    analog.closePhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)