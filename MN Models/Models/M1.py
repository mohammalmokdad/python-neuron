# M1 Motorneuron Type S, passive parameters generated from PassParams.py
from neuron import h
from neuron.units import um, mV, ms
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
import efel
h.load_file("stdrun.hoc")
h.celsius=37

soma=h.Section(name="soma")
soma.diam=25
soma.L=4264
soma.Ra=11.3073
soma.cm=0.89162

soma.insert('pas')
soma.e_pas=-70
soma.g_pas=0.000086456

soma.insert("gh")
soma.half_gh=-77
soma.ghbar_gh=3e-5

soma.insert('na3rp')
soma.gbar_na3rp = 0.05
soma.ar_na3rp = 0.4
soma.sh_na3rp = 12

soma.insert('naps')
soma.gbar_naps = 0.0005
soma.ar_naps = 0.4
soma.sh_naps = 22

soma.insert('kdrRL')
soma.gMax_kdrRL = 0.03
soma.ek=-80

soma.insert('mAHP')
soma.gcamax_mAHP = 8e-06
soma.gkcamax_mAHP = 0.0011
soma.taur_mAHP = 70
soma.eca=60



dend=h.Section(name="dend")
dend.connect(soma,0)
dend.diam=25
dend.L=3636
dend.Ra=11.3073
dend.cm=1.10794
dend.insert('pas')
dend.e_pas=-70
dend.g_pas=0.000105686

dend.insert("gh")
dend.half_gh=-77
dend.ghbar_gh=3e-5


dend.insert('L_Ca')
dend.gcabar_L_Ca = 0.00013
dend.ecaL=60

dend.insert('kca2')
dend.g_kca2 = 1.8e-05
dend.depth2_kca2 = 100
dend.taur2_kca2 = 200
dend.ek=-80

h.qinf_na3rp = 8
h.thinf_na3rp = -50
h.vslope_naps = 6
h.mvhalfca_mAHP = -20
h.tmin_kdrRL = 0.8
h.taumax_kdrRL = 20
h.mVh_kdrRL = -21
h.theta_m_L_Ca = -42
h.tau_m_L_Ca = 40

# # Current Clamp
# stim_start=500
# stim_dur=190

# ic=h.IClamp(soma(0.5))
# ic.delay = stim_start
# ic.dur = stim_dur
# ic.amp = 0

# time=h.Vector().record(h._ref_t)
# voltage=h.Vector().record(soma(0.5)._ref_v)
# curr=h.Vector().record(ic._ref_i)

# h.finitialize(-20*mV)
# h.continuerun(stim_start+stim_dur+500)

# fig=px.line(x=time, y=curr)
# fig = fig.update_layout({
#     "xaxis_title": "Time (ms)",
#     "yaxis_title": "Current (nA)",
#     "title":'Current-time plot'
# })
# fig.show()

# fig1 =px.line(x=time, y=voltage)
# fig1 = fig1.update_layout({
#     "xaxis_title": "Time (ms)",
#     "yaxis_title": "Voltage (V)",
#     "title":'Voltage-time plot'
# })
# fig1.show()

# Rn calc
impcalc=h.Impedance()
impcalc.loc(dend(0.5))
impcalc.compute(0)
imp=impcalc.input(soma(0.5))
print('Input resistance is %f megahohms' % imp)

# Ramp current clamp

stim_start=1000
stim_dur=5000
RC=h.RClamp(dend(0.5))
RC.delay = stim_start
RC.dur = stim_dur
RC.pkamp = 30
RC.bias=0

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

# # Current Clamp
# stim_start=500
# stim_dur=1000

# ic=h.IClamp(soma(0.5))
# ic.delay = stim_start
# ic.dur = stim_dur

# t=h.Vector().record(h._ref_t)
# v=h.Vector().record(soma(0.5)._ref_v)



# # Plotting FI curve

# trace = {"T": t, "V": v, "stim_start": [stim_start], "stim_end": [stim_start+stim_dur+500]}
# traces = [trace]

# testcurrs=np.arange(0,60,0.5)
# spike_counts=[]
# amplitudes=[]

# ic.amp = testcurrs[0]
# h.finitialize(-70*mV)
# h.continuerun(stim_start+stim_dur+500)
# features = efel.getFeatureValues(traces, ["Spikecount"])
# spikecount=features[0]['Spikecount']
# n=spikecount[0]
# spike_counts.append(n)
# amplitudes.append(testcurrs[0])

# for curr in testcurrs:
#     print(curr)
#     ic.amp = curr
#     h.finitialize(-70*mV)
#     h.continuerun(stim_start+stim_dur+500)
#     features = efel.getFeatureValues(traces, ["Spikecount"])
#     spikecount=features[0]['Spikecount']
#     if spikecount[0]>n:
#         n=spikecount[0]
#         spike_counts.append(n)
#         amplitudes.append(curr)

# fig=px.scatter(x=amplitudes, y=spike_counts)
# fig = fig.update_layout({
#     "xaxis_title": "Amplitude of Current (nA)",
#     "yaxis_title": "Spikes per sec (Hz)",
#     "title":'F-I curve for test cell'
# })
# fig.show()



# # Plotting v-t curve
# fig=go.Figure()
# for curr in np.arange(10,30,1):
#     ic.amp=curr
#     h.finitialize(-70*mV)
#     h.continuerun(stim_start+stim_dur+500)
#     fig.add_trace(go.Scatter(x=t, y=v, name=f"{curr} nA"))
# # fig = fig.update_layout(
# #     xaxis_range=[stim_start-20,stim_start+stim_dur+100]
# #     )
# fig = fig.update_layout({
#     "xaxis_title": "Time (ms)",
#     "yaxis_title": "Voltage (mV)",
#     "title":'M1 Motorneuron Voltage Response to Various Depolarizing Current'
# })
# fig.show()