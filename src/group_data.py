import flylib
import db_access as dba
#fly_db = dba.get_db()
import numpy as np


genotype_nicknames = {'GMR10A12': '+;P{20XUAS-IVS-GCaMP6f}attP40/+;P{y[+t7.7] w[+mC]=GMR10A12-GAL4}attP2/+',
                     'GMR10A12_GFP': '+;10XUAS-EGFP/+;P{y[+t7.7] w[+mC]=GMR10A12-GAL4}attP2/+',
                     'GMR22H05': '+;P{20XUAS-IVS-GCaMP6f}attP40/+;P{y[+t7.7] w[+mC]=GMR22H05-GAL4}attP2/+',
                     'GMR22H05_GFP': '+;10XUAS-EGFP/+;P{y[+t7.7] w[+mC]=GMR22H05-GAL4}attP2/+',
                     'GMR29E05': '+;P{20XUAS-IVS-GCaMP6f}attP40/+;P{y[+t7.7] w[+mC]=GMR29E05-GAL4}attP2/+',
                     'GMR29E05_GFP': '+;10XUAS-EGFP/+;P{y[+t7.7] w[+mC]=GMR29E05-GAL4}attP2/+',
                     'GMR31E10': '+;P{20XUAS-IVS-GCaMP6f}attP40/+;P{y[+t7.7] w[+mC]=GMR31E10-GAL4}attP2/+',
                     'GMR31E10_GFP': '+;10XUAS-EGFP/+;P{y[+t7.7] w[+mC]=GMR31E10-GAL4}attP2/+',
                     'GMR39E01': '+;P{20XUAS-IVS-GCaMP6f}attP40/+;P{y[+t7.7] w[+mC]=GMR39E01-GAL4}attP2/+',
                     'GMR39E01_GFP': '+;10XUAS-EGFP/+;P{y[+t7.7] w[+mC]=GMR39E01-GAL4}attP2/+',
                     'GMR74F03': '+;P{20XUAS-IVS-GCaMP6f}attP40/+;P{y[+t7.7] w[+mC]=GMR74F03-GAL4}attP2/+',
                     'GMR75B06': '+;P{20XUAS-IVS-GCaMP6f}attP40/+;P{y[+t7.7] w[+mC]=GMR75B06-GAL4}attP2/+',
                     'GMR75B06_GFP': '+;10XUAS-EGFP/+;P{y[+t7.7] w[+mC]=GMR75B06-GAL4}attP2/+',
                     'GMR40D04': '+;P{20XUAS-IVS-GCaMP6f}attP40/+;P{y[+t7.7] w[+mC]=GMR40D04-GAL4}attP2/+'}


GMR22H05_list = [308,309,310,311,312,314,315,316,317,327,328,453,455,456,461,462,463,466,467,468,469,470] #R range(317,326) 
GMR22H05_swarm = flylib.NetSquadron(GMR22H05_list)
GMR39E01_list = [318,319,320,321,322,323,324,325,329,330,331,332,333,334,335,336] #S
GMR39E01_swarm = flylib.NetSquadron(GMR39E01_list)
GMR31E10_list = [337,338,339,340,341,342,343,344,345,346,347,348,458,459,460] #R
GMR31E10_swarm = flylib.NetSquadron(GMR31E10_list)
GMR29E05_list = [349,350,351,352,353,354,355,356,357,358,359,360] #R
GMR29E05_swarm = flylib.NetSquadron(GMR29E05_list)

GMR10A12_list = [387,388,389,399,400,401,408,409,410,417,418,419,450,452] #R
GMR10A12_swarm = flylib.NetSquadron(GMR10A12_list)

GMR75B06_list = [393,394,395,402,403,404,405,406,407,420,421,422] #S
GMR75B06_swarm = flylib.NetSquadron(GMR75B06_list)

GMR74F03_list = [396,397,398,411,412,413,414,415,416] #S
GMR74F03_swarm = flylib.NetSquadron(GMR74F03_list)

GMR22H05_pr_list = [471,472,473,474,475,476,477,478,479,480,481,483,484,485,486] # azmuthal tuning - pitch to roll
GMR22H05_pr_swarm = flylib.NetSquadron(GMR22H05_pr_list)

GMR40D04_pr_list = [587, 588, 589, 600, 601, 602, 603, 604, 605, 606, 607] # azmuthal tuning - pitch to roll
GMR40D04_pr_swarm = flylib.NetSquadron(GMR40D04_pr_list)

GMR40D04_ca_list = [615,616] # azmuthal tuning - pitch to roll
GMR40D04_ca_swarm = flylib.NetSquadron(GMR40D04_pr_list)

