from neuron import h
from neuron.units import mV, ms, um
import plotly
import plotly.graph_objects as go


h.load_file('stdrun.hoc')

axon=h.Section(name="axon")
axon.L=400 * um
axon.diam=10 * um
axon.Ra=20

initseg=h.Section(name="initseg")
initseg.L=100 * um
initseg.diam=6 * um
initseg.Ra=20

soma=h.Section(name="soma")
soma.L=360 * um
soma.diam=10 * um
soma.Ra=20

proxdend=h.Section(name="proxdend")
proxdend.L=500 * um
proxdend.diam=40 * um
proxdend.Ra=60

distdend=h.Section(name="distdend")
distdend.L=400 * um
distdend.diam=30 * um
distdend.Ra=60

initseg.connect(axon,0)
soma.connect(initseg,0)
proxdend.connect(soma,0)
distdend.connect(proxdend,0)

h.celsius=37

h.topology()