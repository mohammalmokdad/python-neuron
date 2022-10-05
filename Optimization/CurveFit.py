# Python Script to test out optimzation with bluepyopt
from neuron import h
from neuron.units import um, mV, ms
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import scipy.optimize as optimize
h.load_file("stdrun.hoc")
h.load_file("import3d.hoc")


def cumarea(morph_file,resolution):
    # Loading in the morphology
    class morph:
        def __init__(self):
            self.load_morphology()
            # do discretization, ion channels, etc
        def load_morphology(self):
            cell = h.Import3d_SWC_read()
            cell.input(morph_file)
            i3d = h.Import3d_GUI(cell, False)
            i3d.instantiate(self)

    mycell=morph()

    maxlength=0
    totarea=0

    soma=mycell.soma[0]
    for sec in soma.subtree():
        sec.nseg=int(np.ceil(sec.L/resolution))
        totarea+=sec.L*sec.diam*np.pi
        length=h.distance(soma(0),sec(1))
        if length>maxlength:
            maxlength=length
            section=sec

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
    return cumarea, distarray

[y_values,x_values]=cumarea("Morpho/v_e_moto6.CNG.swc",2)

# Objective
def objective(x_values, a, b):
    return 1-(1/(1-np.exp(-a/b)+np.exp((x_values-a)/b)))

pop, cov = optimize.curve_fit(objective, x_values, y_values)

a=pop[0]
b=pop[1]

y_line=objective(x_values,a,b)

fig=px.line(x=x_values, y=y_values)
fig.add_trace(go.Line(x=x_values, y=y_line,showlegend=False))
fig = fig.update_layout({
    "xaxis_title": "Path Length",
    "yaxis_title": "Cumalitive Area",
    "title":'FR Motorneuron (M6) Cumalative Area vs Path Length'
})
fig.show()