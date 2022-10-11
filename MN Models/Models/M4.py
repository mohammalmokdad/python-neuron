# M4 Motorneuron Type FR, passive parameters generated from PassParams.py
from neuron import h
from neuron.units import um, mV, ms
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
h.load_file("stdrun.hoc")
h.celsius=37

soma=h.Section(name="soma")
soma.diam=35
soma.L=2584
soma.Ra=48.54371
soma.cm=2.15875
soma.insert('pas')
soma.e_pas=-70
soma.g_pas=0.000295730


dend=h.Section(name="dend")
dend.diam=35
dend.L=3316
dend.Ra=48.54371
dend.cm=0.64935
dend.insert('pas')
dend.e_pas=-70
dend.g_pas=0.000073086

dend.connect(soma,0)

# Rn calc
impcalc=h.Impedance()
impcalc.loc(soma(0.5))
impcalc.compute(0)
imp=impcalc.input(soma(0.5))
print('Input resistance is %f megahohms' % imp)


# Current Clamp
stim_start=100
stim_dur=300

ic=h.IClamp(dend(0.5))
ic.delay = stim_start
ic.dur = stim_dur
ic.amp = 1

t=h.Vector().record(h._ref_t)
v=h.Vector().record(dend(0.5)._ref_v)


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
print('Time constant tau is %f ms' % t_tau)


# Plotting v-t curve
fig=px.line(x=t, y=v)
fig = fig.update_layout(
    yaxis_range=[-75,-65],
    xaxis_range=[stim_start-20,stim_start+stim_dur+100]
    )
fig = fig.update_layout({
    "xaxis_title": "Time (ms)",
    "yaxis_title": "Voltage (mV)",
    "title":'M4 Motorneuron Voltage Response to 1 nA Current'
})
fig.show()