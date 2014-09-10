import panelcom as pc
import time
import numpy as np
from analog_out import *
leds = pc.LEDPanels()
fixation_pattern = 1

pattern_names = ['static_test_yaw_90.mat',
                 'static_test_yaw_270.mat']

trial_condition_ao = 0
phase_signal_ao = 1
#Closed loop
def led_closed_loop():
	leds.panel_com('stop');
	leds.panel_com('set_pattern_id',fixation_pattern)
	leds.panel_com('set_mode',1, 1)
	leds.panel_com('set_velfunc_id',0, 0)
	leds.panel_com('send_gain_bias',-100,0,0,0)
	leds.panel_com('set_position',48, 0)
	leds.panel_com('start')

def led_open_loop(pattern_id,function_id):
	leds.panel_com('stop');
	leds.panel_com('set_pattern_id',pattern_id)
	leds.panel_com('set_mode',1, 4)#closed loop on x, open loop on y
	leds.panel_com('set_posfunc_id',2,function_id)
	leds.panel_com('send_gain_bias',-100,0,0,0)
	leds.panel_com('set_position',48, 0)
	leds.panel_com('set_funcy_freq', 60)
	leds.panel_com('start')

analog.setVoltage(trial_condition_ao, -1)
analog.setVoltage(phase_signal_ao, 4)
led_closed_loop()
time.sleep(20)

#analog.setVoltage(trial_condition_ao, 1)

for rep in range(10):
	print('rep#%s'%(rep))
	for condition in np.random.permutation([2]):
		print ('running pattern:%s'%(pattern_names[condition-2]))
		led_closed_loop()
		time.sleep(5)
		led_open_loop(condition,1)
		analog.setVoltage(trial_condition_ao, condition)
		time.sleep(25.0)
		analog.setVoltage(trial_condition_ao, -1)
led_closed_loop()

try:
    analog.closePhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)