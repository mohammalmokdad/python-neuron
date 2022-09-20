TITLE KDR
: Potassium Delayed Rectifier

NEURON {
	SUFFIX KDR
	USEION k READ ek WRITE ik
	RANGE gkdrbar, ik, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gkdrbar = 0 (S/cm2)
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
	g = gkdrbar * n^4
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
	an = 0.01 * (-(v+55)/(exp(-(v+55)/10)-1))
	bn = 0.125 * exp(-(v+65)/80)
	ntau = 1/(an + bn)
	ninf = an/(an + bn)
}