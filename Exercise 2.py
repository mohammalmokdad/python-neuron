from neuron import h
from neuron.units import um, mV, ms
from neuron import rxd
import plotly
import plotly.graph_objects as go
h.load_file("stdrun.hoc")

axon=h.Section(name="axon")
axon.L=10 * um
axon.diam=1 * um
axon.nseg=10
h.hh.insert(axon)
cyt=rxd.Region(h.allsec(), name='cyt', nrn_region='i')
k=rxd.Species(cyt, name='k',charge=1)

vc=h.SEClamp(axon(0.5))
vc.amp1=-65*mV
vc.dur1= 5*ms
vc.amp3=-65*mV
vc.dur3=1000*ms

t=h.Vector().record(h._ref_t)
ina=h.Vector().record(axon(0.5)._ref_ina)
ik=h.Vector().record(axon(0.5)._ref_ik)
ki=h.Vector().record(axon(0.5)._ref_ki)
figna=go.Figure()
figk=go.Figure()
figki=go.Figure()

for voltage in [-80,-70,-60,-50,-40,-30,-20,-10,-0,10,20,30,40]:
    vc.amp2=voltage*mV
    vc.dur2=20*ms
    h.finitialize(-65*mV)
    h.continuerun(30*ms)
    figna.add_trace(go.Scatter(x=t, y=ina, name=f"{voltage} mV"))
    figk.add_trace(go.Scatter(x=t, y=ik, name=f"{voltage} mV"))
    figki.add_trace(go.Scatter(x=t, y=ki, name=f"{voltage} mV"))


figna = figna.update_layout({
    "xaxis_title": "time (ms)",
    "yaxis_title": "ina (mA/cm^2)",
    "title":'Sodium Conductance vs Clamp Voltage over Time'
})
figk = figk.update_layout({
    "xaxis_title": "time (ms)",
    "yaxis_title": "ik (mA/cm^2)",
    "title":'Potassium Conductance vs Clamp Voltage over Time'
})
figki = figki.update_layout({
    "xaxis_title": "time (ms)",
    "yaxis_title": "concentration (mM)",
    "title":'Potassium Concentration vs Clamp Voltage over Time'
})
figna.show()
figk.show()
figki.show()