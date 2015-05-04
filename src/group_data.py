import flylib
import db_access as dba
fly_db = dba.get_db()
import numpy as np

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

GMR22H05_pr_list = [471,472,473,474,475,476,477,478,479,480,481,483,484,485,486]
GMR22H05_pr_swarm = flylib.NetSquadron(GMR22H05_pr_list)
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

GMR39E01_GFP_list = []
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
          'GMR22H05_pr':GMR22H05_pr_swarm
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
    'GMR22H05_pr':GMR22H05_pr_swarm
}

encode = {'regressive':1,'descending':2,'progressive':3,'ascending':4,'flow_right':6,'flow_left':5}
decode = dict()

for key,value in zip(encode.keys(),encode.values()):
    decode[value] = key



def get_cond(fly_path,trial):
    """extact the experimental condition from a trial"""
    #print 'here'
    import h5py
    fly_record = h5py.File(fly_path + 'fly_record.hdf5')
    exp_record = fly_record['experiments'].values()[0]
    sigs = exp_record['tiff_data']['axon_framebase']
    cond_data = np.array(sigs['StimCond'])[trial]
    val = np.around(np.mean(cond_data[cond_data>0.5]))
    if np.isnan(val):
        raise ValueError
    return val


decode_pitch_roll = dict()
[decode_pitch_roll.update({i:'pth_roll_%s'%p}) for i,p in enumerate(range(0,360,30))]

def get_cond_pitch_roll(fly_path,trial):
    """extact the experimental condition from a """
    #print 'here'
    import h5py
    fly_record = h5py.File(fly_path + 'fly_record.hdf5')
    exp_record = fly_record['experiments'].values()[0]
    sigs = exp_record['tiff_data']['axon_framebase']
    cond_data = np.array(sigs['StimCond'])[trial] #-1)*360/(30*9)
    val = np.around(np.mean((cond_data[cond_data>0.5]-1)*360/(30*9)))
    if np.isnan(val):
        raise ValueError
    return val


GMR22H05_pr_swarm.get_cond = get_cond_pitch_roll
GMR22H05_pr_swarm.decode = decode_pitch_roll