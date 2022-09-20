TITLE NaF_AS
: Potassium A-Current

NEURON {
	SUFFIX KA
	USEION k READ ek WRITE ik
	RANGE gkabar, ik, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gkabar = 0 (S/cm2)
}

ASSIGNED {
	v (mV)
	ek (mV)
	ik (mA/cm2)
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
	g = gkabar * m^4 * h
	ik = g * (v - ek)
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
	am = 0.032 * (v+54)/(1-exp((v+54)/(-6)))
	bm = 0.203 /exp((v+30)/24)
	ah = 0.05 / (1 + exp((v+76)/10))
	bh = 0.05 / (1 + exp((v+76)/(-10)))
	mtau = 1/(am + bm)
	minf = am/(am + bm)
	htau = 1/(ah + bh)
	hinf = ah/(ah + bh)
}