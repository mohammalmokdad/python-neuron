TITLE NaP
: Persistant sodium conductance

NEURON {
	SUFFIX NaP
	USEION na READ ena WRITE ina
	RANGE gnapbar, ina, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gnapbar = 0 (S/cm2)
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
	g = gnapbar * m^3
	ina = g * (v - ena)
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
	am = 0.4 * (7.5-v)/(exp((7.5-v)/5)-1)
	bm = 0.4 * (v-35)/(exp((v-35)/5)-1)
	mtau = 1/(am + bm)
	minf = am/(am + bm)
}