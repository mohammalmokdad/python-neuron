TITLE gh
: H-current

NEURON {
	SUFFIX gh
	NONSPECIFIC_CURRENT i
	RANGE ghbar, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	ghbar = 0 (S/cm2)
}

ASSIGNED {
	v (mV)
	eh (mV)
	i (mA/cm2)
	g (S/cm2)
	minf mtau
}

STATE { 
	m
}

BREAKPOINT {
	SOLVE states METHOD cnexp
	g = ghbar * m
	i = g * (v - eh)
}

INITIAL {
	rates(v)
	m = minf
}

DERIVATIVE states {
	rates(v)
	m' = (minf - m)/mtau
}

PROCEDURE rates(v(mV)) {LOCAL am, bm
	am = 0.06/(1+exp((v+75)/5.3))
	bm = 0.06/(1+exp((v+75)/(-5.3)))
	mtau = 1/(am + bm)
	minf = am/(am + bm)
}