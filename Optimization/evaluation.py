# Optimization evalation function, takes in values for lengths and outputs how far away they are from targets
from neuron import h
from neuron.units import um, mV, ms
import numpy as np
h.load_file("stdrun.hoc")
# pylint: disable=W0212


def evaluate(individual):
    """
    Evaluate a neuron model with parameters somalen and dendlen, extracts
    tau and input resistance then outputs the difference between the target as
    abs(target_Rn - imp) and 
    abs(target_tau - t_tau)
    """
    target_Rn=0.9
    target_tau=8
    soma=h.Section(name="soma")
    soma.diam=22
    soma.L=individual[0]
    soma.Ra=70
    soma.cm=individual[2]
    soma.insert('pas')
    soma.e_pas=-70
    soma.g_pas=0.0048

    dend=h.Section(name="dend")
    dend.diam=70
    dend.L=individual[1]
    dend.Ra=115
    dend.cm=individual[2]/10
    dend.insert('pas')
    dend.e_pas=-70
    dend.g_pas=0.0048

    dend.connect(soma,0)

    impcalc=h.Impedance()
    impcalc.loc(soma(0.5))
    impcalc.compute(0)
    imp=impcalc.input(soma(0.5))

    # Current Clamp
    stim_start=100
    stim_dur=300

    ic=h.IClamp(soma(0.5))
    ic.delay = stim_start
    ic.dur = stim_dur
    ic.amp = 1

    t=h.Vector().record(h._ref_t)
    v=h.Vector().record(soma(0.5)._ref_v)


    h.finitialize(-70*mV)
    h.continuerun(stim_start+stim_dur+100)

    # tau calc
    start_idx=int((stim_start/h.dt) - 1)
    stop_idx=int(((stim_start+stim_dur)/h.dt)+1)
    v_np=np.asarray(v)
    v_np_mod=v_np[start_idx:stop_idx]
    maxv=np.amax(v_np_mod)
    minv=np.amin(v_np_mod)
    diffv=maxv-minv
    v_tau=minv+diffv*(1-(1/np.exp(1)))
    idx=(np.abs(v_np_mod - v_tau)).argmin()
    t_tau=t[idx+start_idx]-stim_start

    return np.abs(target_Rn - imp)+np.abs(target_tau - t_tau)
    # return np.abs(target_Rn - imp), \
    #     np.abs(target_tau - t_tau)