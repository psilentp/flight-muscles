# coding: utf-8
import numpy as np
import pylab as plb
from scipy import io
#################
trial_duration = 3.0

params = {	'updates_per_sec': 60.,
			'epoch_duration': 6.0,
			'deg_per_pix': 360/96.0,
			'cycles_per_sec': 1.0,
			'deg_per_cycle': 30}

def temp_freq_ramp(start_pos = 0,
                   updates_per_sec = 60.,
                   epoch_duration = 6.0,
                   deg_per_pix = 360/96.0,
                   cycles_per_sec = 10.0,
                   deg_per_cycle = 30,
                   direction = 'positive'):
    deg_per_sec = deg_per_cycle * cycles_per_sec
    pix_per_sec = deg_per_sec/deg_per_pix
    pix_per_update = pix_per_sec / updates_per_sec
    times = np.linspace(0,epoch_duration,updates_per_sec*epoch_duration)
    if direction == 'positive':
        func = (np.arange(0,len(times))*pix_per_update)+start_pos
    elif direction == 'negative':
        func = (np.arange(0,len(times))*pix_per_update*-1)+start_pos
    return(func)

#################
for epoch0_duration in [0,0.250,0.50,1.0]:
	if epoch0_duration > 0:
		params.update({'start_pos':0,
					   'epoch_duration':epoch0_duration,
					   'direction':'positive'})
		epoch0 = temp_freq_ramp(**params)
		params.update({'start_pos':epoch0[-1],
					   'epoch_duration':trial_duration - epoch0_duration,
					   'direction':'negative'})
		epoch1 = temp_freq_ramp(**params)
		func = np.hstack((epoch0[:-1],epoch1))
	else:
		params.update({'start_pos':0,
					   'epoch_duration':trial_duration,
					   'direction':'negative'})
		func = temp_freq_ramp(**params)
	func += np.abs(np.min(func)) + 1
	io.savemat('./stimulus_data/position_function_%ss.mat'%(epoch0_duration),{'func':func})



