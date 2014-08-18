import flylib as flb
import neo
import os
import gc
from pylab import *
from numpy import *
import sys

rootdir = sys.argv[1]
#rootdir = '/media/FlyDataB/FlyDB/Fly0193/'
abf_file = filter(lambda x:'.abf' in x,os.listdir(rootdir))[1]
print abf_file
sigs = flb.get_axon_signals(rootdir + abf_file)
gc.collect()
idxs = flb.idx_by_thresh(sigs['DAC2'],thresh = 0)
t_codes = np.array([sigs['DAC2'][x] for x in idxs])
t_vals = around(array([mean(tc) for tc in t_codes])*6)
t_args = argsort(t_vals)
static_test_90 = squeeze(argwhere(t_vals == 10))
static_test_270 = squeeze(argwhere(t_vals == 20))
stripe_test_90 = squeeze(argwhere(t_vals == 30)) 
stripe_test_270 = squeeze(argwhere(t_vals == 40))
opti_test_90 = squeeze(argwhere(t_vals == 50))
opti_test_270 = squeeze(argwhere(t_vals == 60))
lmrs = np.array([sigs['Ph2'][x[:280000]] for x in idxs])
lwings = np.array([sigs['Ph0'][x[:280000]] for x in idxs])
rwings = np.array([sigs['Ph1'][x[:280000]] for x in idxs])
Ypos = np.array([sigs['Ypos'][x[:280000]] for x in idxs])
Xpos = np.array([sigs['Xpos'][x[:280000]] for x in idxs])
ttype = static_test_90
"""
####################
figure()
subplot(3,1,1)
ave = mean(Ypos[ttype],axis=0)
stdev = std(Ypos[ttype],axis=0)
plot(ave,c = 'k')
plot(ave+stdev,c = 'b')
plot(ave-stdev,c = 'b')
i = 2
for ttype in [static_test_90,static_test_270]:
    subplot(3,1,i)
    ave = mean(lwings[ttype],axis=0)
    stdev = std(lwings[ttype],axis=0)
    plot(ave,c = 'k')
    plot(ave+stdev,c = 'b')
    plot(ave-stdev,c = 'b')
    i+=1
    gca().set_ybound(-3,3)
suptitle('static')

##################
figure()
subplot(3,1,1)
ave = mean(Ypos[ttype],axis=0)
stdev = std(Ypos[ttype],axis=0)
plot(ave,c = 'k')
plot(ave+stdev,c = 'b')
plot(ave-stdev,c = 'b')
i = 2
for ttype in [opti_test_90,opti_test_270]:
    subplot(3,1,i)
    ave = mean(lwings[ttype],axis=0)
    stdev = std(lwings[ttype],axis=0)
    plot(ave,c = 'k')
    plot(ave+stdev,c = 'b')
    plot(ave-stdev,c = 'b')
    i+=1
    gca().set_ybound(-3,3)
suptitle('opti')

##################
figure()
subplot(3,1,1)
ave = mean(Ypos[ttype],axis=0)
stdev = std(Ypos[ttype],axis=0)
plot(ave,c = 'k')
plot(ave+stdev,c = 'b')
plot(ave-stdev,c = 'b')
i = 2
for ttype in [stripe_test_90,stripe_test_270]:
    subplot(3,1,i)
    ave = mean(lwings[ttype],axis=0)
    stdev = std(lwings[ttype],axis=0)
    plot(ave,c = 'k')
    plot(ave+stdev,c = 'b')
    plot(ave-stdev,c = 'b')
    i+=1
    gca().set_ybound(-3,3)
suptitle('stripe')
"""

ave_dict_lmr = {'static_test_90':mean(lmrs[static_test_90],axis=0),
            'static_test_270':mean(lmrs[static_test_270],axis=0),
            'stripe_test_90':mean(lmrs[stripe_test_90],axis=0),
            'stripe_test_270':mean(lmrs[stripe_test_270],axis=0),
            'opti_test_90':mean(lmrs[opti_test_90],axis=0),
            'opti_test_270':mean(lmrs[opti_test_270],axis=0)}

ave_dict_lwings = {'static_test_90':mean(lwings[static_test_90],axis=0),
            'static_test_270':mean(lwings[static_test_270],axis=0),
            'stripe_test_90':mean(lwings[stripe_test_90],axis=0),
            'stripe_test_270':mean(lwings[stripe_test_270],axis=0),
            'opti_test_90':mean(lwings[opti_test_90],axis=0),
            'opti_test_270':mean(lwings[opti_test_270],axis=0)}

ave_dict_rwings = {'static_test_90':mean(rwings[static_test_90],axis=0),
            'static_test_270':mean(rwings[static_test_270],axis=0),
            'stripe_test_90':mean(rwings[stripe_test_90],axis=0),
            'stripe_test_270':mean(rwings[stripe_test_270],axis=0),
            'opti_test_90':mean(rwings[opti_test_90],axis=0),
            'opti_test_270':mean(rwings[opti_test_270],axis=0)}



import cPickle
f = open(rootdir + 'T2_trial2_ave_data.cpkl','wb')
cPickle.dump({'lmr':ave_dict_lmr,'lwings':ave_dict_lwings,'rwings':ave_dict_rwings},f)
f.close()