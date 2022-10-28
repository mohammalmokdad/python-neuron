import pandas as pd
import numpy as np
import getpassparams as GPP
from numpy.random import randint
#myfile=input("Enter the name of the ht/lt parameters \".csv\" file: ")

def createmn(neuronactive,neuronpassive):
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


    L_somastr=[]
    diam_somastr=[]
    L_dendstr=[]
    diam_dendstr=[]
    g_somastr=[]
    g_dendstr=[]
    cm_somastr=[]
    cm_dendstr=[]
    Ra_somastr=[]
    Ra_dendstr=[]
    for N in range(NNeurons):
        L_somastr.append(f'\tsoma.L = {SpacedPassivePre[N][0]*SpacedPassivePre[N][2]} \n')
        diam_somastr.append(f'\tsoma.diam = {SpacedPassivePre[N][1]} \n')
        L_dendstr.append(f'\tdend.L = {SpacedPassivePre[N][0]*(1-SpacedPassivePre[N][2])} \n')
        diam_dendstr.append(f'\tdend.diam = {SpacedPassivePre[N][1]} \n')
        g_somastr.append(f"\tsoma.g_pas = {SpacedPassivePost[N][0]} \n")
        g_dendstr.append(f"\tdend.g_pas = {SpacedPassivePost[N][1]} \n")
        cm_somastr.append(f"\tsoma.cm = {SpacedPassivePost[N][2]} \n")
        cm_dendstr.append(f"\tdend.cm = {SpacedPassivePost[N][3]} \n")
        Ra_somastr.append(f"\tsoma.Ra = {SpacedPassivePost[N][4]} \n")
        Ra_dendstr.append(f"\tdend.Ra = {SpacedPassivePost[N][4]} \n")

    ActivePars=[]
    for N in range(NNeurons):
        active=[]
        for index, row in activecsv.iterrows():
            active.append(f'\t{row[0]}.{row[1]} = {SpacedActive[N][index]} \n')
        ActivePars.append(active)

    for N in range(NNeurons):
        pyfile=open(f'CreateCells/CreatedCells/M{N+1}.py','w')
        pyfile.write('def neuron(soma,dend,h): \n')
        pyfile.write("# PASSIVE PARAMETERS \n")
        pyfile.write(L_somastr[N])
        pyfile.write(diam_somastr[N])
        pyfile.write(g_somastr[N])
        pyfile.write(cm_somastr[N])
        pyfile.write(Ra_somastr[N])
        pyfile.write(L_dendstr[N])
        pyfile.write(diam_dendstr[N])
        pyfile.write(g_dendstr[N])
        pyfile.write(cm_dendstr[N])
        pyfile.write(Ra_dendstr[N])

        pyfile.write("\n # ACTIVE PARAMETERS \n")
        for i in range(len(ActivePars[N])):
            pyfile.write(ActivePars[N][i])
        pyfile.write('\treturn soma,dend')
        pyfile.close()
    print("Files Created Succesfully")