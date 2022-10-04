# Python Script to test out optimzation with bluepyopt
from neuron import h
from neuron.units import um, mV, ms
import numpy as np
import scipy.optimize as optimize

import evaluation


initial_guess=[300,1200,25]
bnds=([50,1000],[300,10000],[10,120])
result=optimize.minimize(evaluation.evaluate, initial_guess, method='Nelder-Mead', bounds=bnds)

if result.success:
    fitted_params = result.x
    print(fitted_params)
else:
    raise ValueError(result.message)
