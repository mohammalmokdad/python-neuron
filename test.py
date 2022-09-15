from unicodedata import name
from neuron import h
from neuron.units import mV, ms, um
from neuron import rxd
import pandas as pd

h.load_file('stdrun.hoc')

h.finitialize(-65*mV)
h.continuerun(10*ms)
main=h.Section(name='main')
dend1=h.Section(name='dend1')
dend2=h.Section(name='dend2')

main.diam=10
dend1.diam=dend2.diam=2
dend1.connect(main)
dend2.connect(main)

ps=h.PlotShape(False)
