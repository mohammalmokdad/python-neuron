# Gets the passive parameters (converted from Making_a_pool_of_two_compt_NEURON_model.docx)

import numpy as np


# Calculates axial resistance from Gc
def calc_Ra(gc,totarea,totalL,diam):
    Lpath=0.5*totalL
    Ratot=1/(gc*1e-6*totarea*1e-8)
    Ra=(Ratot/(Lpath*1e-4))*(1e-8*(np.pi/4)*diam**2)
    return Ra

# Calculates cm in the soma
def get_cms(gms,gmd,gc,cmd,ps,tau):
    gms=gms/1000
    gmd=gmd/1000
    gc=gc/1000    
    cms=tau*(ps*(1-ps)*tau*gms*gmd+ps*gms*(tau*gc-cmd)+ ps**2*gms*cmd+(1-ps)*(tau*gc*gmd-gc*cmd))
    cms=cms/(ps*((1-ps)*(tau*gmd-cmd)+tau*gc))
    return cms




def get_pass_params(totalL,diam,psoma,vads,vasd,vasdac,tau,Rn):
    totarea=np.pi*totalL*diam
    rsoma=psoma*totarea*Rn*1e-8
    gms=(1-vads)/(rsoma*(1-vasd*vads))
    gmd=(psoma*vads*(1-vasd))/((1-psoma)*rsoma*vasd*(1-vasd*vads))
    gc=(psoma*vads)/(rsoma*(1-vasd*vads))
    cmd=1/(500*np.pi*(1-psoma))
    cmd=cmd*(np.sqrt(((gc/vasdac)**2)-(gc+gmd*(1-psoma))**2))
    cms=get_cms(gms,gmd,gc,cmd,psoma,tau)
    Ra=calc_Ra(gc,totarea,totalL,diam)
    return rsoma, gms, gmd, gc, cmd, cms, Ra, psoma