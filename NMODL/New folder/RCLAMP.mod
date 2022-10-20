COMMENT
RClamp: Injects a triangular up-&-down current with similar parameters
        to NEURON's IClamp.
Since this is an electrode current, positive values of i depolarize the cell
and in the presence of the extracellular mechanism there will be a change
in vext since i is not a transmembrane current but a current injected
directly to the inside of the cell.

Revision: 28July2021 added in a bias current to remove the need to add
this feature using a separate IClamp
ENDCOMMENT

NEURON {
        POINT_PROCESS RClamp
        RANGE del, dur, pkamp, bias
        ELECTRODE_CURRENT i
}

UNITS {
        (nA) = (nanoamp)
      
       }

PARAMETER {
        del=0	(ms)
        dur=0	(ms)
        pkamp=0 (nA)
        bias=0  (nA)
}

ASSIGNED {
        i (nA)
}

BREAKPOINT {
        if (t < del) {
		i=0	
	}else{  
              if (t < del+(dur/2)) {
		i = (t-del)*(pkamp/(dur/2))+bias
		}else{  
			if (t < del +2*(dur/2)) {
				i = (t-del-(dur/2))*(-pkamp/(dur/2))+pkamp+bias
        		}else{
				i = 0
			}}}

}
