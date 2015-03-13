import flylib
import db_access as dba
fly_db = dba.get_db()
import numpy as np

GMR22H05_list = [308,309,310,311,312,313,314,315,316,317,327,328] #range(317,326)
GMR22H05_swarm = flylib.Squadron(fly_db,GMR22H05_list)
GMR39E01_list = [318,319,320,321,322,323,324,325,329,330,331,332,333,334,335,336]
GMR39E01_swarm = flylib.Squadron(fly_db,GMR39E01_list)
GMR31E10_list = [337,338,339,340,341,342,343,344,345,346,347,348]
GMR31E10_swarm = flylib.Squadron(fly_db,GMR31E10_list)
GMR29E05_list = [349,350,351,352,353,354,355,356,357,358,359,360]
GMR29E05_swarm = flylib.Squadron(fly_db,GMR29E05_list)

GMR22H05_GFP_list = [370,371,372,373,380,381,382,383]
GMR22H05_GFP_swarm = flylib.Squadron(fly_db,GMR22H05_GFP_list)

GMR31E10_GFP_list = [361,362,363,364,365,384,385,386]
GMR31E10_GFP_swarm = flylib.Squadron(fly_db,GMR31E10_GFP_list)

GMR29E05_GFP_list = [366,367,368,369,376,377,378,379]
GMR29E05_GFP_swarm = flylib.Squadron(fly_db,GMR29E05_GFP_list)

swarms = {'GMR22H05':GMR22H05_swarm,
          'GMR39E01':GMR39E01_swarm,
          'GMR31E10':GMR31E10_swarm,
          'GMR29E05':GMR29E05_swarm,
          'GMR22H05_GFP':GMR22H05_GFP_swarm,
          'GMR31E10_GFP':GMR31E10_GFP_swarm,
          'GMR29E05_GFP':GMR29E05_GFP_swarm
         }

encode = {'regressive':1,'descending':2,'progressive':3,'ascending':4,'flow_right':6,'flow_left':5}
decode = dict()

for key,value in zip(encode.keys(),encode.values()):
    decode[value] = key
   

def get_cond(fly,trial):
    """extact the experimental condition from a trial"""
    expmnt = fly.experiments.values()[0]
    sigs = expmnt.exp_record['tiff_data']['axon_framebase']
    cond_data = np.array(sigs['StimCond'])[trial]
    val = np.around(np.mean(cond_data[cond_data>0.5]))
    if np.isnan(val):
        raise ValueError
    return val