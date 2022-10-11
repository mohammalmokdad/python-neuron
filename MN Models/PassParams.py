from neuron import h
from neuron.units import um, mV, ms
import numpy as np
h.load_file("stdrun.hoc")
h.load_file("import3d.hoc")

class morph:
    def __init__(self):
        self.load_morphology()
        # do discretization, ion channels, etc
    def load_morphology(self):
        cell = h.Import3d_SWC_read()
        cell.input("Morpho/v_e_moto4.CNG.swc")
        i3d = h.Import3d_GUI(cell, False)
        i3d.instantiate(self)

mycell=morph()
soma=mycell.soma[0]
D_path=650
totarea=0
for sec in soma.subtree():
    totarea+=sec.L*sec.diam*np.pi

diam=35
Length=totarea/(np.pi*diam)
Length=100*round(Length/100)


import getpassparams as GPP
import VAFuncs as VA
import cumareafuncs as CAF

tau=7.7
Rn=0.97



params=GPP.get_pass_params(Length, diam, CAF.M4(D_path), VA.DS_DC_M4(D_path), VA.SD_DC_M4(D_path), VA.SD_AC_M4(D_path), tau, Rn)

print(params)