TITLE CaL
: L-Type Calcium Current

NEURON {
	SUFFIX CaL
	USEION ca READ eca WRITE ica
	RANGE gcalbar, ica, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gcalbar = 0 (S/cm2)
}

ASSIGNED {
	v (mV)
	eca (mV)
	ica (mA/cm2)
	i (mA/cm2)
	g (S/cm2)
	minf mtau
}

STATE { 
	m
}

BREAKPOINT {
	SOLVE states METHOD cnexp
	g = gcalbar * m
	ica = g * (v - eca)
}

INITIAL {
	rates(v)
	m = minf
}

DERIVATIVE states {
	rates(v)
	m' = (minf - m)/mtau
}

PROCEDURE rates(v(mV)) {LOCAL am, bm, ah, bh
	am = 0.025/(1+exp((v+30)/(-7)))
	bm = 0.025/(1+exp((v+30)/7))
	mtau = 1/(am + bm)
	minf = am/(am + bm)
}