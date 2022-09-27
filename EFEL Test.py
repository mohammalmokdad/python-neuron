# Test script to generate the FI curve with a test cell given by the parameters in the file "ini_2cmpt.hoc"

from re import A
from neuron import h
from neuron.units import um, mV, ms
import plotly
import plotly.express as px
import numpy as np
import efel
h.load_file("stdrun.hoc")

h.load_file('cell.hoc')

soma=h.soma
dend=h.dendrite

time=h.Vector().record(h._ref_t)
voltage=h.Vector().record(soma(0.5)._ref_v)

stim_start=500
stim_end=1500

ic=h.IClamp(soma(0.5))
ic.delay = stim_start
ic.dur = stim_end-stim_start
ic.amp = 60

h.finitialize(-68.5)
h.continuerun(2000)

fig=px.line(x=time, y=voltage)
fig = fig.update_layout({
    "xaxis_title": "Time (ms)",
    "yaxis_title": "Voltage (V)",
    "title":'Voltage-time plot'
})

fig.show()

trace={}
trace['T']= time, 
trace["V"]= voltage 
trace['stim_start']= [stim_start]
trace['stim_end']= [stim_end]
traces=[trace]
features = efel.getFeatureValues(traces, ['AP_amplitude', 'ISIs', 'spike_half_width', 'AP_begin_time'])

amps=features[0]['AP_amplitude']
print(amps)
ISIs=features[0]['ISIs']
print(ISIs)
HalfWidth=features[0]['spike_half_width']
print(HalfWidth)
AP_Begin=features[0]['AP_begin_time']
print(AP_Begin)