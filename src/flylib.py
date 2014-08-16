import numpy as np
import sys
import json
import os
import random
import scipy
import quantities as pq
import scipy.io
#import warnings

stro_R = 'phi_R'
stro_L = 'phi_L'
stroke_dev_R = 'theta_R'
stroke_dev_L = 'theta_L'
wing_rot_R = 'eta_R'
wing_rot_L = 'eta_L'

param_file = open('params.json','rb')
params = json.load(param_file)
param_file.close()

photron_interest_signals = ['eta_L','eta_R','phi_L','phi_R','photron_sample_times','theta_L','theta_R']
axon_interest_signals = ['AMsysCh1','CamSync','LeftWing','Ph0','Ph1','Ph2','Photostim','RightWing','WBSync','Xpos','Ypos','axon_sample_times']


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
#rootpath = params['platform_paths'][sys.platform] + params['root_dir']


class Squadron(object):
    """Controller object to facilitate the groupwise analysis of the fly data"""
    def __init__(self,fly_db,fly_numbers):
        self.fly_db = fly_db
        self.fly_numbers = [int(fln) for fln in fly_numbers]
        self.flies = [Fly(self.fly_db,fln) for fln in self.fly_numbers]
        
class Fly(object):
    """Controler object for fly data, Fly is initialized with a 'fly_record dictionary
    and the object is used to facilitate adding and removing data from this dictionary
    but does does not itself own the dictionary: if Fly is deleted, the dictionary
    can still exist"""
    def __init__(self,fly_db,fly_num):
        self.fly_num = fly_num
        self.fly_record = fly_db[fly_num]
        self.param_file = open('params.json','rb')
        self.params = json.load(self.param_file)
        self.param_file.close()
        self.rootpath = self.params['platform_paths'][sys.platform] + self.params['root_dir']
        self.fly_path = self.rootpath + ('Fly%04d/')%(fly_num)
        self.experiments = self.get_experiments()
        
    def get_experiments(self):
        experiments = dict()
        for experiment_name in self.fly_record['experiments'].keys():
            experiments[experiment_name] = exp_map[experiment_name](self.fly_record,experiment_name,self.fly_path)
        return experiments
    
class Experiment(object):
    """Controller class for an individual experiments init with the fly_record and
    experiment name holds a reference to the experiment record in the fly_record 
    to facilitate operations on those data"""
    
    def __init__(self,fly_record,experiment_name,fly_path):
        self.experiment_name = experiment_name
        self.fly_record = fly_record
        self.exp_record = fly_record['experiments'][experiment_name]
        self.fly_path = fly_path
        self.sequences = self.get_sequences()
    
    def get_sequences(self):
        pass

class Sequence(object):
    def __init__(self,exp_record,seq_num,fly_path):
        self.exp_record = exp_record
        self.fly_path = fly_path
        self.seq_num = seq_num
        try:
            self.seq_record = exp_record['sequences'][str(seq_num)]
        except KeyError:
            exp_record['sequences'].create_group(str(seq_num))
            self.seq_record = exp_record['sequences'][str(seq_num)]

#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################