#GMR22H05_prc_list = [487,488,489,490,491,492,493,494,495,496,497,498,499]
#GMR22H05_prc_list = [488,489,490,491,492,493,494,495,496,497,498]
GMR22H05_prc_list = [488,489,490,491,492,493,494,495,496,497,498,499,500,501,502] # azmuthal tuning - pitch to roll as well as motion control stimuli

GMR22H05_prc_swarm = flylib.NetSquadron(GMR22H05_prc_list)
###################
###################

GMR22H05_GFP_list = [370,371,372,373,380,381,382,383]
GMR22H05_GFP_swarm = flylib.NetSquadron(GMR22H05_GFP_list)

GMR31E10_GFP_list = [361,362,363,364,365,384,385,386]
GMR31E10_GFP_swarm = flylib.NetSquadron(GMR31E10_GFP_list)

GMR29E05_GFP_list = [366,367,368,369,376,377,378,379]
GMR29E05_GFP_swarm = flylib.NetSquadron(GMR29E05_GFP_list)

GMR74F03_GFP_list = [430,431,432,433]
GMR74F03_GFP_swarm = flylib.NetSquadron(GMR74F03_GFP_list)

GMR10A12_GFP_list = [434,435,436,437,442,443]
GMR10A12_GFP_swarm = flylib.NetSquadron(GMR10A12_GFP_list)

GMR75B06_GFP_list = [438,439,440,441,444,445,446,447]
GMR75B06_GFP_swarm = flylib.NetSquadron(GMR75B06_GFP_list)

GMR39E01_GFP_list = [503,504,505,506]
GMR39E01_GFP_swarm = flylib.NetSquadron(GMR39E01_GFP_list)


swarms = {'GMR22H05':GMR22H05_swarm,
          'GMR39E01':GMR39E01_swarm,
          'GMR31E10':GMR31E10_swarm,
          'GMR29E05':GMR29E05_swarm,
          'GMR10A12':GMR10A12_swarm,
          'GMR75B06':GMR75B06_swarm,
          'GMR74F03':GMR74F03_swarm,
          'GMR22H05_GFP':GMR22H05_GFP_swarm,
          'GMR31E10_GFP':GMR31E10_GFP_swarm,
          'GMR39E01_GFP':GMR39E01_GFP_swarm,
          'GMR29E05_GFP':GMR29E05_GFP_swarm,
          'GMR74F03_GFP':GMR74F03_GFP_swarm,
          'GMR10A12_GFP':GMR10A12_GFP_swarm,
          'GMR75B06_GFP':GMR75B06_GFP_swarm,
          'GMR22H05_pr':GMR22H05_pr_swarm,
          'GMR40D04_pr':GMR40D04_pr_swarm,
          'GMR22H05_prc':GMR22H05_prc_swarm,
         }

exp_swarms = {'GMR22H05':GMR22H05_swarm,
          'GMR39E01':GMR39E01_swarm,
          'GMR31E10':GMR31E10_swarm,
          'GMR29E05':GMR29E05_swarm,
          'GMR10A12':GMR10A12_swarm,
          'GMR75B06':GMR75B06_swarm,
          'GMR74F03':GMR74F03_swarm,
         }

ctrl_swarms = {
          'GMR22H05_GFP':GMR22H05_GFP_swarm,
          'GMR39E01_GFP':GMR39E01_GFP_swarm,
          'GMR31E10_GFP':GMR31E10_GFP_swarm,
          'GMR29E05_GFP':GMR29E05_GFP_swarm,
          'GMR74F03_GFP':GMR74F03_GFP_swarm,
          'GMR10A12_GFP':GMR10A12_GFP_swarm,
          'GMR75B06_GFP':GMR75B06_GFP_swarm
         }

ptch_roll_swarms = {
    'GMR22H05_pr':GMR22H05_pr_swarm,
    'GMR22H05_prc':GMR22H05_prc_swarm,
}

def decode_cond_step_yaw(cond_data):
    """extact the experimental condition for a trial from a 'step_yaw' type experiment"""
    decode = {1:'progressive',2:'descending',3:'regressive',4:'ascending',5:'yaw_left',6:'yaw_right'}
    #cond_data = np.array(sigs['StimCond'])[trial]
    val = np.around(np.mean(cond_data[cond_data>0.5]))
    if np.isnan(val):
        raise ValueError
    return decode[val]

def decode_cond_pitch_roll(cond_data):
    """extact the experimental condition for a trial from a 'pitch_roll' type experiment"""
    decode = dict()
    [decode.update({i:'pth_roll_%s'%p}) for i,p in enumerate(range(0,360,30))]
    val = np.around(np.mean((cond_data[cond_data>0.5]-1)*360/(30*9)))
    if np.isnan(val):
        raise ValueError
    return decode[val]

