# Functions for calculating the VA for each of the motorneurons from Burke et. al

import numpy as np

# calculations for VA DS DC

def M1(D_path):
    a=559.5900739428298
    b=310.72431966327235
    cumarea=1-(1/(1-np.exp(-a/b)+np.exp((D_path-a)/b)))
    return cumarea

def M2(D_path):
    a=592.9432100308615
    b=284.170655892884
    cumarea=1-(1/(1-np.exp(-a/b)+np.exp((D_path-a)/b)))
    return cumarea

def M3(D_path):
    a=558.9825607401616
    b=368.024382347019
    cumarea=1-(1/(1-np.exp(-a/b)+np.exp((D_path-a)/b)))
    return cumarea

def M4(D_path):
    a=679.2968391773574
    b=344.9262571957527
    cumarea=1-(1/(1-np.exp(-a/b)+np.exp((D_path-a)/b)))
    return cumarea

def M6(D_path):
    a=457.18287996963613
    b=372.12955854433187
    cumarea=1-(1/(1-np.exp(-a/b)+np.exp((D_path-a)/b)))
    return cumarea