class HSVExperiment(Experiment):
    """Controller class for an individual experiments init with the fly_record and
    experiment name holds a reference to the experiment record in the fly_record 
    to facilitate operations on those data"""
    
    def get_sequences(self):
        sequences = dict()
        for snum in self.exp_record['photron_seq_nums']:
            sequences[snum] = HSVSequence(self.exp_record,snum,self.fly_path)
        return sequences
        
    def import_sequence_data(self):
        for key in self.sequences.keys():
            self.sequences[key].import_flytracks()
            self.sequences[key].import_processed_wbkin()
    
    def import_axon_data(self,filenum = 0):
        """load the axon data from an experiment into the fly_record"""
        axon_file = self.fly_path + self.exp_record['axon_file_names'][filenum]
        axondata = get_axon_signals(axon_file)
        if not('axon_data' in self.exp_record.keys()):
            self.exp_record.create_group('axon_data')
        for key in axondata:
            self.exp_record['axon_data'][key] = axondata[key]
            
    def calc_spikepool(self,thresh =5,wl = 100, wr = 200,filter_window = 55,invert_polarity = False):
        """initialize a putative pool of unsorted spikes"""
        if not('spike_data' in self.exp_record.keys()):
            self.exp_record.create_group('spike_data')
        else:
            del(self.exp_record['spike_data'])
            self.exp_record.create_group('spike_data')
        sweep = np.array(self.exp_record['axon_data']['AMsysCh1'])
        times = np.array(self.exp_record['axon_data']['times'])
        if invert_polarity:
            sweep *= -1
        import neo
        import sorters
        sig = neo.AnalogSignal(sweep,units = 'V',sampling_period = pq.Quantity(times[1]-times[0],'s'))
        sp = sorters.get_spike_pool(sig,
                                    thresh=thresh,
                                    wl = wl, wr = wr,
                                    filter_window = filter_window)
        self.exp_record['spike_data']['spike_pool'] = np.array(sp)
        self.exp_record['spike_data']['wv_mtrx'] = sp.wv_mtrx
        self.exp_record['spike_data']['time_mtrx'] = sp.time_mtrx
        self.exp_record['spike_data']['peak_times'] = np.array(sp.times)
        self.sp = sp
    
    def set_spike_selection(self,cell_name,selection_mask,pickle_data = True):
        """add a selection mask for spikes of a particular cell"""
        if not(cell_name in self.exp_record['spike_data'].keys()):
            self.exp_record['spike_data'].create_group(cell_name)
        else:
            del(self.exp_record['spike_data'][cell_name])
            self.exp_record['spike_data'].create_group(cell_name)
        self.exp_record['spike_data'][cell_name]['selection_mask'] = selection_mask
        if pickle_data:
            sp_file = open(self.fly_path+'spike_pool.cpkl','wb')
            mask_file = open(self.fly_path+'spike_mask.cpkl','wb')
            import cPickle as cpkl
            cpkl.dump(np.array(self.sp),sp_file)
            cpkl.dump(np.array(selection_mask),mask_file)
            sp_file.close()
            sp_file.close()
    
    def sync_sorted_spikes(self,cell_name):
        """mix the sorted spikes into the wb_mtrx"""
        for seq_key in self.sequences.keys():
            seq = self.sequences[seq_key]
            wb_times_mtrx = np.array(seq.seq_record['wb_mtrx']['axon_sample_times'])
            wb_spike_mtrx = np.zeros_like(wb_times_mtrx)
            mask = np.array(self.exp_record['spike_data'][cell_name]['selection_mask'])
            spk_times = self.exp_record['spike_data']['peak_times'][mask]
            for wb in np.arange(np.shape(wb_times_mtrx)[0]):
                wb_times = wb_times_mtrx[wb,:]
                cond1 = wb_times[~np.isnan(wb_times)][0]<spk_times
                cond2 = wb_times[~np.isnan(wb_times)][-1]>spk_times
                spikes_in_wb = np.argwhere(cond1 & cond2)
                for spk in spikes_in_wb:
                    idx = np.argwhere(np.diff((wb_times>spk_times[spk]).astype(float))>0)
                    wb_spike_mtrx[wb,idx] = 1
            if 'spikes_%s'%cell_name in seq.seq_record['wb_mtrx'].keys():
                del(seq.seq_record['wb_mtrx']['spikes_%s'%cell_name])
            seq.seq_record['wb_mtrx']['spikes_%s'%cell_name] = wb_spike_mtrx
        
    def sync_sequences(self):
        """sync the timing of ephys and high speed video data"""
        if 'axon_data' not in self.exp_record.keys():
            self.import_axon_data()
        fps = pq.Quantity(np.float64(self.exp_record['photron_frame_rate_Hz']),'Hz')
        trig_idxs = idx_by_thresh(np.array(self.exp_record['axon_data']['CamTrig']))
        start_idxs = [x[0] for x in trig_idxs]
        times = np.array(self.exp_record['axon_data']['times'])
        def fallback_frame_idx(cam_epoch,numframes):
            idx = np.array(np.ceil(np.linspace(cam_epoch[0],cam_epoch[-1],numframes)),dtype = int)
            return idx
        for snum,start_idx in zip(sorted(self.sequences.keys()),start_idxs):
            sequence = self.sequences[snum]
            numframes = sequence.seq_record['wbkin']['last_track'][0]
            capture_epoch = numframes/fps
            ax_dt = pq.Quantity(times[1]-times[0],'s')
            capture_samples = np.ceil(capture_epoch/ax_dt)
            epoch = np.arange(np.int(start_idx),np.int(start_idx)+capture_samples,dtype = np.int)
            try:
                frame_idxs = get_frame_idxs(epoch,self.exp_record['axon_data'])
            except IndexError:
                import warnings
                warnings.warn("problem extracting idxs from camera_sync_signal for sequence %s using even spaced idx's over the camera epoch instead"%(snum))
                frame_idxs = fallback_frame_idx(epoch,numframes)
            if not(np.shape(frame_idxs)[0] == numframes):
                import warnings
                warnings.warn("problem extracting idxs from camera_sync_signal for epoch %s using even spaced idx's over the camera epoch instead"%(snum))
                frame_idxs = fallback_frame_idx(epoch,numframes)
            if not('axon' in sequence.seq_record.keys()):
                sequence.seq_record.create_group('axon')
            sequence.seq_record['wbkin']['axon_epoch'] = epoch
            sequence.seq_record['wbkin']['axon_idxs'] = frame_idxs
            sequence.seq_record['wbkin']['photron_sample_times'] = times[frame_idxs]
            keys = filter(lambda x: not(x in ['times','sampling_period']),self.exp_record['axon_data'].keys())
            for key in keys:
                signal = np.array(self.exp_record['axon_data'][key])
                sequence.seq_record['axon'][key] = signal[frame_idxs[0]:frame_idxs[-1]]
            sequence.seq_record['axon']['axon_sample_times'] = times[frame_idxs[0]:frame_idxs[-1]]
            sequence.seq_record['expan_pol'] = sequence.lookup_trial_from_ypos()

