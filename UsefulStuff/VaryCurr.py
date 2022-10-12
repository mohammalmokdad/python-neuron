fig=go.Figure()
for curr in range(-10,0,1):
    ic.amp=curr
    h.finitialize(-70*mV)
    h.continuerun(stim_start+stim_dur+200)
    fig.add_trace(go.Scatter(x=t, y=v, name=f"{curr} nA"))
# fig = fig.update_layout(
#     xaxis_range=[stim_start-20,stim_start+stim_dur+100]
#     )
fig = fig.update_layout({
    "xaxis_title": "Time (ms)",
    "yaxis_title": "Voltage (mV)",
    "title":'M1 Motorneuron Voltage Response to Various Hyperpolarizing Current'
})
fig.show()