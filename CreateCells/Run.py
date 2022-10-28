from neuron import h
from neuron.units import um, mV, ms
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import efel

import createmn
h.load_file("stdrun.hoc")


createmn.createmn("CreateCells/neuronactive.csv","CreateCells/neuronpassive.csv")

import init
import CreatedCells.M1 as cell
soma,dend=init.init(h)

cell.neuron(soma,dend,h)

# Rn calc
impcalc=h.Impedance()
impcalc.loc(dend(0.5))
impcalc.compute(0)
imp=impcalc.input(soma(0.5))
print('Input resistance is %f megahohms' % imp)

# Ramp current clamp

stim_start=1000
stim_dur=6000
RC=h.RClamp(soma(0.5))
RC.delay = stim_start
RC.dur = stim_dur
RC.pkamp = 20
RC.bias=-0

time=h.Vector().record(h._ref_t)
voltage=h.Vector().record(soma(0.5)._ref_v)
curr=h.Vector().record(RC._ref_i)

h.finitialize(-68.5)
h.continuerun(2*stim_start+stim_dur)


trace = {"T": time, "V": voltage, "stim_start": [stim_start], "stim_end": [stim_start+stim_dur]}
traces = [trace]
features = efel.getFeatureValues(traces, ["AP_amplitude", "ISIs", "spike_half_width", "AP_begin_time"])
ISIs=features[0]['ISIs']
AP_begin=features[0]['AP_begin_time']
instfiringfreq=1/(1e-3*ISIs)

# Finding currents for each spike for FI curve

Half_times=[]
for i in np.arange(0,len(AP_begin)-1):
    Half_times.append((AP_begin[i]+AP_begin[i+1])/2)

testcurrs=[]
testtimes=[]
for i in np.arange(0,len(Half_times)):
    idx=(np.abs(time - Half_times[i])).argmin()
    testtimes.append(time[idx])
    testcurrs.append(curr[idx])

fig=make_subplots(
    rows=2, cols=2, subplot_titles=("Current-time Plot", "Voltage-time Plot", "Firing Rate-Current Plot", "Firing Rate-Time Plot")
)
fig.update_layout(showlegend=False)
fig.add_trace(
    go.Scatter(x=time, y=curr),
    row=1,col=1
)

fig.add_trace(
    go.Scatter(x=time, y=voltage),
    row=1,col=2
)

fig.add_trace(
    go.Scatter(x=testcurrs, y=instfiringfreq,mode='markers'),
    row=2,col=1
)

fig.add_trace(
    go.Scatter(x=testtimes, y=instfiringfreq,mode='markers'),
    row=2,col=2
)

fig.update_xaxes(title_text="Time (ms)", row=1, col=1)
fig.update_xaxes(title_text="Time (ms)", row=1, col=2)
fig.update_xaxes(title_text="Current (nA)", row=2, col=1)
fig.update_xaxes(title_text="Time (ms)", row=2, col=2)

fig.update_yaxes(title_text="Current (nA)", row=1, col=1)
fig.update_yaxes(title_text="Voltage (V)", row=1, col=2)
fig.update_yaxes(title_text="Instantaneous Firing Frequency (imp/s)", row=2, col=1)
fig.update_yaxes(title_text="Instantaneous Firing Frequency (imp/s)", row=2, col=2)

fig.show()