class HSVSequence(Sequence):
    def __init__(self,exp_record,seq_num,fly_path):
        Sequence.__init__(self,exp_record,seq_num,fly_path)
        frmtstr = self.exp_record['solution_format_string'][0]
        self.seq_path = self.fly_path + frmtstr%(self.seq_num)
    
    def import_flytracks(self):
        self.seq_record['flytracks'] = load_flytracks_files(self.seq_path)
        
    def import_processed_wbkin(self):
        """import the wbkin file produced by Johan's matlab script"""
        frmtstr = self.exp_record['solution_format_string'][0]
        frmtstr += self.exp_record['kine_filename'][0]
        kine_filename = self.fly_path + frmtstr%(self.seq_num)
        data = load_wbkin_file(kine_filename)
        if not('wbkin' in self.seq_record.keys()):
            self.seq_record.create_group('wbkin')
        for key in data:
            self.seq_record['wbkin'][key] = data[key]
        
    def lookup_trial_from_ypos(self):
        """map the Y position signal to the trial type - given some epoch to average
        over. A future version will be able to figure out what that interval should be
        - but this might be hard to do without loosing generality"""
        epoch_ypos = np.mean(self.seq_record['axon']['Ypos'])
        trial_idx = np.argmin(abs(self.exp_record['Ypos_trial_volts']-epoch_ypos))
        trial_val = self.exp_record['Ypos_trial_vals'][trial_idx]
        return trial_val
    
    def calc_seqs_strokeplanes(self):
        """calculate the strokeplane for all the seqences of an experiment
        should move this to the matlab program that generates kine data"""
        if 'solution_sequences' not in self.exp_record.keys(): 
            self.load_solution_sequences()
        seqs = self.exp_record['solution_sequences']
        self.exp_record['strokeplanes'] = [calc_seq_strokeplane(s) for s in seqs]
        
    def calc_kine_phases(self,fband = (180,300)):
        """calculate the time series of the wingstroke phase extracted from the wingbeat
        kine inplace. 'fband' defines the frequency band to detect phases"""
        from scipy.signal import hilbert
        frame_times = self.seq_record['wbkin']['photron_sample_times']
        stro_angle = np.array((self.seq_record['wbkin'][stro_L][:,] + self.seq_record['wbkin'][stro_R][:,])/2)
        stro_angle = np.squeeze(stro_angle)
        nan_idx = np.argwhere(~np.isnan(stro_angle))
        frame_times = frame_times[~np.isnan(stro_angle)]
        phase_trace = stro_angle.copy()
        stro_angle = stro_angle[~np.isnan(stro_angle)]
        filt_sig = butter_bandpass_filter(stro_angle,fband[0],fband[1],frame_times[1]-frame_times[0],order = 3)
        peaks = scipy.signal.find_peaks_cwt(filt_sig*-1,np.arange(1,20))
        A = np.angle(hilbert(filt_sig))
        A = np.mod(np.unwrap(A),2*np.pi)
        #find the phase of the ventral stroke reversal and re-wrap
        peak_phase = np.mean(A[peaks])
        A2 = np.unwrap(A)+peak_phase
        phase_trace[nan_idx] = A2[:]
        self.seq_record['wbkin']['seq_phase'] = phase_trace
        
    def calc_wb_mtrx(self,num_samples = 1500):
        """resample the data from  the photron and axon signals into the phase domain-
        currently three cycles -2pi to 4pi"""
        import scipy
        wb_idx = self.select_wb_idx()
        phase = np.array(self.seq_record['wbkin']['seq_phase'])
        photron_sample_times = np.array(self.seq_record['wbkin']['photron_sample_times'])
        axon_sample_times = np.array(self.seq_record['axon']['axon_sample_times'])
        wb_mtrx = dict()
        for key in photron_interest_signals:
            wb_mtrx[key] = list()
        for key in axon_interest_signals:
            wb_mtrx[key] = list()
        for a_samp,p_samp in zip(wb_idx['axon_sample_idx'],wb_idx['photron_sample_idx']):
            try:
                phase = np.array(self.seq_record['wbkin']['seq_phase'])
                photron_sample_times_wb = photron_sample_times[p_samp]
                axon_sample_times_wb = axon_sample_times[a_samp]
                #### get a shifted phase trace
                zero_idx = np.argwhere(np.diff(np.mod(phase[p_samp],2*np.pi))<0)[0]
                phs_points_photron = phase[p_samp]-phase[p_samp][zero_idx]
                #### get the phases at the axon sample points
                phs_points_axon = scipy.interpolate.griddata(photron_sample_times_wb,
                                                 phs_points_photron,
                                                 axon_sample_times_wb,
                                                 method = 'cubic')
                nans = np.isnan(phs_points_axon)
                #### now resample all the photron and axon signals at xi
                xi = np.linspace(-2*np.pi,4*np.pi,num_samples)
                for key in photron_interest_signals:
                    signal = np.squeeze(np.array(self.seq_record['wbkin'][key])[p_samp])
                    if key in ['eta_L','eta_R']:
                        signal = np.unwrap(signal - np.pi/2)
                    wb_mtrx[key].append(scipy.interpolate.griddata(phs_points_photron,
                                                       signal,
                                                       xi,
                                                       method = 'cubic'))
                for key in axon_interest_signals:
                    signal = np.squeeze(np.array(self.seq_record['axon'][key])[a_samp])
                    wb_mtrx[key].append(scipy.interpolate.griddata(phs_points_axon[~nans],
                                                       signal[~nans],
                                                       xi,
                                                       method = 'linear'))
            except Exception as err:
               print err
        self.seq_record.create_group('wb_mtrx')
        for key in wb_mtrx:
            self.seq_record['wb_mtrx'][key] = np.array(wb_mtrx[key])
            
    def calc_stim_frame(self,x_thresh = 2.5):
        idx_col = np.argwhere(np.array(self.seq_record['axon']['Xpos'])>x_thresh)[0]
        t_col = np.array(self.seq_record['axon']['axon_sample_times'])[idx_col]
        ax_times = np.array(self.seq_record['wb_mtrx']['axon_sample_times'])
        ph_times = np.array(self.seq_record['wb_mtrx']['photron_sample_times'])
        mean_times = (ax_times+ph_times)/2
        stim_times= mean_times - t_col
        update_dset(self.seq_record['wb_mtrx'],'stim_frame_times',stim_times)
                                                       
    def select_wb_idx(self):
        """utility function to extract the indices of the wingstrokes, used for the
        calc_wb_mtrx function"""
        phases = np.array(self.seq_record['wbkin']['seq_phase'])
        frame_times = np.array(self.seq_record['wbkin']['photron_sample_times'])
        nanidx = np.squeeze(np.argwhere(~np.isnan(phases)))
        idx = np.argwhere(np.diff(np.mod(phases[nanidx],2*np.pi))<0)[:,0]+1+nanidx[0]
        stai = 0
        stpi = len(idx)-2
        #store the data in some lists
        stroke_phys_idx = list();stroke_kin_idx = list()
        #we need the axon data to load the phys data
        axon_times = self.seq_record['axon']['axon_sample_times']
        for i1,i2 in zip(idx[stai:stpi],idx[stai+3:stpi+3])[:-5]:
            stroke_kin_idx.append(np.arange(i1,i2))
            axon_i1 = np.argwhere(axon_times>=frame_times[i1])[0]
            axon_i2 = np.argwhere(axon_times>frame_times[i2])[0]
            stroke_phys_idx.append(np.arange(axon_i1,axon_i2))
        return {'photron_sample_idx':stroke_kin_idx,
                'axon_sample_idx':stroke_phys_idx}

