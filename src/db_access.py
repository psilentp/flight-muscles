# -*- coding: utf-8 -*- # <nbformat>3.0</nbformat>

import sys
import json
import os
import numpy as np
import h5py

#import json
#param_file = open('params.json','rb')
#params = json.load(param_file)

from parameters import params
root_dir = params['platform_paths'][sys.platform] + params['root_dir']
#root_dir = '/Volumes/FlyDataB/FlyDB/'
from group_meta_data import *
 
class FlyDB(dict):
    def __init__(self,root_dir):
        dict.__init__(self)
        self.root_dir = root_dir

    def create_group(self,flynum):
        self[flynum] = h5py.File(self.root_dir+'Fly%04d'%(int(flynum))+'/fly_record.hdf5','w')

    def close(self):
        for key in self.keys():
            self[key].close()
            print self[key]

    def flush(self):
        for key in self.keys():
            self[key].flush()

def main():
    import cPickle
    fn = 'fly_db_init.cpkl'
    f = open(fn,'wb')
    cPickle.dump(fly_db,f)
    f.close()

###In order to work while data is being uploaded    
hold_flies = [500,501,502]
def get_db():
    #fly_db = h5py.File('/Volumes/FlyDataB/FlyDB/flydb.hdf5','a')
    flydirs = filter(lambda s:'Fly' in s,os.listdir(root_dir))
    initialized_flies = filter(lambda s:'fly_record.hdf5' in os.listdir(root_dir+'/'+s),flydirs)
    fly_db = FlyDB(root_dir)
    for fly in initialized_flies:
        flynum = int(fly.split('Fly')[1])
        #print flynum
        if not(flynum in hold_flies):
            fly_db[flynum] = h5py.File(root_dir+fly+'/fly_record.hdf5','a')
    return fly_db

class FlySwitch(dict):
    def __getitem__(self,flynum):
        return self.__getattribute__('initfly_'+str(flynum))(flynum)

