from neuron import h
from neuron.units import um, mV, ms
from neuron import rxd
import plotly
import plotly.graph_objects as go
h.load_file("stdrun.hoc")

soma=h.Section(name="soma")
soma.L=10 * um
soma.diam=10 * um
soma.nseg=10
h.hh.insert(soma)
cyt=rxd.Region(h.allsec(), name='cyt', nrn_region='i')
k=rxd.Species(cyt, name='k',charge=1)

vc=h.SEClamp(soma(0.5))
vc.amp1=-65*mV
vc.dur1= 5*ms
vc.dur2=20*ms
vc.amp3=-65*mV
vc.dur3=1000*ms

t=h.Vector().record(h._ref_t)
ina=h.Vector().record(soma(0.5)._ref_ina)
ik=h.Vector().record(soma(0.5)._ref_ik)
ki=h.Vector().record(soma(0.5)._ref_ki)
figna=go.Figure()
figk=go.Figure()
figki=go.Figure()

for voltage in range(-80,50,10):
    vc.amp2=voltage*mV
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