#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################

class IMGExperiment(Experiment):

    def get_sequences(self):
        sequences = dict()
        if 'sequence_pattern_names' in self.exp_record.keys():
            for snum,sname in enumerate(self.exp_record['sequence_pattern_names']):
                sequences[snum] = IMGSequence(self.exp_record,snum,self.fly_path)
        else:
            self.exp_record['sequence_pattern_names'] = starfield_pattern_names_6_0_2014
            for snum,sname in enumerate(self.exp_record['sequence_pattern_names']):
                sequences[snum] = IMGSequence(self.exp_record,snum,self.fly_path)
        return sequences

    def get_images(self):
        return np.array(self.exp_record['tiff_data']['images'])

    def set_roi_data(self,roi_dict):
        ename = self.experiment_name 
        f = open(self.fly_path + ename + '_roi.cpkl','wb')
        import cPickle
        cPickle.dump(roi_dict,f)
        f.close()
        #if 'roi_data' not in self.exp_record.keys():
        #    self.exp_record.create_group('roi_data')
        #for key in roi_dict:
        #    update_dset(self.exp_record['roi_data'],key,roi_dict[key])

    def import_axon_data(self,filenum = 0):
        """load the axon data from an experiment into the fly_record"""
        axon_file = self.fly_path + self.exp_record['axon_file_names'][filenum]
        axondata = get_axon_signals(axon_file)
        if not('axon_data' in self.exp_record.keys()):
            self.exp_record.create_group('axon_data')
        for key in axondata:
            update_dset(self.exp_record['axon_data'],key,axondata[key])
            #self.exp_record['axon_data'][key] = axondata[key]

    def import_tiff_data(self,filenum = 0):
        tiff_file = self.fly_path + self.exp_record['tiff_file_names'][filenum]
        import tifffile
        tif = tifffile.TiffFile(tiff_file)
        images = tif.asarray()
        if not('tiff_data' in self.exp_record.keys()):
            self.exp_record.create_group('tiff_data')
        update_dset(self.exp_record['tiff_data'],'images',images)
        #self.exp_record['tiff_data']['images'] = images

    def calc_framebase(self):
        if 'axon_data' not in self.exp_record.keys():
            self.import_axon_data()
        if 'tiff_data' not in self.exp_record.keys():
            self.import_tiff_stack()
        sigs = self.exp_record['axon_data']
        exposures = idx_by_thresh(np.array(sigs['CamSync']),thresh = 1)
        frames = np.array([x[-1] for x in exposures])[0:-1].astype(int)
        update_dset(self.exp_record['tiff_data'],'frame_idx',frames)
        if 'axon_framebase' not in self.exp_record['tiff_data'].keys():
            self.exp_record['tiff_data'].create_group('axon_framebase')
        for key in sigs.keys():
            sig = np.array(sigs[key])
            downsamp = np.array([np.mean(sig[ex]) for ex in exposures])
            update_dset(self.exp_record['tiff_data']['axon_framebase'],key,downsamp)
        
    def sync_sequences(self):
        frame_rate = self.exp_record['imaging_frame_rate_guess'].value
        ep_duration = self.exp_record['ol_epoch_duration'].value
        if 'axon_data' not in self.exp_record.keys():
            self.import_axon_data()
        if 'tiff_data' not in self.exp_record.keys():
            self.import_tiff_stack()
        if 'axon_framebase' not in self.exp_record['tiff_data'].keys():
            self.calc_framebase()
        sigs = self.exp_record['tiff_data']['axon_framebase']
        ypos = np.array(self.exp_record['axon_data']['Ypos'])
        ax_time = np.array(self.exp_record['axon_data']['times'])
        frame_times = np.array(sigs['times'])
        epochs = idx_by_thresh(ypos*-1,-9.5)
        ttups = [(ax_time[ep[0]],ax_time[ep[0]]+ep_duration) for ep in epochs]
        new_epochs = [np.squeeze(np.argwhere((frame_times>ttup[0]) & (frame_times<ttup[1]))) for ttup in ttups] 
        #new_epochs = [np.arange(ep[0],ep[0]+frame_rate*ep_duration).astype(int) for ep in epochs]
        ypos_frames = np.array(self.exp_record['tiff_data']['axon_framebase']['Ypos'])
        trial_ind = [int(np.around(np.mean(ypos_frames[ep[10:30]])*10)) for ep in new_epochs]
        sorted_epochs = sorted(zip(trial_ind,new_epochs),key = lambda x:x[0])
        for skey,seq_epoch in enumerate(sorted_epochs):
            sequence = self.sequences[skey]
            try:
                update_dset(sequence.seq_record,'epoch_framebase',seq_epoch[1])
            except IndexError:
                print('missing sequence #%s'%(skey))

