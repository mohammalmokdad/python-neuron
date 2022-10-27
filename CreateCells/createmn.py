import pandas as pd
import numpy as np
import getpassparams as GPP
from numpy.random import randint
#myfile=input("Enter the name of the ht/lt parameters \".csv\" file: ")

activecsv=pd.read_csv("CreateCells/neuronactive.csv",header=None)
passivecsv=pd.read_csv("CreateCells/neuronpassive.csv",header=None)
NNeurons=11

a=[]
for index, row in activecsv.iterrows():
    a.append(np.linspace(row[2],row[3],NNeurons))
SpacedActive=pd.DataFrame(a)

b=[]

for index, row in passivecsv.iterrows():
    b.append(np.linspace(row[1],row[2],NNeurons))

SpacedPassivePre=pd.DataFrame(b)

params=[]
for i in range(NNeurons):
    totalL=SpacedPassivePre[i][0]
    diam=SpacedPassivePre[i][1]
    psoma=SpacedPassivePre[i][2]
    vads=SpacedPassivePre[i][3]
    vasd=SpacedPassivePre[i][4]
    vasdac=SpacedPassivePre[i][5]
    tau=SpacedPassivePre[i][6]
    Rn=SpacedPassivePre[i][7]
    pars=GPP.get_pass_params(totalL,diam,psoma,vads,vasd,vasdac,tau,Rn)
    # G_pas soma, G_pas dend, Cm soma, Cm dend, Ra
    fixedpars=np.asarray([pars[1]/1000000, pars[2]/1000000, pars[5], pars[4], pars[6]])
    params.append(fixedpars)

SpacedPassivePost=pd.DataFrame(np.transpose(params))

index=0
N=0



g_somastr=[]
g_dendstr=[]
cm_somastr=[]
cm_dendstr=[]
Ra_somastr=[]
Ra_dendstr=[]
for N in range(NNeurons):
    g_somastr.append(f"soma.g_pas = {SpacedPassivePost[N][0]} \n")
    g_dendstr.append(f"dend.g_pas = {SpacedPassivePost[N][1]} \n")
    cm_somastr.append(f"soma.cm = {SpacedPassivePost[N][2]} \n")
    cm_dendstr.append(f"dend.cm = {SpacedPassivePost[N][3]} \n")
    Ra_somastr.append(f"soma.Ra = {SpacedPassivePost[N][4]} \n")
    Ra_dendstr.append(f"dend.Ra = {SpacedPassivePost[N][4]} \n")

ActivePars=[]
for N in range(NNeurons):
    active=[]
    for index, row in activecsv.iterrows():
        active.append(f'{row[0]}.{row[1]} = {SpacedActive[N][index]} \n')
    ActivePars.append(active)

for N in range(NNeurons):
    pyfile=open(f'CreateCells/CreatedCells/M{N+1}.py','w')

    pyfile.write("# PASSIVE PARAMETERS \n")

    pyfile.write(g_somastr[N])
    pyfile.write(g_dendstr[N])
    pyfile.write(cm_somastr[N])
    pyfile.write(cm_dendstr[N])
    pyfile.write(Ra_somastr[N])
    pyfile.write(Ra_dendstr[N])

    pyfile.write("\n # ACTIVE PARAMETERS \n")
    for i in range(len(ActivePars[N])):
        pyfile.write(ActivePars[N][i])
    pyfile.close()