class InitDB(FlySwitch):
    #fly_db = h5py.File("/Volumes/FlyDataB/FlyDB/flydb.hdf5", "w")
    def __init__(self):
        self.fly_db = FlyDB(root_dir)

    def init_all(self):
        import inspect
        initfuncts = filter(lambda t:'initfly' in t[0],inspect.getmembers(self))
        flynums = [int(x[0].split('initfly_')[1]) for x in initfuncts]

    def initfly_111(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [1,2,3,4,5,6]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly01_lr_blob_expansion_14401000.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140401']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140401_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'l'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_112(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [7,8,9,10,11,12]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly02_lr_blob_expansion_14401002.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140401']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140401_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'l'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_114(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [13,14,15,16,17,18]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly04_lr_blob_expansion_14401012.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140401']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140401_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'l'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_115(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [1,2,3,4,5,6]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly01_lr_blob_expansion_14402001.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140402']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140402_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'l'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_116(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [1,2,3,4,5,6]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly01_lr_blob_expansion_14410000.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140410']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140410_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'l'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_117(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [7,8,9,10,11,12]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly02_lr_blob_expansion_14410002.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140410']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140410_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'l'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_118(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [13,14,15,16,17]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly03_lr_blob_expansion_14410003.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140410']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140410_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'l'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_122(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [1,2,3,4,5,6]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly01_lr_blob_expansion_14428000.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140428']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140428_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'r'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_123(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [7,8,9,10,11]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly02_lr_blob_expansion_14428001.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140428']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140428_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'r'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_124(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [2,3,4,5,6]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly01_lr_blob_expansion_14429001.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140429']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140429_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'r'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_125(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [7,8,9,10,11,12]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly02_lr_blob_expansion_14429004.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140429']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140429_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'b1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'r'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_130(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('lr_blob_expansion')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['lr_blob_expansion']['photron_seq_nums'] = [1,2,3,4,5,6]
        fly_record['experiments']['lr_blob_expansion']['axon_file_names'] = ['fly01_lr_blob_expansion_14506005.abf']
        fly_record['experiments']['lr_blob_expansion']['photron_date_string'] = ['20140506']
        fly_record['experiments']['lr_blob_expansion']['kine_filename'] = ['WBkin.mat']
        fly_record['experiments']['lr_blob_expansion']['solution_format_string'] = ['20140506_S%04d/']
        fly_record['experiments']['lr_blob_expansion']['photron_frame_rate_Hz'] = 6000
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_volts'] = np.linspace(1,10,12)
        fly_record['experiments']['lr_blob_expansion']['Ypos_trial_vals'] = np.concatenate(([np.nan],np.arange(0,12)*30))
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_ID'] = 'i1'
        fly_record['experiments']['lr_blob_expansion']['AMsysCh1_side'] = 'r'
        fly_record['experiments']['lr_blob_expansion'].create_group('sequences')

    def initfly_151(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0151_rotating_starfield_imaging_T2_trial_1_14529002.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/trial1/trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_153(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0153_rotating_starfield_imaging_T2_trial_1_14530005.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_154(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0154_rotating_starfield_imaging_T2_trial_1_14530007.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_155(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0155_rotating_starfield_imaging_T2_trial_1_14530009.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_156(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0156_rotating_starfield_imaging_T2_trial_1_14530011.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_157(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0157_rotating_starfield_imaging_T2_trial_1_14602000.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_158(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0158_rotating_starfield_imaging_T2_trial_1_14602002.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_159(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0159_rotating_starfield_imaging_T2_trial_1_14602004.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_160(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0160_rotating_starfield_imaging_T2_trial_1_14602007.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_161(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0161_rotating_starfield_imaging_T2_trial_1_14603000.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_162(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0162_rotating_starfield_imaging_T2_trial_1_14603003.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_163(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0163_rotating_starfield_imaging_T2_trial_1_14603009.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_164(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0164_rotating_starfield_imaging_T2_trial_1_14603012.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_165(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0165_rotating_starfield_imaging_T2_trial_1_14603017.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_166(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0166_rotating_starfield_imaging_T2_trial_1_14605000.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_167(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0167_rotating_starfield_imaging_T2_trial_1_14605001.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_168(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0168_rotating_starfield_imaging_T2_trial_1_14605002.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_169(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0169_rotating_starfield_imaging_T2_trial_1_14605004.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

#### Imaging #######################

    def initfly_170(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0170_rotating_starfield_imaging_T2_trial_1_14605004.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_171(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0171_rotating_starfield_imaging_T2_trial_1_14605004.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_172(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0172_rotating_starfield_imaging_T2_trial_1_14605004.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_173(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0173_rotating_starfield_imaging_T2_trial_1_14605004.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_174(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0174_rotating_starfield_imaging_T2_trial_1_14605004.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_175(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfield_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfield_t2_rep1']['axon_file_names'] = ['fly0175_rotating_starfield_imaging_T2_trial_1_14605004.abf']
        fly_record['experiments']['img_starfield_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfield_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
        fly_record['experiments']['img_starfield_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfield_t2_rep1']['ol_epoch_duration'] = 4.5
        fly_record['experiments']['img_starfield_t2_rep1'].create_group('sequences')

    def initfly_176(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfields2_t2_rep1')
        fly_record['experiments']['img_starfields2_t2_rep1']['axon_file_names'] = ['T2_trial1_14630005.abf']
        fly_record['experiments']['img_starfields2_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep1']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep1'].create_group('sequences')
        fly_record['experiments'].create_group('img_starfields2_t2_rep2')
        fly_record['experiments']['img_starfields2_t2_rep2']['axon_file_names'] = ['T2_trial2_14630008.abf']
        fly_record['experiments']['img_starfields2_t2_rep2']['tiff_file_names'] = ['/T2_trial2/T2_trial2_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep2']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep2']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep2']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep2'].create_group('sequences')

    def initfly_177(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfields2_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfields2_t2_rep1']['axon_file_names'] = ['T2_trial1_14630009.abf']
        fly_record['experiments']['img_starfields2_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep1']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep1'].create_group('sequences')
        fly_record['experiments'].create_group('img_starfields2_t2_rep2')
        fly_record['experiments']['img_starfields2_t2_rep2']['axon_file_names'] = ['T2_trial2_14630010.abf']
        fly_record['experiments']['img_starfields2_t2_rep2']['tiff_file_names'] = ['/T2_trial2/T2_trial2_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep2']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep2']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep2']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep2'].create_group('sequences')

    def initfly_178(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfields2_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfields2_t2_rep1']['axon_file_names'] = ['T2_trial1_14630014.abf']
        fly_record['experiments']['img_starfields2_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep1']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep1'].create_group('sequences')
        fly_record['experiments'].create_group('img_starfields2_t2_rep2')
        fly_record['experiments']['img_starfields2_t2_rep2']['axon_file_names'] = ['T2_trial2_14630016.abf']
        fly_record['experiments']['img_starfields2_t2_rep2']['tiff_file_names'] = ['/T2_trial2/T2_trial2_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep2']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep2']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep2']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep2'].create_group('sequences')

    def initfly_179(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfields2_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfields2_t2_rep1']['axon_file_names'] = ['T2_trial1_14701000.abf']
        fly_record['experiments']['img_starfields2_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep1']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep1'].create_group('sequences')
        fly_record['experiments'].create_group('img_starfields2_t2_rep2')
        fly_record['experiments']['img_starfields2_t2_rep2']['axon_file_names'] = ['T2_trial2_14701001.abf']
        fly_record['experiments']['img_starfields2_t2_rep2']['tiff_file_names'] = ['/T2_trial2/T2_trial2_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep2']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep2']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep2']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep2'].create_group('sequences')

    def initfly_180(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfields2_t2_rep1')
        fly_record['experiments']['img_starfields2_t2_rep1']['axon_file_names'] = ['T2_trial1_14701006.abf']
        fly_record['experiments']['img_starfields2_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep1']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep1'].create_group('sequences')
        fly_record['experiments'].create_group('img_starfields2_t2_rep2')
        fly_record['experiments']['img_starfields2_t2_rep2']['axon_file_names'] = ['T2_trial2_14701008.abf']
        fly_record['experiments']['img_starfields2_t2_rep2']['tiff_file_names'] = ['/T2_trial2/T2_trial2_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep2']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep2']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep2']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep2'].create_group('sequences')
    
    def initfly_181(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_starfields2_t2_rep1')
        #fly_record['experiments'].create_group('b1_azm_expansion_tuning')
        fly_record['experiments']['img_starfields2_t2_rep1']['axon_file_names'] = ['T2_trial1_14701009.abf']
        fly_record['experiments']['img_starfields2_t2_rep1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep1']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep1']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep1']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep1'].create_group('sequences')
        fly_record['experiments'].create_group('img_starfields2_t2_rep2')
        fly_record['experiments']['img_starfields2_t2_rep2']['axon_file_names'] = ['T2_trial2_14701010.abf']
        fly_record['experiments']['img_starfields2_t2_rep2']['tiff_file_names'] = ['/T2_trial2/T2_trial2_MMStack.ome.tif']
        fly_record['experiments']['img_starfields2_t2_rep2']['sequence_pattern_names'] = starfield_pattern_names_6_29_2014
        fly_record['experiments']['img_starfields2_t2_rep2']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_starfields2_t2_rep2']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_starfields2_t2_rep2'].create_group('sequences')

    def initfly_182(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14804016.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')

    def initfly_183(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14804017.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')

    def initfly_184(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14804018.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')

    def initfly_185(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14805002.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')
####
    def initfly_186(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14805003.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')

    def initfly_187(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14805005.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')
    
    def initfly_188(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14806000.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')

    def initfly_189(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14806001.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton']['experiment_start_time'] = 20.0
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')

    def initfly_190(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14806001.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')

    def initfly_191(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14807000.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial2_14807001.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')

    def initfly_192(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14807003.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial2_14807004.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')

    def initfly_193(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14807005.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial2_14807006.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')

    def initfly_194(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14807006.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial2_14807007.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')

    def initfly_195(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14807008.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial2_14807009.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')

    def initfly_196(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14808000.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial2_14808003.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')

    def initfly_197(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lighton')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14808004.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial2_14808005.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')

    def initfly_198(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial1_14812000.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')

    def initfly_199(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lighton']['axon_file_names'] = ['T2_trial1_14812002.abf']
        fly_record['experiments']['img_pattern_test_t2_lighton']['sequence_pattern_names'] = test_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lighton']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lighton']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lighton'].create_group('sequences')

    def initfly_200(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial1_14819000.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')    
    
    def initfly_201(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial1_14819001.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')

    def initfly_202(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial1_14819002.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')    

    def initfly_203(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial1_14819003.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')        

    def initfly_204(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial1_14819004.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')        

    def initfly_205(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial1_14819005.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')        

    def initfly_206(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial1_14819006.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')        

    def initfly_207(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_pattern_test_t2_lightoff')
        fly_record['experiments']['img_pattern_test_t2_lightoff']['axon_file_names'] = ['T2_trial1_14819007.abf']
        fly_record['experiments']['img_pattern_test_t2_lightoff']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['img_pattern_test_t2_lightoff']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_pattern_test_t2_lightoff']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_pattern_test_t2_lightoff'].create_group('sequences')
 
    def initfly_208(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_power_t2_ND_32')
        fly_record['experiments']['img_power_t2_ND_32']['axon_file_names'] = ['T2_trial1_ND_32_14822000.abf']
        fly_record['experiments']['img_power_t2_ND_32']['tiff_file_names'] = ['/T2_trial1_ND_32/T2_trial1_ND_32_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_32']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_32']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_32'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_16')
        fly_record['experiments']['img_power_t2_ND_16']['axon_file_names'] = ['T2_trial2_ND_16_14822001.abf']
        fly_record['experiments']['img_power_t2_ND_16']['tiff_file_names'] = ['/T2_trial2_ND_16/T2_trial2_ND_16_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_16']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_16']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_16'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_08')
        fly_record['experiments']['img_power_t2_ND_08']['axon_file_names'] = ['T2_trial3_ND_08_14822002.abf']
        fly_record['experiments']['img_power_t2_ND_08']['tiff_file_names'] = ['/T2_trial3_ND_08/T2_trial3_ND_08_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_08']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_08']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_08'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_04')
        fly_record['experiments']['img_power_t2_ND_04']['axon_file_names'] = ['T2_trial4_ND_04_14822003.abf']
        fly_record['experiments']['img_power_t2_ND_04']['tiff_file_names'] = ['/T2_trial4_ND_04/T2_trial4_ND_04_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_04']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_04']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_04'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_02')
        fly_record['experiments']['img_power_t2_ND_02']['axon_file_names'] = ['T2_trial5_ND_02_14822004.abf']
        fly_record['experiments']['img_power_t2_ND_02']['tiff_file_names'] = ['/T2_trial5_ND_02/T2_trial5_ND_02_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_02']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_02']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_02'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_01')
        fly_record['experiments']['img_power_t2_ND_01']['axon_file_names'] = ['T2_trial6_ND_01_14822005.abf']
        fly_record['experiments']['img_power_t2_ND_01']['tiff_file_names'] = ['/T2_trial6_ND_01/T2_trial6_ND_01_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_01']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_01']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_01'].create_group('sequences')

    def initfly_209(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_power_t2_ND_32')
        fly_record['experiments']['img_power_t2_ND_32']['axon_file_names'] = ['T2_trial1_ND_32_14822006.abf']
        fly_record['experiments']['img_power_t2_ND_32']['tiff_file_names'] = ['/T2_trial1_ND_32/T2_trial1_ND_32_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_32']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_32']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_32'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_16')
        fly_record['experiments']['img_power_t2_ND_16']['axon_file_names'] = ['T2_trial2_ND_16_14822007.abf']
        fly_record['experiments']['img_power_t2_ND_16']['tiff_file_names'] = ['/T2_trial2_ND_16/T2_trial2_ND_16_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_16']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_16']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_16'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_08')
        fly_record['experiments']['img_power_t2_ND_08']['axon_file_names'] = ['T2_trial3_ND_08_14822008.abf']
        fly_record['experiments']['img_power_t2_ND_08']['tiff_file_names'] = ['/T2_trial3_ND_08/T2_trial3_ND_08_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_08']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_08']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_08'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_04')
        fly_record['experiments']['img_power_t2_ND_04']['axon_file_names'] = ['T2_trial4_ND_04_14822009.abf']
        fly_record['experiments']['img_power_t2_ND_04']['tiff_file_names'] = ['/T2_trial4_ND_04/T2_trial4_ND_04_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_04']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_04']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_04'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_02')
        fly_record['experiments']['img_power_t2_ND_02']['axon_file_names'] = ['T2_trial5_ND_02_14822011.abf']
        fly_record['experiments']['img_power_t2_ND_02']['tiff_file_names'] = ['/T2_trial5_ND_02/T2_trial5_ND_02_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_02']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_02']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_02'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_01')
        fly_record['experiments']['img_power_t2_ND_01']['axon_file_names'] = ['T2_trial6_ND_01_14822012.abf']
        fly_record['experiments']['img_power_t2_ND_01']['tiff_file_names'] = ['/T2_trial6_ND_01/T2_trial6_ND_01_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_01']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_01']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_01'].create_group('sequences')

    def initfly_210(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_power_t2_ND_32')
        fly_record['experiments']['img_power_t2_ND_32']['axon_file_names'] = ['T2_trial1_ND_32_14823000.abf']
        fly_record['experiments']['img_power_t2_ND_32']['tiff_file_names'] = ['/T2_trial1_ND_32/T2_trial1_ND_32_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_32']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_32']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_32'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_16')
        fly_record['experiments']['img_power_t2_ND_16']['axon_file_names'] = ['T2_trial2_ND_16_14823002.abf']
        fly_record['experiments']['img_power_t2_ND_16']['tiff_file_names'] = ['/T2_trial2_ND_16/T2_trial2_ND_16_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_16']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_16']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_16'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_08')
        fly_record['experiments']['img_power_t2_ND_08']['axon_file_names'] = ['T2_trial3_ND_08_14823003.abf']
        fly_record['experiments']['img_power_t2_ND_08']['tiff_file_names'] = ['/T2_trial3_ND_08/T2_trial3_ND_08_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_08']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_08']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_08'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_04')
        fly_record['experiments']['img_power_t2_ND_04']['axon_file_names'] = ['T2_trial4_ND_04_14823004.abf']
        fly_record['experiments']['img_power_t2_ND_04']['tiff_file_names'] = ['/T2_trial4_ND_04/T2_trial4_ND_04_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_04']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_04']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_04'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_02')
        fly_record['experiments']['img_power_t2_ND_02']['axon_file_names'] = ['T2_trial5_ND_02_14823005.abf']
        fly_record['experiments']['img_power_t2_ND_02']['tiff_file_names'] = ['/T2_trial5_ND_02/T2_trial5_ND_02_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_02']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_02']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_02'].create_group('sequences')

    def initfly_211(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('img_power_t2_ND_32')
        fly_record['experiments']['img_power_t2_ND_32']['axon_file_names'] = ['T2_trial1_ND_32_14823006.abf']
        fly_record['experiments']['img_power_t2_ND_32']['tiff_file_names'] = ['/T2_trial1_ND_32/T2_trial1_ND_32_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_32']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_32']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_32'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_16')
        fly_record['experiments']['img_power_t2_ND_16']['axon_file_names'] = ['T2_trial2_ND_16_14823007.abf']
        fly_record['experiments']['img_power_t2_ND_16']['tiff_file_names'] = ['/T2_trial2_ND_16/T2_trial2_ND_16_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_16']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_16']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_16'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_08')
        fly_record['experiments']['img_power_t2_ND_08']['axon_file_names'] = ['T2_trial3_ND_08_14823008.abf']
        fly_record['experiments']['img_power_t2_ND_08']['tiff_file_names'] = ['/T2_trial3_ND_08/T2_trial3_ND_08_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_08']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_08']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_08'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_04')
        fly_record['experiments']['img_power_t2_ND_04']['axon_file_names'] = ['T2_trial4_ND_04_14823009.abf']
        fly_record['experiments']['img_power_t2_ND_04']['tiff_file_names'] = ['/T2_trial4_ND_04/T2_trial4_ND_04_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_04']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_04']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_04'].create_group('sequences')
        fly_record['experiments'].create_group('img_power_t2_ND_02')
        fly_record['experiments']['img_power_t2_ND_02']['axon_file_names'] = ['T2_trial5_ND_02_14823010.abf']
        fly_record['experiments']['img_power_t2_ND_02']['tiff_file_names'] = ['/T2_trial5_ND_02/T2_trial5_ND_02_MMStack.ome.tif']
        fly_record['experiments']['img_power_t2_ND_02']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['img_power_t2_ND_02']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['img_power_t2_ND_02'].create_group('sequences')

    def initfly_216(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('open_loop_test_1ms')
        fly_record['experiments']['open_loop_test_1ms']['axon_file_names'] = ['T2_trial1_ND_04_1ms_exposure_14902001.abf']
        fly_record['experiments']['open_loop_test_1ms']['tiff_file_names'] = ['/T2_trial1_ND_04_1ms_exposure/T2_trial1_ND_04_1ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['open_loop_test_1ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['open_loop_test_1ms']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['open_loop_test_1ms'].create_group('sequences')

    def initfly_217(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('open_loop_test_1ms')
        fly_record['experiments']['open_loop_test_1ms']['axon_file_names'] = ['T2_trial1_ND_04_1ms_exposure_14902002.abf']
        fly_record['experiments']['open_loop_test_1ms']['tiff_file_names'] = ['/T2_trial1_ND_04_1ms_exposure/T2_trial1_ND_04_1ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['open_loop_test_1ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['open_loop_test_1ms']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['open_loop_test_1ms'].create_group('sequences')
        fly_record['experiments'].create_group('open_loop_test_10ms')
        fly_record['experiments']['open_loop_test_10ms']['axon_file_names'] = ['T2_trial2_ND_08_10ms_exposure_14902003.abf']
        fly_record['experiments']['open_loop_test_10ms']['tiff_file_names'] = ['/T2_trial2_ND_08_10ms_exposure/T2_trial2_ND_08_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['open_loop_test_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['open_loop_test_10ms']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['open_loop_test_10ms'].create_group('sequences')

    def initfly_218(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('open_loop_test_1ms')
        fly_record['experiments']['open_loop_test_1ms']['axon_file_names'] = ['T2_trial1_ND_04_1ms_exposure_14902004.abf']
        fly_record['experiments']['open_loop_test_1ms']['tiff_file_names'] = ['/T2_trial1_ND_04_1ms_exposure/T2_trial1_ND_04_1ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['open_loop_test_1ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['open_loop_test_1ms']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['open_loop_test_1ms'].create_group('sequences')
        fly_record['experiments'].create_group('open_loop_test_10ms')
        fly_record['experiments']['open_loop_test_10ms']['axon_file_names'] = ['T2_trial2_ND_08_10ms_exposure_14902005.abf']
        fly_record['experiments']['open_loop_test_10ms']['tiff_file_names'] = ['/T2_trial2_ND_08_10ms_exposure/T2_trial2_ND_08_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['open_loop_test_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['open_loop_test_10ms']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['open_loop_test_10ms'].create_group('sequences')

    def initfly_219(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14904001.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_3.0hz_a10.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_220(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14904003.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 3.5
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_221(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14904005.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')
        fly_record['experiments'].create_group('sin_yaw_1ms')
        fly_record['experiments']['sin_yaw_1ms']['axon_file_names'] = ['T2_trial2_ND_02_1ms_exposure_14904006.abf']
        fly_record['experiments']['sin_yaw_1ms']['tiff_file_names'] = ['/T2_trial2_ND_02_1ms_exposure/T2_trial2_ND_02_1ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_1ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_1ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_1ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_1ms'].create_group('sequences')

    def initfly_222(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14904007.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_223(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14905005.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_224(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14905006.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_225(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14905008.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

################sin yaw ##############
    def initfly_226(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14906000.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_227(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14906001.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_228(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14906002.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_229(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14906004.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_230(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14906007.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_231(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14906008.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

################step responses########

    def initfly_232(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_responses')
        fly_record['experiments']['step_responses']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14908000.abf']
        fly_record['experiments']['step_responses']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['step_responses']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['step_responses']['ol_epoch_duration'] = 3
        fly_record['experiments']['step_responses'].create_group('sequences')

    def initfly_233(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_responses')
        fly_record['experiments']['step_responses']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14909000.abf']
        fly_record['experiments']['step_responses']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['step_responses']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['step_responses']['ol_epoch_duration'] = 3
        fly_record['experiments']['step_responses'].create_group('sequences')

    def initfly_234(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_responses')
        fly_record['experiments']['step_responses']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14909001.abf']
        fly_record['experiments']['step_responses']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['step_responses']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['step_responses']['ol_epoch_duration'] = 3
        fly_record['experiments']['step_responses'].create_group('sequences')

    def initfly_235(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_responses')
        fly_record['experiments']['step_responses']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14909004.abf']
        fly_record['experiments']['step_responses']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['step_responses']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['step_responses']['ol_epoch_duration'] = 3
        fly_record['experiments']['step_responses']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['step_responses'].create_group('sequences')

    def initfly_236(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_responses')
        fly_record['experiments']['step_responses']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14909005.abf']
        fly_record['experiments']['step_responses']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['step_responses']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['step_responses']['ol_epoch_duration'] = 3
        fly_record['experiments']['step_responses']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['step_responses'].create_group('sequences')

################sin yaw group 2 ######

    def initfly_237(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14910002.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_238(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14910003.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_239(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14910004.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_240(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14910006.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_241(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14911000.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_242(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14911001.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_243(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14911002.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

    def initfly_244(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('sin_yaw_10ms')
        fly_record['experiments']['sin_yaw_10ms']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14911003.abf']
        fly_record['experiments']['sin_yaw_10ms']['tiff_file_names'] = ['/T2_trial1_ND_16_10ms_exposure/T2_trial1_ND_16_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['sin_yaw_10ms']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['sin_yaw_10ms']['ol_epoch_duration'] = 60
        fly_record['experiments']['sin_yaw_10ms']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['sin_yaw_10ms'].create_group('sequences')

################TrpA1 test ######

    def initfly_245(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('TrpA1_test')
        fly_record['experiments']['TrpA1_test']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14912000.abf']
        fly_record['experiments']['TrpA1_test']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['TrpA1_test'].create_group('sequences')

    def initfly_246(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('TrpA1_test')
        fly_record['experiments']['TrpA1_test']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14912002.abf']
        fly_record['experiments']['TrpA1_test']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['TrpA1_test'].create_group('sequences')

    def initfly_247(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('TrpA1_test')
        fly_record['experiments']['TrpA1_test']['axon_file_names'] = ['T2_trial1_ND_16_10ms_exposure_14912003.abf']
        fly_record['experiments']['TrpA1_test']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['TrpA1_test'].create_group('sequences')

    def initfly_248(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('TrpA1_test')
        fly_record['experiments']['TrpA1_test']['axon_file_names'] = ['T2_trial1_ND_16_14912005.abf']
        fly_record['experiments']['TrpA1_test']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['TrpA1_test'].create_group('sequences')

    def initfly_249(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('TrpA1_test')
        fly_record['experiments']['TrpA1_test']['axon_file_names'] = ['T2_trial1_ND_16_14912006.abf']
        fly_record['experiments']['TrpA1_test']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['TrpA1_test'].create_group('sequences')

    def initfly_250(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('TrpA1_test')
        fly_record['experiments']['TrpA1_test']['axon_file_names'] = ['T2_trial1_ND_16_14912007.abf']
        fly_record['experiments']['TrpA1_test']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['TrpA1_test'].create_group('sequences')

    def initfly_251(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('TrpA1_test')
        fly_record['experiments']['TrpA1_test']['axon_file_names'] = ['T2_trial1_ND_16_14912008.abf']
        fly_record['experiments']['TrpA1_test']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['TrpA1_test'].create_group('sequences')

    def initfly_252(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('TrpA1_test')
        fly_record['experiments']['TrpA1_test']['axon_file_names'] = ['T2_trial1_ND_16_14912009.abf']
        fly_record['experiments']['TrpA1_test']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['TrpA1_test'].create_group('sequences')

    def initfly_253(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('TrpA1_test')
        fly_record['experiments']['TrpA1_test']['axon_file_names'] = ['T2_trial1_ND_16_14912010.abf']
        fly_record['experiments']['TrpA1_test']['sequence_pattern_names'] = pitch_yaw_aperture_pattern_names
        fly_record['experiments']['TrpA1_test'].create_group('sequences')


################Driver line sin yaw ######

    def initfly_254(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial2_ND_04_10ms_exposure_14929001.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial2_ND_04_10ms_exposure/T2_trial2_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial2_ND_04_100us_exposure_td_end/T2_trial2_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial2_ND_04_100us_exposure_td_refstack/T2_trial2_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']

        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_255(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14929002.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_256(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14929003.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_257(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14929005.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_258(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14929006.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

########
    def initfly_259(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14930000.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_refstack/T2_trial1_ND_04_1ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_260(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14930001.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_refstack/T2_trial1_ND_04_1ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_261(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14930003.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_refstack/T2_trial1_ND_04_1ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_262(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14930004.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_refstack/T2_trial1_ND_04_1ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_263(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14930005.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_refstack/T2_trial1_ND_04_1ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_264(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14930006.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_refstack/T2_trial1_ND_04_1ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    ###
    def initfly_265(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o01000.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_266(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o01001.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_267(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o01002.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_268(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o01003.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_269(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o01004.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')


    def initfly_270(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o01005.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

###

    def initfly_271(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o02000.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_2ms_exposure_td_refstack/T2_trial1_ND_04_2ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')


    def initfly_272(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o02001.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_2ms_exposure_td_refstack/T2_trial1_ND_04_2ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')


    def initfly_273(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o02002.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_2ms_exposure_td_refstack/T2_trial1_ND_04_2ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')



    def initfly_274(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o02003.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_2ms_exposure_td_refstack/T2_trial1_ND_04_2ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')



    def initfly_275(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o02004.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_2ms_exposure_td_refstack/T2_trial1_ND_04_2ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_276(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o02006.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_1ms_exposure_td_end/T2_trial1_ND_04_1ms_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_2ms_exposure_td_refstack/T2_trial1_ND_04_2ms_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_277(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o06000.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_end/T2_trial1_ND_04_500us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_refstack/T2_trial1_ND_04_500us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_278(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o06002.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_end/T2_trial1_ND_04_500us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_refstack/T2_trial1_ND_04_500us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_279(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o06005.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_end/T2_trial1_ND_04_500us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_refstack/T2_trial1_ND_04_500us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_280(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o06008.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_end/T2_trial1_ND_04_500us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_refstack/T2_trial1_ND_04_500us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_281(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o06009.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_end/T2_trial1_ND_04_500us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_refstack/T2_trial1_ND_04_500us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_282(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14o06010.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_end/T2_trial1_ND_04_500us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_500us_exposure_td_refstack/T2_trial1_ND_04_500us_exposure_td_refstack_MMStack.ome.tif']
        
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

####

    def initfly_283(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24000.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_284(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24001.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_285(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24002.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_286(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24003.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_287(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24004.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_288(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record['flynum'] = flynum
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24005.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_289(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24007.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_290(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24009.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_291(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24011.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_292(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n24012.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_293(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n25004.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_294(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n25005.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

    def initfly_295(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n25006.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')


    def initfly_296(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw')
        fly_record['experiments']['driver_line_sin_yaw']['axon_file_names'] = ['T2_trial1_ND_04_10ms_exposure_14n25007.abf']
        fly_record['experiments']['driver_line_sin_yaw']['tiff_file_names'] = ['/T2_trial1_ND_04_10ms_exposure/T2_trial1_ND_04_10ms_exposure_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['td_end_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_end/T2_trial1_ND_04_100us_exposure_td_end_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw']['td_refstack_file_names'] = ['/T2_trial1_ND_04_100us_exposure_td_refstack/T2_trial1_ND_04_100us_exposure_td_refstack_MMStack.ome.tif']
            
        fly_record['experiments']['driver_line_sin_yaw']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw'].create_group('sequences')

###
    def initfly_297(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw_td_movement')
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['axon_file_names'] = ['T2_trial1_ND_8Ex_16Em_10ms_exposure_14d04001.abf']
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['tiff_file_names'] = ['/T2_trial1_ND_8Ex_16Em_10ms_exposure/T2_trial1_ND_8Ex_16Em_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_298(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw_td_movement')
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['axon_file_names'] = ['T2_trial1_ND_8Ex_16Em_10ms_exposure_14d04002.abf']
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['tiff_file_names'] = ['/T2_trial1_ND_8Ex_16Em_10ms_exposure/T2_trial1_ND_8Ex_16Em_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')
    
    def initfly_299(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw_td_movement')
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['axon_file_names'] = ['T2_trial1_ND_8Ex_16Em_10ms_exposure_14d04003.abf']
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['tiff_file_names'] = ['/T2_trial1_ND_8Ex_16Em_10ms_exposure/T2_trial1_ND_8Ex_16Em_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_300(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('driver_line_sin_yaw_td_movement')
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['axon_file_names'] = ['T2_trial1_ND_8Ex_16Em_10ms_exposure_14d04004.abf']
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['tiff_file_names'] = ['/T2_trial1_ND_8Ex_16Em_10ms_exposure/T2_trial1_ND_8Ex_16Em_10ms_exposure_MMStack.ome.tif']
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['imaging_frame_rate_guess'] = 70
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['ol_epoch_duration'] = 60
        fly_record['experiments']['driver_line_sin_yaw_td_movement']['ol_function_name'] = 'position_function_sin_0.5hz_a40.0.mat'
        fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    ### missing 301

    def initfly_302(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw')
        fly_record['experiments']['step_yaw']['axon_file_names'] = ['T2_trial1_led_test_14d30003.abf']
        fly_record['experiments']['step_yaw']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')


    def initfly_303(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw')
        fly_record['experiments']['step_yaw']['axon_file_names'] = ['T2_trial1_led_test_14d30005.abf']
        fly_record['experiments']['step_yaw']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_304(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw')
        fly_record['experiments']['step_yaw']['axon_file_names'] = ['T2_trial1_led_test_14d30007.abf']
        fly_record['experiments']['step_yaw']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')
####
    def initfly_305(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_14d31001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_306(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_14d31002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_307(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_14d31003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_308(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_14d31005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_309(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_14d31007.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_310(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15102001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_311(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15102002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_312(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15102004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_313(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15102005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

#############

    def initfly_314(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15108000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_315(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15108001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_316(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15108002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')
        
    def initfly_317(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15108004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_318(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15108007.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_319(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15108008.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_320(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15108009.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_321(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15108010.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_322(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15108012.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

###

    def initfly_323(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15114001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_324(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15114002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_325(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15114003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_326(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15114004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

#########

    def initfly_327(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15115001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_328(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15115002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_header_fix.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

#########

    def initfly_329(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15116001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_330(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15116002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')
        
    def initfly_331(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15116003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_332(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15116005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_333(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15116006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

###

    def initfly_334(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15122006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_335(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15122007.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_336(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15122008.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

##########

    def initfly_337(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15203003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_338(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15203004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_339(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15203005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_340(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15203006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_341(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15203007.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_342(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15203008.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_343(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15203010.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.repair.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_344(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15203011.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

#############

    def initfly_345(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15204000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_346(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15204001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_347(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15204003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_348(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15204005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

####


    def initfly_349(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15205000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_350(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15205002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_351(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15205003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_352(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15205004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

#########################

    def initfly_353(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15211001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')


    def initfly_354(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15211002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')


    def initfly_355(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15211003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')


    def initfly_356(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15211004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

####

    def initfly_357(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15213001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_358(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15213002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_359(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15213003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_360(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15213006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_361(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15225000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_362(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15225002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']
        #fly_record['experiments']['driver_line_sin_yaw_td_movement'].create_group('sequences')

    def initfly_363(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15225003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_364(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15225004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_365(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15225005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_366(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15227000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_367(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15227003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_368(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15227004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_369(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15227006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_370(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15228001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_371(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15228002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_372(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15228003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_373(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15228004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_374(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15301000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_375(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15301002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_376(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15302000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_377(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15302001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_378(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15302003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_379(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15302004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_380(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15304000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_381(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15304002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_382(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15304003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_383(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15304002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_384(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15305000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_385(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15305001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_386(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15305002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

####

    def initfly_387(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15312001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_388(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15312002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_389(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15312004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_390(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15312005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_391(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15312007.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_392(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15312008.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


#############

    def initfly_393(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15313000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_394(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15313001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_395(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15313003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_396(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15313004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_397(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15313006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_398(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15313007.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

#############

    def initfly_399(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['15314001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_400(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15314002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_401(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15314003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_402(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15314004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_403(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15314005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_404(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15313004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    ##############

    def initfly_405(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15316002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_406(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15316003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_407(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15316004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_408(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15316005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_409(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15316006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_410(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15316008.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_411(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15316010.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_412(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15316011.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_413(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15316012.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


#################

    def initfly_414(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15317000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_415(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15317001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_416(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15317002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_417(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15317003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_418(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15317004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_419(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15317005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_420(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15317006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_421(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15317007.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_422(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15317009.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

#########

    def initfly_423(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15324001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_424(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15324002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_425(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15324003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

####################################
####################################
######## Pilot td tomato exp here ##
####################################
####################################

    def initfly_430(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15330000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_431(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15330001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_432(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15330002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_433(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15330003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_434(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15331000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_435(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15331001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_436(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15331002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_437(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15331003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_438(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15402001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_439(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15402002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_440(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15402003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_441(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15402004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_442(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15402006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_443(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15402007.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_444(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15407001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_445(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15407002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_446(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15407003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_447(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15407004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


###############
###############
###############


    def initfly_448(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15416000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_449(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15416001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_450(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15416002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_451(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15416003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_452(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15416004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_453(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15421000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_454(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15421001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_455(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15421002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_456(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15421003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_457(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15421004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_458(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15421006.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_459(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15421007.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_460(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15421008.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_461(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15422001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_462(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15422002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_463(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15422003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']


    def initfly_464(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15422004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

######################

    def initfly_465(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15424003.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

######################
    def initfly_466(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15427001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_467(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15427002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_468(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15427003.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_469(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15427004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_470(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15427005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

#############
#############

    def initfly_471(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15428001.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_472(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15428003.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_473(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15428005.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_474(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15428006.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

####
    def initfly_475(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15429001.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_476(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15429002.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_477(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15429005.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    ###########

    def initfly_478(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15430001.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_479(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15430002.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_480(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15430003.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_481(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15430005.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_482(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15501000.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_483(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15501001.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_484(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15501002.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_485(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15501003.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_486(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll')
        fly_record['experiments']['step_ptch_roll']['axon_file_names'] = ['T2_trial1_ptch_roll_15501004.abf']
        fly_record['experiments']['step_ptch_roll']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

##########
##########

    def initfly_487(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15506003.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_488(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15506005.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_489(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15506006.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_490(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15507001.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_491(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15507007.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_492(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15507009.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_493(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15507011.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_494(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15507013.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_495(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15507014.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_496(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15507016.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

######
######

    def initfly_497(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15508000.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_498(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15508002.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_499(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15508003.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

######
######

    def initfly_500(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15511000.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_501(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15511002.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

    def initfly_502(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_ptch_roll_ctrl')
        fly_record['experiments']['step_ptch_roll_ctrl']['axon_file_names'] = ['T2_trial1_ptch_roll_15511003.abf']
        fly_record['experiments']['step_ptch_roll_ctrl']['tiff_file_names'] = ['/T2_trial1_ptch_roll/T2_trial1_ptch_roll_MMStack.ome.tif']

#####
#####

    def initfly_503(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15518000.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_504(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15518001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_505(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15518002.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_506(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15518004.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

    def initfly_507(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_led_test_15518005.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1_led_test/T2_trial1_led_test_MMStack.ome.tif']

################
## Fly0508 contains the data from the
## segmented confocal images
################

    def initfly_509(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('step_yaw_mod1')
        fly_record['experiments']['step_yaw_mod1']['axon_file_names'] = ['T2_trial1_15706001.abf']
        fly_record['experiments']['step_yaw_mod1']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

##############
##############

    def initfly_510(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('ASAP_pilot')
        fly_record['experiments']['ASAP_pilot']['axon_file_names'] = ['T2_trial1_15706004.abf']
        fly_record['experiments']['ASAP_pilot']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_511(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('ASAP_pilot')
        fly_record['experiments']['ASAP_pilot']['axon_file_names'] = ['T2_trial1_15707000.abf']
        fly_record['experiments']['ASAP_pilot']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']


    def initfly_512(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('ASAP_pilot')
        fly_record['experiments']['ASAP_pilot']['axon_file_names'] = ['T2_trial1_15707001.abf']
        fly_record['experiments']['ASAP_pilot']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_513(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('ASAP_pilot')
        fly_record['experiments']['ASAP_pilot']['axon_file_names'] = ['T2_trial1_15707002.abf']
        fly_record['experiments']['ASAP_pilot']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_514(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('ASAP_pilot')
        fly_record['experiments']['ASAP_pilot']['axon_file_names'] = ['T2_trial1_15707003.abf']
        fly_record['experiments']['ASAP_pilot']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_515(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('ASAP_pilot')
        fly_record['experiments']['ASAP_pilot']['axon_file_names'] = ['T2_trial1_15707005.abf']
        fly_record['experiments']['ASAP_pilot']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_516(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('ASAP_pilot')
        fly_record['experiments']['ASAP_pilot']['axon_file_names'] = ['T2_trial1_15707006.abf']
        fly_record['experiments']['ASAP_pilot']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_517(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('ASAP_pilot')
        fly_record['experiments']['ASAP_pilot']['axon_file_names'] = ['T2_trial1_15707007.abf']
        fly_record['experiments']['ASAP_pilot']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
    
    def initfly_518(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['T2_trial1_15707009.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1_MMStack.ome.resave.tif']

    def initfly_519(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15708000.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_520(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15709002.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
    

    def initfly_521(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15709002.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
    

    def initfly_522(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15709003.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_523(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15709008.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_524(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15715009.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
    

    def initfly_525(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15715011.abf']
        #fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1_MMStack_resave.ome.tif']

    def initfly_526(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15720008.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']

    def initfly_527(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15720010.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        
    def initfly_528(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15727003.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
    

    def initfly_529(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15727004.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        
    

    def initfly_530(self,flynum):
        fly_db = self.fly_db
        fly_db.create_group(flynum)
        fly_record =fly_db[flynum]
        fly_record.create_group('experiments')
        fly_record['experiments'].create_group('strain_tracking')
        fly_record['experiments']['strain_tracking']['axon_file_names'] = ['15727006.abf']
        fly_record['experiments']['strain_tracking']['tiff_file_names'] = ['/T2_trial1/T2_trial1_MMStack.ome.tif']
        