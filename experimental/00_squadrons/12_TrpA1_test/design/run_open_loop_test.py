import panelcom as pc
import time
import numpy as np
import os

from analog_out import *

leds = pc.LEDPanels()
fixation_pattern = 1

if np.sum(['.abf' in x for x in os.listdir('E:\\FlyDB\\' + os.listdir('E:\\FlyDB')[-1])]):
    newdir = 'Fly%04d'%(int(os.listdir('E:\\FlyDB')[-1].split('Fly')[-1])+1)
    print 'making:' + newdir
    os.mkdir('E:\\FlyDB\\'+newdir)
else:
	newdir = 'Fly%04d'%(int(os.listdir('E:\\FlyDB')[-1].split('Fly')[-1]))

pattern_names = ['static_test_roll_90.mat',
                 'static_test_roll_270.mat',
                 'static_test_yaw_90.mat',
                 'static_test_yaw_270.mat']

trial_condition_ao = 0
phase_signal_ao = 1

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

#start with closed loop stripe fixation
analog.setVoltage(trial_condition_ao, -1)
analog.setVoltage(phase_signal_ao, 4)
led_closed_loop()
time.sleep(20)

#run open loop paterns
for rep in range(10):
	condition_list = np.random.permutation([2,3,4,5])
	for condition in condition_list:
		print ('running pattern:%s'%(pattern_names[condition-2]))
		led_closed_loop()
		time.sleep(5)
		led_open_loop(condition,1)
		analog.setVoltage(trial_condition_ao, condition-1)
		time.sleep(3.0)
		analog.setVoltage(trial_condition_ao, -1)
	led_closed_loop()

f = open('E:\\FlyDB\\'+newdir + '\\run_data.txt','wt')
f.writelines([pattern_names[condition_number-2] + '\n' for condition_number in condition_list])
f.close()

try:
    analog.closePhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)