TITLE NaF_AS
: Fast sodium conductance for axon and soma

NEURON {
	SUFFIX NaF_AS
	USEION na READ ena WRITE ina
	RANGE gnaf_asbar, ina, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gnaf_asbar = 0 (S/cm2)
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
	g = gnaf_asbar * m^3 * h
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
	am = 0.4 * (4-v)/(exp((4-v)/5)-1)
	bm = 0.4 * (v-29)/(exp((v-29)/5)-1)
	ah = .28 * exp((24-v)/20)
	bh = 4 / (exp((24-v)/10) + 1)
	mtau = 1/(am + bm)
	minf = am/(am + bm)
	htau = 1/(ah + bh)
	hinf = ah/(ah + bh)
}