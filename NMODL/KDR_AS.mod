TITLE KDR_AS
: Potassium Delayed Rectifier for axon and soma

NEURON {
	SUFFIX KDR_AS
	USEION k READ ek WRITE ik
	RANGE gkdr_asbar, ik, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gkdr_asbar = 0 (S/cm2)
}

ASSIGNED {
	v (mV)
	ek (mV)
	ik (mA/cm2)
	i (mA/cm2)
	g (S/cm2)
	ninf ntau
}

STATE { 
	n
}

BREAKPOINT {
	SOLVE states METHOD cnexp
	g = gkdr_asbar * n^4
	ik = g * (v - ek)
}

INITIAL {
	rates(v)
	n = ninf
}

DERIVATIVE states {
	rates(v)
	n' = (ninf - n)/ntau
}

PROCEDURE rates(v(mV)) {LOCAL an, bn
	an = 0.02 * (20-v)/(exp((20-v)/10)-1)
	bn = 0.25 * exp(10-v/80)
	ntau = 1/(an + bn)
	ninf = an/(an + bn)
}