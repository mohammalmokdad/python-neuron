TITLE CalConc
: Calculates intracellular calcium concentration

NEURON {
	SUFFIX CaN
	USEION ca READ ica WRITE cai
	RANGE cai, cca, ica, ican
}

UNITS {
	(molar) = (1/liter)
	(mV) = (millivolt)
	(mA) = (milliamp)
	(mM) = (millimolar)
}

PARAMETER {
	B = 0
	tau = 13.33 (ms)
}

ASSIGNED { 
	ican (mA/cm2)
	ica (mA/cm2)
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
