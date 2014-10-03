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

pattern_names = dict()
count = 1
for i in range(1,12,3):
    for rep in range(5):
        pattern_names['step_yaw_90_v%s_rep%s'%(i,rep)] = count
        count += 1
for i in range(1,12,3):
    for rep in range(5):
        pattern_names['step_yaw_270_v%s_rep%s'%(i,rep)] = count
        count += 1

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
	leds.panel_com('set_mode',0, 0)#closed loop on x, open loop on y
	leds.panel_com('set_posfunc_id',1,function_id)
	leds.panel_com('send_gain_bias',10,20,0,0)
	leds.panel_com('set_position',0,0)
	leds.panel_com('set_funcy_freq', 60)
	leds.panel_com('start')

#start with closed loop stripe fixation
analog.setVoltage(trial_condition_ao, -1)
analog.setVoltage(phase_signal_ao, 4)
led_closed_loop()
time.sleep(1)

#run open loop paterns
trials = np.array([[[(z,y,x) for x in range(5)] for y in [1,4,7]] for z in [90,270]])
trials = np.reshape(trials,(30,3))

condition_list = np.random.permutation(trials)

for condition in condition_list:
	print condition
	pattern_name = 'step_yaw_%s_v%s_rep%s'%(condition[0],condition[1],condition[2])
	print ('running pattern:%s'%(pattern_name))
	pattern_id = pattern_names[pattern_name]
	print pattern_id
	led_closed_loop()
	time.sleep(5.0)
	led_open_loop(pattern_id+1,0)
	analog.setVoltage(trial_condition_ao, (pattern_id+1)/30)
	time.sleep(4.0)
	analog.setVoltage(trial_condition_ao, -1)

led_closed_loop()

f = open('E:\\FlyDB\\'+newdir + '\\run_data.txt','wt')
f.writelines(['step_yaw_%s_v%s_rep%s'%(condition[0],condition[1],condition[2]) + '\n' for condition in condition_list])
f.close()

try:
    analog.closePhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

#load the patterns on the disk in this order
"""
['step_yaw_90_v1_rep0',
 'step_yaw_90_v1_rep1',
 'step_yaw_90_v1_rep2',
 'step_yaw_90_v1_rep3',
 'step_yaw_90_v1_rep4',
 'step_yaw_90_v4_rep0',
 'step_yaw_90_v4_rep1',
 'step_yaw_90_v4_rep2',
 'step_yaw_90_v4_rep3',
 'step_yaw_90_v4_rep4',
 'step_yaw_90_v7_rep0',
 'step_yaw_90_v7_rep1',
 'step_yaw_90_v7_rep2',
 'step_yaw_90_v7_rep3',
 'step_yaw_90_v7_rep4',
 'step_yaw_90_v10_rep0',
 'step_yaw_90_v10_rep1',
 'step_yaw_90_v10_rep2',
 'step_yaw_90_v10_rep3',
 'step_yaw_90_v10_rep4',
 'step_yaw_270_v1_rep0',
 'step_yaw_270_v1_rep1',
 'step_yaw_270_v1_rep2',
 'step_yaw_270_v1_rep3',
 'step_yaw_270_v1_rep4',
 'step_yaw_270_v4_rep0',
 'step_yaw_270_v4_rep1',
 'step_yaw_270_v4_rep2',
 'step_yaw_270_v4_rep3',
 'step_yaw_270_v4_rep4',
 'step_yaw_270_v7_rep0',
 'step_yaw_270_v7_rep1',
 'step_yaw_270_v7_rep2',
 'step_yaw_270_v7_rep3',
 'step_yaw_270_v7_rep4',
 'step_yaw_270_v10_rep0',
 'step_yaw_270_v10_rep1',
 'step_yaw_270_v10_rep2',
 'step_yaw_270_v10_rep3',
 'step_yaw_270_v10_rep4']
"""