class IMGSequence(Sequence):
    def __init__(self,exp_record,seq_num,fly_path):
        Sequence.__init__(self,exp_record,seq_num,fly_path)
        self.seq_pattern_name = self.exp_record['sequence_pattern_names'][seq_num]

#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
#############################################################################
def calc_seq_strokeplane(self,seq):
    """calculate the strokeplane from the quaternions of a sequence"""
    q_left = np.squeeze(seq[:,[9,10,11,8]])
    q_right = np.squeeze(seq[:,[13,14,15,12]])
    import transformations as trans
    rot_mats_left = np.array([trans.quaternion_matrix(x.T)[:3,:3] for x in q_left])
    rot_mats_right = np.array([trans.quaternion_matrix(x.T)[:3,:3] for x in q_right])
    l_wingtip = np.dot(rot_mats_left,[0,1,0]).T
    r_wingtip = np.dot(rot_mats_right,[0,-1,0]).T
    from scipy.stats import linregress
    idx = ~np.isnan(l_wingtip[0])
    l_slope = linregress(l_wingtip[0][idx],l_wingtip[2][idx])[0]
    r_slope = linregress(r_wingtip[0][idx],r_wingtip[2][idx])[0]
    return (np.rad2deg(np.arctan(l_slope)),np.rad2deg(np.arctan(r_slope)))
                        
