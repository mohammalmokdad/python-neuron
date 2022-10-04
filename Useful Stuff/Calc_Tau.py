# Calculates time constant tau of a cell. Requires time to be recorded as t, voltage as v, and the stimulus start and duration to be defined. 
# Longer stimulus gives more accurate measurement for tau, especially if tau is large.
import numpy as np

# Calculating tau
start_idx=int((stim_start/h.dt) - 1)
stop_idx=int(((stim_start+stim_dur)/h.dt)+1)
v_np=np.asarray(v)
v_np_mod=v_np[start_idx:stop_idx]
maxv=np.amax(v_np_mod)
minv=np.amin(v_np_mod)
diffv=maxv-minv
v_tau=minv+diffv*(1-(1/np.exp(1)))
idx=(np.abs(v_np_mod - v_tau)).argmin()
t_tau=t[idx+start_idx]-stim_start
print('Time constant tau is %f ms' % t_tau)