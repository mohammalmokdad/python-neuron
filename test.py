from neuron import h
from neuron.units import mV, ms, um
from neuron import rxd
import plotly
import plotly.graph_objects as go


h.load_file('stdrun.hoc')

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

ns2=h.NetStim()
ns2.number=1
ns2.start=15*ms
ns2.noise=False

syn=h.ExpSyn(0)
syn.tau=5*ms
syn.e=0

nc=h.NetCon(ns,syn)
nc.weight[0]=0.01

nc2=h.NetCon(ns2,syn)
nc2.weight[0]=0.01


# build list of vectors for each segment in the axon
th_cr_vecs= [h.Vector() for seg in axon]

# build a list of netcons connecting to cell membrane potential for each seg in axon
monitors=[h.NetCon(seg._ref_v, None, sec=axon) for seg in axon]
for monitor in monitors:
    monitor.threshold=0
for monitor, vec in zip(monitors,th_cr_vecs):
    monitor.record(vec)

t=h.Vector().record(h._ref_t)
v=h.Vector().record(axon(0.00980392)._ref_v)

h.finitialize(-65*mV)
h.dt= 0.025/(2**5)

h.continuerun(30*ms)

fig=go.Figure()
fig2=go.Figure()



fig2.add_trace(go.Scatter(x=t,y=v))

# x coordinate = every segments x value (0-1) multiplied by the length of the axon, this allows position to be expressed in terms of um
# y coordinate = the entry of the vector in each thr_cr_vecs (time stamp of when the threshold was crossed)
cross_times=[vec[1] for vec in th_cr_vecs]
midpoints=[seg.x*axon.L for seg in axon]

fig.add_trace(go.Scatter(x=midpoints, y=cross_times))


fig = fig.update_layout({
    "xaxis_title": "Position (µm)",
    "yaxis_title": "Time when threshold crossed (ms)",
    "title":'Time When Action Potential Occured as a Function of Position'
})
fig.show()
fig2.show()