import panelcom as pc
import time
import numpy as np
import os

from analog_out import *
test_code = False # loop through without actually running trials
print not(test_code)
#save the info needed to recover the vesion of this file from the git repo
git_SHA = os.popen('git rev-parse HEAD').read()
script_path = os.path.dirname(os.path.realpath(sys.argv[0]))

leds = pc.LEDPanels()
fixation_pattern = 1
trial_condition_ao = 0
phase_signal_ao = 1

from scipy import io
SDMat = io.loadmat('SD.mat')
SDData = np.squeeze(SDMat['SD'])
pnames = [pname[0] for pname in SDMat['SD']['pattern'][0][0]['pattNames'][0][0][0]]
volts_per_pattern = 10.0/(len(pnames)-1) # minus 1 because of stripe pattern

pattern_data = [{'index':i+1,'condition_voltage':i*volts_per_pattern,'pattern_name':pname} for 
                i,pname in enumerate(pnames)] 

if pattern_data[0]['pattern_name'] == 'Pattern_fixation_4_wide_4X12_Pan':
    pattern_data[0]['condition_voltage'] = -1

# functions that will execute a trial
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
    leds.panel_com('stop');
    leds.panel_com('set_mode',0, 0)#closed loop on x, open loop on y
    leds.panel_com('send_gain_bias',0,0,0,0)
    leds.panel_com('set_funcy_freq', 60)
    leds.panel_com('start')
    time.sleep(static_duration)
    
nreps = 2
setup_closed_loop_duration = 90
static_duration = 7
motion_duration = 3
cl_duration = 5.0
imaging_frame_duration = 0.021

trial_duration = (cl_duration+static_duration+motion_duration+static_duration)
total_duration = setup_closed_loop_duration + nreps*len(pattern_data[1:])*trial_duration

print('total sequence duration = %ss (%smin)'%(total_duration,total_duration/60.0))
print('allocate more than %s frames'%(int(total_duration/imaging_frame_duration)))

#start with closed loop stripe fixation
analog.setVoltage(trial_condition_ao, -1)
analog.setVoltage(phase_signal_ao, 4)
if not(test_code):
    led_closed_loop(cl_duration = 1.0)
    led_closed_loop(cl_duration = setup_closed_loop_duration)

#save a list of the trials that are run
executed_trials = list()
count = 0

# run through the randomized trials
for rep in range(0,nreps):
    condition_list = np.random.permutation(pattern_data[1:])
    for condition in condition_list:
        pattern_name = condition['pattern_name']
        print ('running pattern:%s'%(pattern_name))
        print count
        count += 1
        pattern_id = condition['index']
        condition_voltage = condition['condition_voltage']
        executed_trials.append(condition)
        if not(test_code):
            led_closed_loop(cl_duration = 5.0)
            led_open_loop(pattern_id = pattern_id,
                          function_id = 1,
                          static_duration = static_duration,
                          motion_duration = motion_duration,
                          condition_voltage = condition_voltage)

if not(test_code):
    led_closed_loop(cl_duration = 5.0)
    led_closed_loop(cl_duration = 5.0)

import cPickle 
f = open('trial_data.cpkl','wb')
cPickle.dump(executed_trials,f)
f.close()

import cPickle 
f = open('experiment_script.cpkl','wb')
cPickle.dump({'script_path':script_path,'git_SHA':git_SHA},f)
f.close()

try:
    analog.closePhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)