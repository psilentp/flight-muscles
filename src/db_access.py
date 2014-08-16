# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

import sys
import json
import os
import numpy as np
import h5py

import json
param_file = open('params.json','rb')
params = json.load(param_file)
root_dir = params['platform_paths'][sys.platform] + params['root_dir']
#root_dir = '/Volumes/FlyDataB/FlyDB/'

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

def get_db():
    #fly_db = h5py.File('/Volumes/FlyDataB/FlyDB/flydb.hdf5','a')
    flydirs = filter(lambda s:'Fly' in s,os.listdir(root_dir))
    initialized_flies = filter(lambda s:'fly_record.hdf5' in os.listdir(root_dir+'/'+s),flydirs)
    fly_db = FlyDB(root_dir)
    for fly in initialized_flies:
        flynum = int(fly.split('Fly')[1])
        #print flynum
        fly_db[flynum] = h5py.File(root_dir+fly+'/fly_record.hdf5','a')
    return fly_db

starfield_pattern_names_6_0_2014  = ['equator_000.mat',
                            'equator_030.mat',
                            'equator_060.mat',
                            'equator_090.mat',
                            'equator_120.mat',
                            'equator_150.mat',
                            'equator_180.mat',
                            'equator_210.mat',
                            'equator_240.mat',
                            'equator_270.mat',
                            'equator_300.mat',
                            'equator_330.mat',
                            'coromeridian_030.mat',
                            'coromeridian_060.mat',
                            'coromeridian_090.mat',
                            'coromeridian_120.mat',
                            'coromeridian_150.mat',
                            'coromeridian_210.mat',
                            'coromeridian_240.mat',
                            'coromeridian_270.mat',
                            'coromeridian_300.mat',
                            'coromeridian_330.mat',
                            'sagimeridian_030.mat',
                            'sagimeridian_060.mat',
                            'sagimeridian_120.mat',
                            'sagimeridian_150.mat',
                            'sagimeridian_210.mat',
                            'sagimeridian_240.mat',
                            'sagimeridian_300.mat',
                            'sagimeridian_330.mat']

starfield_pattern_names_6_29_2014  = ['translate_forward.mat',
                            'translate_backward.mat',
                            'translate_up.mat',
                            'translate_down.mat',
                            'spin_equator_000.mat',
                            'spin_equator_030.mat',
                            'spin_equator_060.mat',
                            'spin_equator_090.mat',
                            'spin_equator_120.mat',
                            'spin_equator_150.mat',
                            'spin_equator_180.mat',
                            'spin_equator_210.mat',
                            'spin_equator_240.mat',
                            'spin_equator_270.mat',
                            'spin_equator_300.mat',
                            'spin_equator_330.mat']
l = [[x,x,x] for x in starfield_pattern_names_6_29_2014]
starfield_pattern_names_6_29_2014 = [item for sublist in l for item in sublist]

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

    #############################################################################################fly_record = dict()
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

    #############################################################################################
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
    #############################################################################################
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
    #############################################################################################
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
    #############################################################################################
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
    #############################################################################################
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
    #############################################################################################
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
    #############################################################################################
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
    #############################################################################################
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
    #############################################################################################
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
    #############################################################################################
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

    #######
    #######
    #######
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