def get_frame_idxs(cam_epoch,axondata):
    """exctract the sync pulse from the camera epochs"""
    sync_signal = np.array(axondata['CamSync'])
    sync_signal = sync_signal[cam_epoch]
    frame_idxs = [x[0]+cam_epoch[0] for x in idx_by_thresh(sync_signal*-1,-3.5)]
    frame_idxs[0] -=1
    return frame_idxs

def idx_by_thresh(signal,thresh = 0.1):
    idxs = np.squeeze(np.argwhere(signal > thresh))
    split_idxs = np.squeeze(np.argwhere(np.diff(idxs) > 1))
    idx_list = np.split(idxs,split_idxs)
    idx_list = [x[1:] for x in idx_list]
    return idx_list
                
def get_axon_signals(filename):
    from neo.io.axonio import AxonIO
    reader = AxonIO(filename=filename)
    blocks = reader.read()
    header = reader.read_header()
    channel_names = [info['ADCChNames'] for info in header['listADCInfo']]
    channel_units = [info['ADCChUnits'] for info in header['listADCInfo']]
    times = blocks[0].segments[0].analogsignals[0].times
    sampling_period = blocks[0].segments[0].analogsignals[0].sampling_period
    times.units = 's'
    sampling_period.units = 's'
    times = np.array(times)
    sampling_period = np.float64(sampling_period)
    signals = [np.array(x) for x in blocks[0].segments[0].analogsignals]
    signals = dict(zip(channel_names,signals))
    signals['times'] = times
    #signals['sampling_period'] = sampling_period
    #signals['time_units'] = 's'
    return signals

