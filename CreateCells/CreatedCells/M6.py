def neuron(soma,dend,h): 
# PASSIVE PARAMETERS 
	soma.L = 3575.0000000000005 
	soma.diam = 20.0 
	soma.g_pas = 0.00015073162711321265 
	soma.cm = 1.620622707533274 
	soma.Ra = 19.433197633653634 
	dend.L = 2924.9999999999995 
	dend.diam = 20.0 
	dend.g_pas = 0.00011599512045337768 
	dend.cm = 0.8486354778598116 
	dend.Ra = 19.433197633653634 

 # ACTIVE PARAMETERS 
	soma.e_pas = -71.5 
	soma.gbar_na3rp = 0.016 
	soma.gbar_naps = 2.3e-05 
	soma.sh_na3rp = 1.0 
	soma.sh_naps = 5.0 
	soma.ar_na3rp = 1.0 
	soma.ar_naps = 1.0 
	soma.gMax_kdrRL = 0.0175 
	soma.gcamax_mAHP = 8.449999999999999e-06 
	soma.gkcamax_mAHP = 0.000525 
	soma.taur_mAHP = 35.0 
	soma.ek = -80.0 
	soma.ghbar_gh = 0.00013000000000000002 
	soma.half_gh = -77.0 
	dend.e_pas = -71.5 
	dend.gcabar_L_Ca = 0.0001105 
	dend.ghbar_gh = 0.00013000000000000002 
	dend.half_gh = -77.0 
	h.qinf_na3rp = 8.0 
	h.thinf_na3rp = -50.0 
	h.vslope_naps = 5.0 
	h.asvh_naps = -90.0 
	h.bsvh_naps = -22.0 
	h.mvhalfca_mAHP = -20.0 
	h.mtauca_mAHP = 2.0 
	h.celsius = 37.0 
	h.theta_m_L_Ca = -38.5 
	h.tau_m_L_Ca = 40.0 
	#h.theta_h_L_Ca = -11.3 
	#h.tau_h_L_Ca = 2500.0 
	#h.kappa_h_L_Ca = 5.0 
	h.htau_gh = 30.0 
	h.mVh_kdrRL = -21.0 
	h.tmin_kdrRL = 0.8 
	h.taumax_kdrRL = 20.0 
	#h.V0 = -2.5 
	return soma,dend