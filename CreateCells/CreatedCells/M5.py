def neuron(soma,dend,h): 
# PASSIVE PARAMETERS 
	soma.L = 3434.4 
	soma.diam = 18.0 
	soma.g_pas = 0.00014839636845743632 
	soma.cm = 1.7734769976887372 
	soma.Ra = 16.44729724858019 
	dend.L = 2925.6 
	dend.diam = 18.0 
	dend.g_pas = 0.000117799575762416 
	dend.cm = 0.9287539683150028 
	dend.Ra = 16.44729724858019 

 # ACTIVE PARAMETERS 
	soma.e_pas = -71.4 
	soma.gbar_na3rp = 0.0148 
	soma.gbar_naps = 2.36e-05 
	soma.sh_na3rp = 1.0 
	soma.sh_naps = 5.0 
	soma.ar_na3rp = 1.0 
	soma.ar_naps = 1.0 
	soma.gMax_kdrRL = 0.017 
	soma.gcamax_mAHP = 8.04e-06 
	soma.gkcamax_mAHP = 0.0005099999999999999 
	soma.taur_mAHP = 40.0 
	soma.ek = -80.0 
	soma.ghbar_gh = 0.00011 
	soma.half_gh = -77.0 
	dend.e_pas = -71.4 
	dend.gcabar_L_Ca = 0.00010740000000000001 
	dend.ghbar_gh = 0.00011 
	dend.half_gh = -77.0 
	h.qinf_na3rp = 8.0 
	h.thinf_na3rp = -50.0 
	h.vslope_naps = 5.0 
	h.asvh_naps = -90.0 
	h.bsvh_naps = -22.0 
	h.mvhalfca_mAHP = -20.0 
	h.mtauca_mAHP = 2.0 
	h.celsius = 37.0 
	h.theta_m_L_Ca = -38.8 
	h.tau_m_L_Ca = 40.0 
	#h.theta_h_L_Ca = -7.440000000000001 
	#h.tau_h_L_Ca = 2500.0 
	#h.kappa_h_L_Ca = 5.0 
	h.htau_gh = 30.0 
	h.mVh_kdrRL = -21.0 
	h.tmin_kdrRL = 0.8 
	h.taumax_kdrRL = 20.0 
	#h.V0 = -5.0 
	return soma,dend