# Test script to generate the FI curve with a test cell given by the parameters in the file "ini_2cmpt.hoc"

from neuron import h
from neuron.units import um, mV, ms
import plotly
import plotly.express as px
import numpy as np
h.load_file("stdrun.hoc")

h.load_file('cell.hoc')

soma=h.soma
dend=h.dendrite

spike_times = h.Vector()
nc2 = h.NetCon(h.soma(0.5)._ref_v, None, sec=h.soma)
nc2.threshold = 0 * mV
nc2.record(spike_times)


ic=h.IClamp(soma(0.5))
ic.delay = 500*ms
ic.dur = 1000*ms

testcurrs=np.arange(9.5,60,0.5)
spike_counts=[]
amplitudes=[]
n=0
for curr in testcurrs:
    print(curr)
    ic.amp = curr
    h.finitialize(-68.5)
    h.continuerun(2000)
    if len(spike_times)>n:
        n=len(spike_times)
        spike_counts.append(n)
        amplitudes.append(curr)


fig=px.scatter(x=amplitudes, y=spike_counts, trendline="ols", trendline_options=dict(log_x=True))
fig = fig.update_layout({
    "xaxis_title": "Amplitude of Current (nA)",
    "yaxis_title": "Spikes per sec (Hz)",
    "title":'F-I curve for test cell'
})
fig.show()