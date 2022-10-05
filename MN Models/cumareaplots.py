import numpy as np
import plotly.graph_objects as go
import plotly.express as px

def objective(x_values, a, b):
    return 1-(1/(1-np.exp(-a/b)+np.exp((x_values-a)/b)))

x=np.arange(0,2200,2)

fig=go.Figure()
fig.add_trace(go.Scatter(x=x, y=objective(x,559.5900739428298,310.72431966327235), name="M1"))
fig.add_trace(go.Scatter(x=x, y=objective(x,592.9432100308615,284.170655892884), name="M2"))
fig.add_trace(go.Scatter(x=x, y=objective(x,558.9825607401616,368.024382347019), name="M3"))
fig.add_trace(go.Scatter(x=x, y=objective(x,679.2968391773574,344.9262571957527), name="M4"))
fig.add_trace(go.Scatter(x=x, y=objective(x,457.1828799696361,372.12955854433187), name="M6"))
fig.update_layout({
    "xaxis_title": "D(μm)",
    "yaxis_title": "Relative Surface Area",
    "title":'Relative Surface Area vs Path Length for All Neuron Types'
})
fig.show()