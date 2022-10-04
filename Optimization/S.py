# Python Script to test out passive properties of different simplified motorneuron types
from neuron import h
from neuron.units import um, mV, ms
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
h.load_file("stdrun.hoc")
h.celsius=37

soma=h.Section(name="soma")
soma.diam=22
soma.L=102.90241125
soma.Ra=115
soma.cm=90.89871662
soma.insert('pas')
soma.e_pas=-70
soma.g_pas=0.0048


dend=h.Section(name="dend")
dend.diam=22
dend.L=2134.69197027
dend.Ra=115
dend.cm=9.089871662
dend.insert('pas')
dend.e_pas=-70
dend.g_pas=0.0048

dend.connect(soma,0)

# Rn calc
impcalc=h.Impedance()
impcalc.loc(soma(0.5))
impcalc.compute(0)
imp=impcalc.input(soma(0.5))
print('Input resistance is %f megahohms' % imp)


# Current Clamp
stim_start=100
stim_dur=100

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
print('Time constant tau is %f ms' % t_tau)


# Plotting v-t curve
fig=px.line(x=t, y=v)
fig = fig.update_layout(
    yaxis_range=[-71,-68],
    xaxis_range=[80,240]
    )
fig = fig.update_layout({
    "xaxis_title": "Time (ms)",
    "yaxis_title": "Voltage (mV)",
    "title":'S Motorneuron Voltage Response to 1 nA Current'
})
fig.show()