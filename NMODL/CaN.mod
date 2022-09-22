TITLE CaN
: N-type Calcium Current

NEURON {
	SUFFIX CaN
	USEION can READ ecan WRITE ican VALENCE 2
	USEION ca READ eca WRITE ica
	RANGE gcanbar, ica, ican, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gcanbar = 0 (S/cm2)
	ecan
}

ASSIGNED {
	v (mV)
	eca (mV)
	ica (mA/cm2)
	ican (mA/cm2)
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
	g = gcanbar * m^2 * h
	ican = g * (v - ecan)
	ica = ican
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
	am = 0.25/(1+exp((v+20)/(-5)))
	bm = 0.25/(1+exp((v+20)/5))
	ah = 0.025/(1+exp((v+35)/5))
	bh = 0.025/(1+exp((v+35)/(-5)))
	mtau = 1/(am + bm)
	minf = am/(am + bm)
	htau = 1/(ah + bh)
	hinf = ah/(ah + bh)
}