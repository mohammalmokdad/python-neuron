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
for sec in mycell.all:
    area = area + sec(0.5).area()
print(area)

length=0
len_vec=[]
area1=0
areavec=[]
for sec in mycell.all:
    area1=area1 + sec(0.5).area()
    areavec.append(area1/area)
    length=length+sec.L
    len_vec.append(length)
print(area)



fig=px.line(x=len_vec, y=areavec)
fig = fig.update_layout({
    "xaxis_title": "Time (ms)",
    "yaxis_title": "Voltage (mV)",
    "title":'Voltage response to 1 nA current'
})
fig.show()