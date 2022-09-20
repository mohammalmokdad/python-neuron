TITLE CaT
: T-Type Calcium Current

NEURON {
	SUFFIX CaT
	USEION ca READ eca WRITE ica
	RANGE gcatbar, ica, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gcatbar = 0 (S/cm2)
}

ASSIGNED {
	v (mV)
	eca (mV)
	ica (mA/cm2)
	i (mA/cm2)
	g (S/cm2)
	minf mtau
	hinf htau
}

STATE { 
	m h
}

BREAKPOINT {
	SOLVE states METHOD cnexp
	g = gcatbar * m^3 * h
	ica = g * (v - eca)
}

INITIAL {
	rates(v)
	m = minf
	h = hinf
}

DERIVATIVE states {
	rates(v)
	m' = (minf - m)/mtau
	h' = (hinf - h)/htau
}

PROCEDURE rates(v(mV)) {LOCAL am, bm, ah, bh
	am = 0.02 * (v+38)/(1-exp((v+38)/(-4.5)))
	bm = (-0.05) * (v+41)/(1-exp((v+41)/4.5))
	ah = (-0.0001) * (v+43)/(1-exp((v+43)/7.8))
	bh = 0.03 / (1 + exp((v+41)/(-4.8)))
	mtau = 1/(am + bm)
	minf = am/(am + bm)
	htau = 1/(ah + bh)
	hinf = ah/(ah + bh)
}