import flylib
import db_access as dba
fly_db = dba.get_db()
import numpy as np

GMR22H05_list = [308,309,310,311,312,313,314,315,316,317,327,328] #R range(317,326) #S
GMR22H05_swarm = flylib.NetSquadron(GMR22H05_list)
GMR39E01_list = [318,319,320,321,322,323,324,325,329,330,331,332,333,334,335,336] #S
GMR39E01_swarm = flylib.NetSquadron(GMR39E01_list)
GMR31E10_list = [337,338,339,340,341,342,343,344,345,346,347,348] #R
GMR31E10_swarm = flylib.NetSquadron(GMR31E10_list)
GMR29E05_list = [349,350,351,352,353,354,355,356,357,358,359,360] #R
GMR29E05_swarm = flylib.NetSquadron(GMR29E05_list)

GMR10A12_list = [387,388,389,399,400,401,408,409,410,417,418,419,448,449,450,451,452] #R
GMR10A12_swarm = flylib.NetSquadron(GMR10A12_list)

GMR75B06_list = [393,394,395,402,403,404,405,406,407,420,421,422] #S
GMR75B06_swarm = flylib.NetSquadron(GMR75B06_list)

GMR74F03_list = [396,397,398,411,412,413,414,415,416] #S
GMR74F03_swarm = flylib.NetSquadron(GMR74F03_list)

###################
###################

GMR22H05_GFP_list = [370,371,372,373,380,381,382,383]
GMR22H05_GFP_swarm = flylib.NetSquadron(GMR22H05_GFP_list)

GMR31E10_GFP_list = [361,362,363,364,365,384,385,386]
GMR31E10_GFP_swarm = flylib.NetSquadron(GMR31E10_GFP_list)

GMR29E05_GFP_list = [366,367,368,369,376,377,378,379]
GMR29E05_GFP_swarm = flylib.NetSquadron(GMR29E05_GFP_list)

swarms = {'GMR22H05':GMR22H05_swarm,
          'GMR39E01':GMR39E01_swarm,
          'GMR31E10':GMR31E10_swarm,
          'GMR29E05':GMR29E05_swarm,
          'GMR10A12':GMR10A12_swarm,
          'GMR75B06':GMR75B06_swarm,
          'GMR74F03':GMR74F03_swarm,
          'GMR22H05_GFP':GMR22H05_GFP_swarm,
          'GMR31E10_GFP':GMR31E10_GFP_swarm,
          'GMR29E05_GFP':GMR29E05_GFP_swarm
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
          'GMR31E10_GFP':GMR31E10_GFP_swarm,
          'GMR29E05_GFP':GMR29E05_GFP_swarm
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