from neuron import h
from neuron.units import mV, ms
import matplotlib.pyplot as plt
h.load_file("stdrun.hoc")

axon=h.Section(name="axon")
axon.L=1000
axon.diam=10
axon.nseg=10
h.hh.insert(axon)

ic=h.IClamp(axon(0))
ic.delay = 2*ms
ic.dur = 0.1*ms
ic.amp = 10

d=h.Vector()
t=h.Vector().record(h._ref_t)
v=h.Vector().record(axon(0.5)._ref_v)

h.finitialize(-65*mV)
h.continuerun(30*ms)

plt.plot(t,v)
plt.xlabel('t (ms)')
plt.ylabel('V (mV)')
plt.show()