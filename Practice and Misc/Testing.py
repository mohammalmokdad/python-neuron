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
        cell.input("Morpho/v_e_moto2.CNG.swc")
        i3d = h.Import3d_GUI(cell, False)
        i3d.instantiate(self)

mycell=morph()

area=0
length=0
for sec in mycell.all:
    area+= sec.L*sec.diam*np.pi
print(area)

maxlength=0
totarea=0
resolution=10

soma=mycell.soma[0]
for sec in soma.subtree():
    sec.nseg=int(np.ceil(sec.L/resolution))
    totarea+=sec.L*sec.diam*np.pi
    length=h.distance(soma(0),sec(1))
    if length>maxlength:
        maxlength=length
        section=sec

print(maxlength)
print(section)
print(totarea)


arearray=[]
distarray=np.arange(0,maxlength+resolution,resolution)
for testdist in distarray:
    area=0
    for sec in soma.subtree():
        halt=0
        i=0
        for seg in sec.allseg():
            i=i+1
            if halt==0:
                dist=h.distance(soma(0),seg)
                if dist>=testdist:
                    area+=h.distance(sec(0),seg)*seg.diam*np.pi
                    halt=1
                if seg==sec(1) and dist<testdist:
                    area+=sec.L*sec.diam*np.pi
    arearray.append(area)

areanp=np.array(arearray)
cumarea=areanp/totarea

fig=px.line(x=distarray, y=cumarea)
fig = fig.update_layout({
    "xaxis_title": "Path Length",
    "yaxis_title": "Cumalitive Area",
    "title":'Voltage response to 1 nA current'
})
fig.show()