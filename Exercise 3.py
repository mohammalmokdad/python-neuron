from neuron import h
from neuron.units import um, mV, ms
import plotly
import plotly.graph_objects as go
h.load_file("stdrun.hoc")

axon=h.Section(name="axon")
axon.L=1001 * um
axon.diam=1 * um
axon.nseg=51
axon.Ra=100

h.hh.insert(axon)

ns=h.NetStim()
ns.number=1
ns.start=5*ms
ns.noise=False

syn=h.ExpSyn(0)
syn.tau=5*ms
syn.e=0

nc=h.NetCon(ns,syn)
nc.weight[0]=0.01


# build list of vectors for each segment in the axon
th_cr_vecs= [h.Vector() for seg in axon]

# build a list of netcons connecting to cell membrane potential for each seg in axon
monitors=[h.NetCon(seg._ref_v, None, sec=axon) for seg in axon]

for monitor, vec in zip(monitors,th_cr_vecs):
    monitor.record(vec)

h.finitialize(-65*mV)
h.dt= 0.025/(2**5)

h.continuerun(10*ms)

fig=go.Figure()

# x coordinate = every segments x value (0-1) multiplied by the length of the axon, this allows position to be expressed in terms of um
# y coordinate = the entry of the vector in each thr_cr_vecs (time stamp of when the threshold was crossed)
cross_times=[vec[0] for vec in th_cr_vecs]

fig.add_trace(go.Scatter(x=[seg.x*axon.L for seg in axon], y=cross_times))

fig = fig.update_layout({
    "xaxis_title": "Position (µm)",
    "yaxis_title": "Time when threshold crossed (ms)",
    "title":'Time where action potential occured as a function of Position'
})
fig.show()





# x coordinate = position of every midpoint of every segment
# y coordinate = speed, calculated as length of each segment divided by the delta T from spike occuring in one section to the next
deltas=h.Vector(cross_times[1:]) - h.Vector(cross_times[:-1])
speed=(axon.L/axon.nseg)/deltas
midpoints=[(i+0.5)*(axon.L/axon.nseg) for i in range(len(speed))]

fig2=go.Figure()
fig2.add_trace(go.Scatter(x=midpoints, y=speed))
fig2 = fig2.update_layout({
    "xaxis_title": "Position (µm)",
    "yaxis_title": "Speed of action potential (µm/ms)",
    "title":'Speed of Action Potential as a Function of Position Along Axon'
})
fig2.show()