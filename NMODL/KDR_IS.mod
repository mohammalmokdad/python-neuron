TITLE KDR_IS
: Potassium Delayed Rectifier for initial segment

NEURON {
	SUFFIX KDR_IS
	USEION k READ ek WRITE ik
	RANGE gkdr_isbar, ik, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gkdr_isbar = 0 (S/cm2)
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
	g = gkdr_isbar * n^4
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
	an = 0.02 * (10-v)/(exp((10-v)/10)-1)
	bn = 0.25 * exp(-v/80)
	ntau = 1/(an + bn)
	ninf = an/(an + bn)
}