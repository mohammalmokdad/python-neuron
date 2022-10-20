# Test script to generate the an ISI plot with a ramping current, using charesterestics from cell.hoc

from neuron import h
from neuron.units import um, mV, ms
import efel
import plotly
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
h.load_file("stdrun.hoc")

h.load_file('UsefulStuff/cell.hoc')

soma=h.soma
dend=h.dendrite

RC=h.RClamp(soma(0.5))
RC.delay = 500*ms
RC.dur = 2000*ms
RC.pkamp = 60
RC.bias=0

time=h.Vector().record(h._ref_t)
voltage=h.Vector().record(soma(0.5)._ref_v)
curr=h.Vector().record(RC._ref_i)

h.finitialize(-68.5)
h.continuerun(3000)


trace = {"T": time, "V": voltage, "stim_start": [500 * ms], "stim_end": [2500 * ms]}
traces = [trace]
features = efel.getFeatureValues(traces, ["AP_amplitude", "ISIs", "spike_half_width", "AP_begin_time"])
ISIs=features[0]['ISIs']


fig=px.line(x=time, y=curr)
fig = fig.update_layout({
    "xaxis_title": "Time (ms)",
    "yaxis_title": "Current (nA)",
    "title":'Current-time plot'
})
fig.show()

fig1 =px.line(x=time, y=voltage)
fig1 = fig1.update_layout({
    "xaxis_title": "Time (ms)",
    "yaxis_title": "Voltage (V)",
    "title":'Voltage-time plot'
})
fig1.show()



counts,bins = np.histogram(ISIs,bins=26,range=(0,130))
plt.hist(bins[:-1], bins, weights=counts)
plt.show()