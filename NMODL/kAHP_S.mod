TITLE kAHP_S
: AHP Conducatance for Soma

NEURON { 
	SUFFIX kAHP_S
	USEION k READ ek WRITE ik
	USEION ca READ cai
	RANGE gkahp_s, ik, g
}

UNITS { 
	(molar) = (1/liter)
	(mV) = (millivolt)
	(mA) = (milliamp)
	(mM) = (millimolar)
}

PARAMETER { 
	gkahp_s = 0 (S/cm2)
}
 
ASSIGNED { 
	v (mV)
	ek (mV)
	ik (mA/cm2)
	i (mA/cm2)
	g (S/cm2)
	cai	(mM)
	qinf qtau
}
 
STATE { 
	q
}

BREAKPOINT { 
	SOLVE states METHOD cnexp
	g = gkahp_s * q
	ik = g * (v - ek)
}

INITIAL {
	rates(cai)
	q = qinf
}

DERIVATIVE states {
	rates(cai)
	q' = (qinf - q)/qtau
}

PROCEDURE rates(cai(mM)) {LOCAL aq, bq 
	aq= cai * 10^(-3)
	bq= 0.04
	qtau = 1/(aq + bq)
	qinf = aq/(aq + bq)
}