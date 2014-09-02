import panelcom as pc
import time
import numpy as np
from analog_out import *
        
leds = pc.LEDPanels()
#leds.panel_com('set_pattern_id',2)
flynum = 169;
#datestr = '20140605'
#rootdir = strcat('G:\FlyDB','\Fly',num2str(flynum,'%04d'))
#exp_label = 'pitch_yaw_aperture_test';
#datafilename = strcat(rootdir,'\fly',num2str(flynum,'%04d'),'_', exp_label);
one_volt = (32766-200)/10;
num_reps = 10;

#np.random.shuffle(phase_levels)
pattern_names = ['static_test_yaw_90.mat','static_test_yaw_270.mat']

fixation_pattern = 1;
num_starfield_patterns = len(pattern_names)
starfield_pattern = 2;
volts_per_pat = 10/num_starfield_patterns;
open_loop_update_freq = 60;

#pattern params needed to set the laser trigger
#pixels in actual pattern
#azmuth_pix = 8*12;
#gs_val = 3;
#x_num = azmuth_pix*(2^gs_val);#same as image Azm
#DegPerXstp = 360/x_num;
#ThreshAngle = 40;
#threshX = floor(DegPerXstp*ThreshAngle);

#Closed loop
leds.panel_com('stop');
#leds.panel_com('set_AO',3 int16(one_volt*-1))
leds.panel_com('laser_off');
leds.panel_com('set_pattern_id',fixation_pattern)
leds.panel_com('set_mode',1, 1)#pause(0.05); ##set closed loop X closed loop Y
leds.panel_com('set_velfunc_id',0, 0)#pause(0.01); ##use default function on x and y channel (is this nessessary?)
leds.panel_com('send_gain_bias',-100,0,0,0)#pause(0.005);#
leds.panel_com('set_position',48, 1)#pause(0.005); # start at close to fixation
#leds.panel_com('set_AO',3, int(one_volt*-1))
#leds.panel_com('set_AO',[4 int(one_volt*0.1)) #phase level
leds.panel_com('start');
time.sleep(2);

record_index = 1;
#Panel_com('send_laser_pattern' ,ones(1,96)]);
#Panel_com('set_funcx_freq', open_loop_update_freq)

phase_levels = np.linspace(0.1,10,10/0.5)
for phase_idx in np.random.permutation(len(phase_levels)):
    phase_level = phase_levels[phase_idx]
    for pattern_idx in np.random.permutation(num_starfield_patterns):
        starfield_pattern = pattern_idx+2;
        open_loop_function = 1;
        #datarecord(record_index).open_loop_function = open_loop_function;
        #datarecord(record_index).starfield_name = pattern_names{i(1)};
        #datarecord(record_index).start_time = now;
        #disp(datarecord(record_index).starfield_name)
        
        #%% Closed loop
        leds.panel_com('stop')#;pause(0.001);
        leds.panel_com('laser_off');
        leds.panel_com('set_pattern_id',fixation_pattern)#;pause(0.001) #stripe fixation pattern
        leds.panel_com('set_mode',1, 1)#;pause(0.001) #set closed loop X open loop Y
        leds.panel_com('set_velfunc_id',0, 0)#;pause(0.001) #use default function on x and y channel (is this nessessary?)
        leds.panel_com('send_gain_bias',-100,0,0,0)#;pause(0.001)#
        leds.panel_com('set_position',48, 0)#;pause(0.001) # start at close to fixation
        #Panel_com('set_AO',3,int(one_volt*-1)])
        #Panel_com('set_AO',4, int(one_volt*phase_level)) #phase level
        leds.panel_com('start')
        analog.setVoltage(0, -1)
        analog.setVoltage(1, phase_level)
        time.sleep(5);
        
        #%disp('here')
        #%% Start starfield
        leds.panel_com('stop')#pause(0.001)
        #%Panel_com('set_AO',[3 int16(one_volt*volts_per_pat*i(1))]);pause(0.001)
        leds.panel_com('set_pattern_id',starfield_pattern)#pause(0.001); #set to expansion pattern 
        leds.panel_com('set_position',1, 1)#;pause(0.001)# #set the x position at begining y posistion is an exp parameter
        leds.panel_com('set_mode',1, 4)#;pause(0.001); #set the x mode to function based position control mode
        leds.panel_com('send_gain_bias',-50,0,0,0)#pause(0.001); #set the gain and bias to zero for both X and Y
        leds.panel_com('set_posfunc_id',2, open_loop_function)#pause(0.001); #position function to run on channel 2 (y)
        leds.panel_com('set_funcx_freq', 60)#pause(0.001);
        leds.panel_com('start')
        analog.setVoltage(0, volts_per_pat*pattern_idx)
        time.sleep(3.1);

        #record_index = record_index+1

##%% Put the fly back into closed loop.
leds.panel_com('stop')#;pause(0.005);
#%Panel_com('set_AO',[3 int16(one_volt*-1)])
#leds.panel_com('laser_off');
leds.panel_com('set_pattern_id',fixation_pattern)#;pause(0.005); #stripe fixation pattern
leds.panel_com('set_mode',1,1)#;pause(0.05); #set closed loop X closed loop Y
leds.panel_com('set_velfunc_id',0, 0)#;pause(0.01); #use default function on x and y channel (is this nessessary?)
leds.panel_com('send_gain_bias',-50,0,0,0)#;pause(0.005);#
leds.panel_com('set_position',48, 0)#;pause(0.005); # start at close to fixation
leds.panel_com('start');
time.sleep(10);

#save(datafilename,'exp_label', 'datarecord');
try:
    analog.closePhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)