def load_wbkin_file(kine_filename):
    """load the matlab generated wb kine and append with some info for convenience"""
    kine_data = scipy.io.loadmat(kine_filename)
    ##now to make life easier add the frame numbers to the dictionary
    first_track = np.argwhere(~np.isnan(kine_data['eta_L']))[0][0]+1
    last_track = np.shape(kine_data['eta_R'])[0]
    #sanity check
    def check_first_frame():
        kfn = kine_filename.split('/')[-1]
        flytracks_path = kine_filename.replace(kfn,'flytracks/')
        #get the list of frames
        tracklist = filter(lambda x: x.startswith('fly'), os.listdir(flytracks_path))
        framenums = [np.int(s.strip('fly.mat')) for s in tracklist]
        return np.min(framenums),np.max(framenums)
    assert first_track == check_first_frame()[0],(first_track,check_first_frame()[0])
    assert last_track == check_first_frame()[1],(last_track,check_first_frame()[1])
    kine_data['first_track'] = np.array([first_track])
    kine_data['last_track'] = np.array([last_track])
    kine_data['frame_nums'] = np.arange(1,last_track)
    return kine_data

def load_flytracks_files(sequence_path):
        """convenience function to load the sequence from fly tracks function will cat
        the frame numbers into the first row the kine matrx, also the untracked frames
        before the start of the sequence are padded with NaNs - tries to emulate the same 
        format as the WBkin file"""
        flytracks_path = sequence_path + 'flytracks/'
        #get the list of frames
        tracklist = filter(lambda x: x.startswith('fly'), os.listdir(flytracks_path))
        framenums = [np.int(s.strip('fly.mat')) for s in tracklist]
        #sort the files by frame number
        tracklist = [x for (y,x) in sorted(zip(framenums,tracklist))]
        tracklist = [flytracks_path + x for x in tracklist]
        #load the data from the .mat files
        mats = [scipy.io.loadmat(trk)['xh'].copy() for trk in tracklist]
        mats = np.array([np.squeeze(np.pad(np.squeeze(mat),(0,15-np.shape(mat)[0]),'constant')) for mat in mats])
        #since the frames are sorted - now sort the frame numbers
        framenums = np.squeeze(sorted(framenums))
        #cat the frame numbers onto the kine data
        seq = np.concatenate((framenums[:,np.newaxis],mats),axis = 1)
        #now pad the matrix with NaNs so that it starts at frame 0
        start_frame = seq[0,0]
        pad_seq = np.pad(seq,((start_frame-1,0),(0,0)),'constant')
        pad_seq[:start_frame-1,0] = np.arange(1,start_frame)
        pad_seq[:start_frame-1,1:] = np.NAN
        return pad_seq
        
