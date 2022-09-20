TITLE NaF_IS
: Fast sodium conductance for initial segment

NEURON {
	SUFFIX NaF_IS
	USEION na READ ena WRITE ina
	RANGE gnaf_isbar, ina, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gnaf_isbar = 0 (S/cm2)
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
	g = gnaf_isbar * m^3 * h
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
	am = 0.4 * (5-v)/(exp((5-v)/5)-1)
	bm = 0.4 * (v-30)/(exp((v-30)/5)-1)
	ah = .28 * exp((25-v)/20)
	bh = 4 / (exp((25-v)/10) + 1)
	mtau = 1/(am + bm)
	minf = am/(am + bm)
	htau = 1/(ah + bh)
	hinf = ah/(ah + bh)
}