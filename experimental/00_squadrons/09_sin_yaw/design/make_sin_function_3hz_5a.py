
# coding: utf-8
import numpy as np
import pylab as plb
#################
update_freq = 60.
cl_duration = 5.0
ol_duration = 60.0
times = np.linspace(0,ol_duration,update_freq*ol_duration)
o_freq = 0.5 #Hz
amp = 40.0
#################
cycle_half_amp = amp/2.0
ol_fun = -1*np.cos(2*np.pi*times*o_freq)*cycle_half_amp+cycle_half_amp+2
cl_fun = np.zeros(update_freq*cl_duration)
func = np.hstack((cl_fun,ol_fun))

func = func.astype(np.int64)
func = func.astype(np.double)
plb.plot(func,'o-');plb.show()

from scipy import io
io.savemat('./stimulus_data/position_function_sin_%shz_a%s.mat'%(o_freq,amp),{'func':func})