def butter_bandpass(lowcut, highcut, sampling_period, order=5):
    sampling_frequency = 1.0/sampling_period
    nyq = 0.5 * sampling_frequency
    low = lowcut / nyq
    high = highcut / nyq
    b, a = scipy.signal.butter(order, [low, high], btype='band')
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, sampling_period, order=5):
    b, a = butter_bandpass(lowcut, highcut, sampling_period, order=order)
    y = scipy.signal.filtfilt(b, a, data)
    return y

def butter_lowpass(lowcut, sampling_period, order=5):
    import scipy.signal
    sampling_frequency = 1.0/sampling_period
    nyq = 0.5 * sampling_frequency
    low = lowcut / nyq
    b, a = scipy.signal.butter( order, low, btype='low')
    return b, a

def butter_lowpass_filter(data, lowcut, sampling_period, order=5):
    import scipy.signal
    b, a = butter_lowpass(lowcut, sampling_period, order=order)
    y = scipy.signal.filtfilt(b, a, data)
    return y
    
def fit_fourier(strk_mtrx,p_init):
    num_strokes = np.shape(strk_mtrx)[0]
    reshaped = np.squeeze(np.reshape(strk_mtrx,(np.size(strk_mtrx),1)))
    phases = np.linspace(0,2*np.pi*num_strokes,np.size(strk_mtrx))
    y_fit = reshaped[~np.isnan(reshaped)]
    x_fit = phases[~np.isnan(reshaped)]
    from scipy import optimize
    ##speed things up by pre-computing the sin and cosine values
    order = (len(p_init)-1)/2
    n = np.arange(1,order+1)
    onesmat = np.ones((len(n),len(x_fit)))
    phase_mtrx = ((onesmat*x_fit).T*n).T
    cos_mtrx = np.cos(phase_mtrx)
    sin_mtrx = np.sin(phase_mtrx)
    p1,msg = optimize.leastsq(errfunc, p_init[:], args=(cos_mtrx,sin_mtrx,np.rad2deg(y_fit)))
    return p1
    
def fourier_pcomp(p,cos_mtrx,sin_mtrx):
    cp = np.array(p[1:-1:2])[:,np.newaxis]
    sp = np.array(p[2::2])[:,np.newaxis]
    hmtrx = cos_mtrx*cp + sin_mtrx*sp
    return p[0] + np.sum(hmtrx,axis = 0)
    
def fourier(phase,p):
    order = (len(p)-1)/2
    n = np.arange(1,order+1)
    onesmat = np.ones((len(n),len(phase)))
    phase_mtrx = ((onesmat*phase).T*n).T
    cp = np.array(p[1:-1:2])[:,np.newaxis]
    sp = np.array(p[2::2])[:,np.newaxis]
    hmtrx = np.cos(phase_mtrx)*cp + np.sin(phase_mtrx)*sp
    return p[0] + np.sum(hmtrx,axis = 0)

def errfunc(p,cos_mtrx,sin_mtrx,y):
    return fourier_pcomp(p,cos_mtrx,sin_mtrx)-y

def update_dset(dset,key,value):
    if not(key in dset.keys()):
        dset[key] = value
    else:
        del(dset[key])
        dset[key] = value

exp_map = {'lr_blob_expansion':HSVExperiment,
           'img_starfield_t2_rep1':IMGExperiment,
           'img_nsf_pilot_t2_rep1':IMGExperiment,
           'img_starfields2_t2_rep1':IMGExperiment,
           'img_starfields2_t2_rep2':IMGExperiment}
