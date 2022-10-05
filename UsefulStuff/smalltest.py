from neuron import h
from neuron.units import um, mV, ms
import plotly.express as px
import pandas as pd
import numpy as np
import sys
import Calc_Cumarea as cm

[cumareas,distance]=cm.cumarea("Morpho\S_2.swc",2)

fig=px.line(x=distance, y=cumareas)
fig = fig.update_layout({
    "xaxis_title": "Path Length",
    "yaxis_title": "Cumalitive Area",
    "title":'S Motorneuron (M1) Cumalative Area vs Path Length'
})
fig.show()