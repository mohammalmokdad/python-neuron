# Script to set up cell as described in Dai et al. Output is not really working well however

from neuron import h
from neuron.units import mV, ms, um
import plotly
import plotly.graph_objects as go

mS=1/1000
h.load_file('stdrun.hoc')

axon=h.Section(name="axon")
axon.L=400 * um
axon.diam=10 * um
axon.Ra=20

axon.insert('pas')
axon.e_pas=-70
axon.g_pas=1/5000

axon.insert('NaF_AS')
axon.gnaf_asbar_NaF_AS=120 * mS
axon.ena=55*mV

axon.insert('KDR_AS')
axon.gkdr_asbar_KDR_AS=40 * mS
axon.ek=-75*mV



initseg=h.Section(name="initseg")
initseg.L=100 * um
initseg.diam=6 * um
initseg.Ra=20

initseg.insert('pas')
initseg.e_pas=-70
initseg.g_pas=1/5000

initseg.insert('NaF_IS')
initseg.gnaf_isbar_NaF_IS=240 * mS
initseg.ena=55*mV

initseg.insert('KDR_IS')
initseg.gkdr_isbar_KDR_IS=110 * mS
initseg.ek=-75*mV

initseg.insert('NaP')
initseg.gnapbar_NaP=12* mS



soma=h.Section(name="soma")
soma.L=360 * um
soma.diam=10 * um
soma.Ra=20

soma.insert('pas')
soma.e_pas=-70
soma.g_pas=1/5000

soma.insert('NaF_AS')
soma.gnaf_asbar_NaF_AS=200 * mS
soma.ena=55*mV

soma.insert('KDR_AS')
soma.gkdr_asbar_KDR_AS=35 * mS
soma.ek=-75*mV

soma.insert('KA')
soma.gkabar_KA=5.5 * mS

soma.insert('gh')
soma.ghbar_gh=6.5 * mS
soma.eh=-55*mV

soma.insert('CaT')
soma.gcatbar_CaT=4 * mS
soma.eca=80*mV

soma.insert('CaN')
soma.gcanbar_CaN=12 * mS
soma.ecan=80*mV

soma.insert('CaL')
soma.gcalbar_CaL=2 * mS

soma.insert('kAHP_S')
soma.gkahp_s_kAHP_S=10 * mS

soma.insert('leak')
soma.gleakbar_leak=0.6 * mS

soma.insert('NaP')
soma.gnapbar_NaP=3 * mS

soma.insert('mAHP')
soma.gcamax_mAHP = 8e-06
soma.gkcamax_mAHP = 0.0011
soma.taur_mAHP = 70

soma.insert('CalConc')
soma.BCal_CalConc=-17.402



proxdend=h.Section(name="proxdend")
proxdend.L=500 * um
proxdend.diam=40 * um
proxdend.Ra=60

proxdend.insert('pas')
proxdend.e_pas=-70
proxdend.g_pas=1/5000

proxdend.insert('CaN')
proxdend.gcanbar_CaN=1.5* mS
proxdend.eca=80*mV
proxdend.ecan=80*mV

proxdend.insert('CaL')
proxdend.gcalbar_CaL=0.33 * mS

proxdend.insert('kAHP_D')
proxdend.gkahp_d_kAHP_D=6 * mS

proxdend.insert('leak')
proxdend.gleakbar_leak=0.6 * mS

proxdend.insert('mAHP')
proxdend.gcamax_mAHP = 8e-06
proxdend.gkcamax_mAHP = 0.0011
proxdend.taur_mAHP = 70

proxdend.insert('CalConc')
proxdend.BCal_CalConc=-10.769



distdend=h.Section(name="distdend")
distdend.L=400 * um
distdend.diam=30 * um
distdend.Ra=60
distdend.insert('pas')
distdend.e_pas=-70
distdend.g_pas=1/5000



initseg.connect(axon,0)
soma.connect(initseg,0)
proxdend.connect(soma,0)
distdend.connect(proxdend,0)

ic=h.IClamp(soma(0.5))
ic.delay = 100*ms
ic.dur = 1000*ms
ic.amp = 15

t=h.Vector().record(h._ref_t)
vrecord=h.Vector().record(soma(0.5)._ref_v)

h.finitialize(-70*mV)
h.continuerun(2000*ms)
h.dt=0.01

fig=go.Figure()
fig.add_trace(go.Scatter(x=t, y=vrecord, name='bruh'))
fig.show()