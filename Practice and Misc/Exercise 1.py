from neuron import h
from neuron.units import um, mV, ms
import plotly
h.load_file("stdrun.hoc")

axon=h.Section(name="axon")
axon.L=1001 * um
axon.diam=1 * um
axon.nseg=1001
h.hh.insert(axon)

ic=h.IClamp(axon(0))
ic.delay = 1*ms
ic.dur = 0.1*ms
ic.amp = 11

rvp=h.RangeVarPlot('v', axon(0), axon(1))

h.finitialize(-65*mV)

my_plot=rvp.plot(plotly, name="t=0", line={'width': 4})

for tstop in [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]:
    h.continuerun(tstop)
    my_plot=rvp.plot(my_plot, name=f't={tstop}',line={'width': 4})

my_plot = my_plot.update_layout({
    "xaxis_title": "position (µm)",
    "yaxis_title": "membrane potential (mV)",
    "title":'Potential as a function of position (Ra=35.4)'
})

my_plot.show()

axon.Ra=100
h.finitialize(-65*mV)

my_plot1=rvp.plot(plotly, name="t=0", line={'width': 4})

for tstop in [0.5,1,1.5,2,2.5,3,3.5,4,4.5,5]:
    h.continuerun(tstop)
    my_plot1=rvp.plot(my_plot1, name=f't={tstop}',line={'width': 4})

my_plot1 = my_plot1.update_layout({
    "xaxis_title": "position (µm)",
    "yaxis_title": "membrane potential (mV)",
    "title":'Potential as a function of position (Ra=100)'
})

my_plot1.show()