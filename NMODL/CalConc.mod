TITLE CalConc
: Calculates intracellular calcium concentration

NEURON {
	SUFFIX CaN
	USEION ca READ ican WRITE cai
	RANGE ican, cai, cca
}

UNITS {
	(mV) = (millivolt)
	(ms) = (ms)
	(mA) = (milliamp)
	(mM) = (millimolar)
}

PARAMETER {
	B = 0
	tau = 13.33 (ms)
}

ASSIGNED {
	ican (mA/cm2)
	i (mA/cm2)
	cai (mM)
}

STATE { 
	cca (mM)
}

BREAKPOINT {
	SOLVE states METHOD cnexp
}

INITIAL {
	cca=0.0001
}

DERIVATIVE states {
	cca' = B*ican - cca/tau
	cai = cca
}
