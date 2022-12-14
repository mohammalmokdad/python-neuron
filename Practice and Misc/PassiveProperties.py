# Python Script to test out passive properties of motorneuron and compare morphology
from neuron import h
from neuron.units import um, mV, ms
import plotly
import plotly.express as px
import pandas as pd
import numpy as np
h.load_file("stdrun.hoc")
h.load_file("import3d.hoc")

# Loading in the morphology
class morph:
    def __init__(self):
        self.load_morphology()
        # do discretization, ion channels, etc
    def load_morphology(self):
        cell = h.Import3d_SWC_read()
        cell.input("Morpho\S_1.swc")
        i3d = h.Import3d_GUI(cell, False)
        i3d.instantiate(self)

mycell=morph()

# calculating total area and length of cell (in um and um^2, respectively)
area=0
length=0
for sec in mycell.all:
    area = area + sec(0.5).area()
    length= length+ sec.L
print(area)

# tau in ms, ri in megaohm (get values as known, then finds the cm and g_pas according to the area)
tau=30
ri=0.6
h.dt=0.01
gpas=1/((ri*(10**(6)))*(area*(10**(-8))))
cm=(tau*10**(-3))/((ri)*(area*(10**(-8))))


soma=mycell.soma[0]
dend=mycell.dend

for sec in mycell.all:
    sec.insert('pas')
    sec.Ra=0.0000001
    sec.g_pas=gpas
    sec.cm=cm

impcalc=h.Impedance()
impcalc.loc(soma(0.5))
impcalc.compute(0)
imp=impcalc.input(soma(0.5))
print(imp)

# testing out different axial resistances and how they change the Rn (finding Rn through impedance)
# imp=[]
# i=0
# testRa=np.arange(0.05,500,0.05)
# for Ra in testRa:
#     i=i+1
#     print(i)
#     for sec in mycell.all:
#         sec.Ra=Ra
#     impcalc=h.Impedance()
#     impcalc.loc(soma(0.5))
#     impcalc.compute(0)
#     imp.append(impcalc.input(soma(0.5)))

# saving to csv for analysis
# pd.DataFrame(testRa).to_csv("testRa.csv", header=None, index=None)
# pd.DataFrame(imp).to_csv("imp.csv", header=None, index=None)

# Creating a current clamp, recording time and voltage, and plotting to see how current changes things
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

# Calculating tau
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
print(t_tau)


fig=px.line(x=t, y=v)
fig = fig.update_layout(
    yaxis_range=[-80,-65])
fig = fig.update_layout({
    "xaxis_title": "Time (ms)",
    "yaxis_title": "Voltage (mV)",
    "title":'Voltage response to 1 nA current'
})
fig.show()