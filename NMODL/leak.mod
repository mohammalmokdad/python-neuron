TITLE leak
: leak current

NEURON {
	SUFFIX leak
	NONSPECIFIC_CURRENT i
	RANGE gleakbar, g
}

UNITS {
	(S) = (siemens)
	(mV) = (millivolt)
	(mA) = (milliamp)
}

PARAMETER {
	gleakbar = 0 (S/cm2)
}

ASSIGNED {
	v (mV)
	ek (mV)
	i (mA/cm2)
	g (S/cm2)
}


BREAKPOINT {
	g = gleakbar
	i = g * (v - ek)
}