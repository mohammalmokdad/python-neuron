# Functions for calculating the VA for each of the motorneurons from Burke et. al

import numpy as np

# calculations for VA DS DC

def DS_DC_M1(D_path):
    alph1=1020.8
    alph2=307.7
    VA=1/(1-np.exp(-alph1/alph2)+np.exp((D_path-alph1)/alph2))
    return VA

def DS_DC_M2(D_path):
    alph1=635.2
    alph2=439.5
    VA=1/(1-np.exp(-alph1/alph2)+np.exp((D_path-alph1)/alph2))
    return VA

def DS_DC_M3(D_path):
    alph1=327.9
    alph2=469.6
    VA=1/(1-np.exp(-alph1/alph2)+np.exp((D_path-alph1)/alph2))
    return VA

def DS_DC_M4(D_path):
    alph1=374.2
    alph2=504.8
    VA=1/(1-np.exp(-alph1/alph2)+np.exp((D_path-alph1)/alph2))
    return VA

def DS_DC_M6(D_path):
    alph1=861.9
    alph2=268.3
    VA=1/(1-np.exp(-alph1/alph2)+np.exp((D_path-alph1)/alph2))
    return VA

# calculations for VA SD DC

def SD_DC_M1(D_path):
    lam=2678.7
    VA=np.exp(-D_path/lam)
    return VA

def SD_DC_M2(D_path):
    lam=3085.6
    VA=np.exp(-D_path/lam)
    return VA

def SD_DC_M3(D_path):
    lam=2763.7
    VA=np.exp(-D_path/lam)
    return VA

def SD_DC_M4(D_path):
    lam=1945.5
    VA=np.exp(-D_path/lam)
    return VA

def SD_DC_M6(D_path):
    lam=2156.4
    VA=np.exp(-D_path/lam)
    return VA

# calculations for VA SD AC

def SD_AC_M1(D_path):
    lam=420.1
    VA=np.exp(-D_path/lam)
    return VA

def SD_AC_M2(D_path):
    lam=437.1
    VA=np.exp(-D_path/lam)
    return VA

def SD_AC_M3(D_path):
    lam=402.3
    VA=np.exp(-D_path/lam)
    return VA

def SD_AC_M4(D_path):
    lam=373.1
    VA=np.exp(-D_path/lam)
    return VA

def SD_AC_M6(D_path):
    lam=464.7
    VA=np.exp(-D_path/lam)
    return VA
