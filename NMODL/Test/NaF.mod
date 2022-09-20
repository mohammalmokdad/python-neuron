TITLE NaF
: Fast sodium conductance

NEURON {
	SUFFIX NaF
	USEION na READ ena WRITE ina
	RANGE gnafbar, ina, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gnafbar = 0 (S/cm2)
}

ASSIGNED {
	v (mV)
	ena (mV)
	ina (mA/cm2)
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
	g = gnafbar * m^3 * h
	ina = g * (v - ena)
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
	am = 0.1 * (-(v+40)/(exp(-(v+40)/10)-1))
	bm = 4 * exp(-(v+65)/18)
	ah = .07 * exp(-(v+65)/20)
	bh = 1 / (exp(-(v+35)/10) + 1)
	mtau = 1/(am + bm)
	minf = am/(am + bm)
	htau = 1/(ah + bh)
	hinf = ah/(ah + bh)
}