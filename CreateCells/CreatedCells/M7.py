def neuron(soma,dend,h): 
# PASSIVE PARAMETERS 
	soma.L = 3718.3999999999996 
	soma.diam = 22.0 
	soma.g_pas = 0.0001575917622485206 
	soma.cm = 1.5073018211173181 
	soma.Ra = 22.032956771088312 
	dend.L = 2921.6000000000004 
	dend.diam = 22.0 
	dend.g_pas = 0.00011779764277018977 
	dend.cm = 0.8010568454776271 
	dend.Ra = 22.032956771088312 

 # ACTIVE PARAMETERS 
	soma.e_pas = -71.6 
	soma.gbar_na3rp = 0.0172 
	soma.gbar_naps = 2.2400000000000002e-05 
	soma.sh_na3rp = 1.0 
	soma.sh_naps = 5.0 
	soma.ar_na3rp = 1.0 
	soma.ar_naps = 1.0 
	soma.gMax_kdrRL = 0.018000000000000002 
	soma.gcamax_mAHP = 8.86e-06 
	soma.gkcamax_mAHP = 0.0005399999999999999 
	soma.taur_mAHP = 30.0 
	soma.ek = -80.0 
	soma.ghbar_gh = 0.00015000000000000001 
	soma.half_gh = -77.0 
	dend.e_pas = -71.6 
	dend.gcabar_L_Ca = 0.0001136 
	dend.ghbar_gh = 0.00015000000000000001 
	dend.half_gh = -77.0 
	h.qinf_na3rp = 8.0 
	h.thinf_na3rp = -50.0 
	h.vslope_naps = 5.0 
	h.asvh_naps = -90.0 
	h.bsvh_naps = -22.0 
	h.mvhalfca_mAHP = -20.0 
	h.mtauca_mAHP = 2.0 
	h.celsius = 37.0 
	h.theta_m_L_Ca = -38.2 
	h.tau_m_L_Ca = 40.0 
	#h.theta_h_L_Ca = -15.160000000000004 
	#h.tau_h_L_Ca = 2500.0 
	#h.kappa_h_L_Ca = 5.0 
	h.htau_gh = 30.0 
	h.mVh_kdrRL = -21.0 
	h.tmin_kdrRL = 0.8 
	h.taumax_kdrRL = 20.0 
	#h.V0 = 0.0 
	return soma,dend