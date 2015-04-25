import panelcom as pc
import time
import numpy as np
import os

from analog_out import *

leds = pc.LEDPanels()
fixation_pattern = 1
trial_condition_ao = 0
phase_signal_ao = 1

vel_range = [1]
dir_range = [('pth_roll_%s'%p,1+9*i*30.0/360.) for i,p in enumerate(range(0,360,30))]
rep_range = range(4)

#run open loop paterns
#trials = np.array([[[(z,y,x) for x in rep_range] for y in vel_range] for z in dir_range])
#trials = np.reshape(trials,(30,3))

#check to see if we need to make a new directory for a new fly
#if np.sum(['.abf' in x for x in os.listdir('E:\\FlyDB\\' + os.listdir('E:\\FlyDB')[-1])]):
#    newdir = 'Fly%04d'%(int(os.listdir('E:\\FlyDB')[-1].split('Fly')[-1])+1)
#    print 'making:' + newdir
#    os.mkdir('E:\\FlyDB\\'+newdir)
#else:
#	newdir = 'Fly%04d'%(int(os.listdir('E:\\FlyDB')[-1].split('Fly')[-1]))

#create a dictionary of pattern names
pattern_data = dict()
count = 2 #pattern_names[0] is fixation
for direction,direction_voltage in dir_range:
    for vel in vel_range:
        for rep in rep_range:
            pattern_data['step_%s_v%s_rep%s'%(direction,vel,rep)] = dict()
            pattern_data['step_%s_v%s_rep%s'%(direction,vel,rep)]['condition_tuple'] = (direction,
                                                                                            vel,
                                                                                            rep)
            pattern_data['step_%s_v%s_rep%s'%(direction,vel,rep)]['pattern_index'] = count
            pattern_data['step_%s_v%s_rep%s'%(direction,vel,rep)]['condition_voltage'] = direction_voltage
            #pattern_data['step_%s_v%s_rep%s'%(direction,vel,rep)]['condition_voltage'] = encode_condition(count)
            count += 1

#def encode_condition(idx):
#    ntrials = len(pattern_data.keys())#len(vel_range)*len(dir_range)*len(rep_range)
#    return ((idx)/float(ntrials+1)*10)

#for trial in pattern_data.values():
#    trial['condition_voltage'] = encode_condition(trial['pattern_index'])

trials = [t['condition_tuple'] for t in pattern_data.values() if not(t['condition_tuple'][1] == 10)]

#for x in pattern_data.values():
#    print x['pattern_index'],x['condition_voltage']

def led_closed_loop(cl_duration = 3.0):
    analog.setVoltage(trial_condition_ao, -1.0)
    leds.panel_com('stop');
    leds.panel_com('set_pattern_id',fixation_pattern)
    leds.panel_com('set_mode',1, 1)
    leds.panel_com('set_velfunc_id',0, 0)
    leds.panel_com('send_gain_bias',-100,0,0,0)
    leds.panel_com('set_position',48, 0)
    leds.panel_com('start')
    time.sleep(cl_duration)

def led_open_loop(pattern_id = 0,
                  function_id = 0,
                  static_duration = 1,
                  motion_duration = 1,
                  condition_voltage = 0):
	#static patern
    analog.setVoltage(trial_condition_ao, 0)
    #time.sleep(0.001)
    #analog.setVoltage(1, 1) #protocol sync
    leds.panel_com('stop');
    leds.panel_com('set_pattern_id',pattern_id)
    leds.panel_com('set_mode',0, 0)#open loop on x, open loop on y
    leds.panel_com('send_gain_bias',0,0,0,0)
    leds.panel_com('set_funcy_freq', 60)
    leds.panel_com('start')
    time.sleep(static_duration)

    #motion patern
    leds.panel_com('stop');
    leds.panel_com('set_mode',0, 0)#open loop on x, open loop on y
    leds.panel_com('set_velfunc_id',1,0)
    leds.panel_com('send_gain_bias',60,0,0,0)
    leds.panel_com('start')
    analog.setVoltage(trial_condition_ao, condition_voltage)
    time.sleep(motion_duration)

    #static patern
    analog.setVoltage(trial_condition_ao, 0)
    #time.sleep(0.001)
    #analog.setVoltage(0, 1) #protocol sync
    leds.panel_com('stop');
    leds.panel_com('set_mode',0, 0)#closed loop on x, open loop on y
    leds.panel_com('send_gain_bias',0,0,0,0)
    leds.panel_com('set_funcy_freq', 60)
    leds.panel_com('start')
    time.sleep(static_duration)
    

#start with closed loop stripe fixation
analog.setVoltage(trial_condition_ao, -1)
analog.setVoltage(phase_signal_ao, 4)
#led_closed_loop(cl_duration = 1.0)
led_closed_loop(cl_duration = 90.0)


#condition_list = np.random.permutation(trials)
count = 0
for rep in [0,1]:
    condition_list = np.random.permutation(trials)
    for condition in condition_list:
        pattern_name = 'step_%s_v%s_rep%s'%(condition[0],condition[1],condition[2])
        print ('running pattern:%s'%(pattern_name))
        print count
        count += 1
        pattern_id = pattern_data[pattern_name]['pattern_index']
        condition_voltage = pattern_data[pattern_name]['condition_voltage']
        led_closed_loop(cl_duration = 5.0)
        #led_open_loop(pattern_id = pattern_id,
        #              function_id = 1,
        #              static_duration = 10,
        #              motion_duration = 3,
        #              condition_voltage = condition_voltage)
        led_open_loop(pattern_id = pattern_id,
                      function_id = 1,
                      static_duration = 7,
                      motion_duration = 3,
                      condition_voltage = condition_voltage)

led_closed_loop(cl_duration = 5.0)
led_closed_loop(cl_duration = 5.0)
#f = open('E:\\FlyDB\\'+newdir + '\\run_data.txt','wt')
#f.writelines(['step_yaw_%s_v%s_rep%s'%(condition[0],condition[1],condition[2]) + '\n' for condition in condition_list])
#f.close()

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
 ]
"""