def decode_cond_pitch_roll_ctrl(cond_data):
    """extact the experimental condition for a trial from a 'pitch_roll_ctrl' type experiment"""
    decode = dict()
    [decode.update({i:'pth_roll_%s'%p}) for i,p in enumerate(range(0,360,30))]
    decode.update({12:'pth_roll_multipole'})
    decode.update({13:'pth_roll_phsrndm'})
    val = np.around(np.mean((cond_data[cond_data>0.5]-1)*len(decode)/9))
    if np.isnan(val):
        raise ValueError
    return decode[val]


decode_map = {'step_yaw_mod1':decode_cond_step_yaw,
              'step_ptch_roll':decode_cond_pitch_roll,
              'step_ptch_roll_ctrl':decode_cond_pitch_roll_ctrl}

#GMR22H05_pr_swarm.get_cond = get_cond_pitch_roll
#GMR22H05_pr_swarm.decode = decode_pitch_roll


def get_update_list(file_name ='nnls_fits_no_bk_dF_F.cpkl', 
                     swarms = swarms,
                     replace = False):
    """ if replace is False this will scan the database to 
    create a 'pathlist' containing just flies that don't have 
    a file with file_name, otherwise all the flies in swarms will be used"""
    import os
    update_flylist = list()
    for swarm_name,swarm in swarms.items():
        #print swarm_name
        for fly in swarm.flies:
            try:
                if not(replace):
                    if os.path.exists(fly.fly_path + file_name):
                        pass
                        #print str(fly.fly_num) + ' exists'
                    else:
                        update_flylist.append(fly)
                else:
                    update_flylist.append(fly)
            except Exception as er:
                print er
    return update_flylist

segmented_fly = 508
muscle_anatomy_dir = '/media/FlyDataC/FlyDB/Fly%04d/'%(segmented_fly)

signal_plot_list = ['wb_frequency','Ph1',
                    'b1','b2','b3',
                    'i1','i2',
                    'iii1','iii24','iii3',
                    'hg1','hg2','hg3','hg4',
                    'tpv','tpd','ttm','pr']

muscle_plot_list = signal_plot_list[2:]

b_list = ['b1','b2','b3']
i_list = ['i1','i2']
iii_list = ['iii1','iii24','iii3']
hg_list = ['hg1','hg2','hg3','hg4']
id_list = ['tpv','tpd','ttm','pr']

signal_plot_info = {'wb_frequency':
                       {'ax_label':'freq',
                        'transform':lambda x:x},
                   'Ph0':
                       {'ax_label':'lwing \n amp',
                       'transform':lambda x:np.rad2deg(x/5.0)},
                   'Ph1':
                       {'ax_label':'rwing \n amp',
                       'transform':lambda x:np.rad2deg(x/5.0)},
                   'Ph2':
                       {'ax_label':'lmr \n amp',
                       'transform':lambda x:np.rad2deg(x/5.0)},
                   'StimCond':
                       {'ax_label':'Stimulus',
                       'transform':lambda x:x},
                   'b1':
                       {'ax_label':'b1',
                       'transform':lambda x:x},
                   'b2':
                       {'ax_label':'b2',
                       'transform':lambda x:x},
                   'b3':
                       {'ax_label':'b3',
                       'transform':lambda x:x},
                   'i1':
                       {'ax_label':'i1',
                       'transform':lambda x:x},
                   'i2':
                       {'ax_label':'i2',
                       'transform':lambda x:x},
                   'iii1':
                       {'ax_label':'iii1',
                       'transform':lambda x:x},
                   'iii24':
                       {'ax_label':'iii24',
                       'transform':lambda x:x},
                   'iii3': 
                       {'ax_label':'iii3', 
                       'transform':lambda x:x},
                   'hg1':
                       {'ax_label':'hg1',
                       'transform':lambda x:x},
                   'hg2':
                       {'ax_label':'hg2',
                       'transform':lambda x:x},
                   'hg3':
                       {'ax_label':'hg3',
                       'transform':lambda x:x},
                   'hg4':
                       {'ax_label':'hg4',
                       'transform':lambda x:x},
                   'ttm':
                       {'ax_label':'ttm',
                       'transform':lambda x:x},
                   'tpv':
                       {'ax_label':'tpv',
                       'transform':lambda x:x},
                   'tpd':
                       {'ax_label':'tpd',
                       'transform':lambda x:x},
                   'ps':
                       {'ax_label':'ps',
                       'transform':lambda x:x},
                   'nm':
                       {'ax_label':'nm',
                       'transform':lambda x:x},
                   'pr':
                       {'ax_label':'pr',
                       'transform':lambda x:x},
                   'Xpos':
                       {'ax_label':'Xpos',
                       'transform':lambda x:x},
                   'Ypos':
                       {'ax_label':'Ypos',
                       'transform':lambda x:x}}
