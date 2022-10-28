#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _L_Ca_reg();
extern void _L_Ca_inact_reg();
extern void _RCLAMP_reg();
extern void _gh_reg();
extern void _kca2_reg();
extern void _kdrRL_reg();
extern void _mAHP_reg();
extern void _na3rp_reg();
extern void _naps_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," L_Ca.mod");
fprintf(stderr," L_Ca_inact.mod");
fprintf(stderr," RCLAMP.mod");
fprintf(stderr," gh.mod");
fprintf(stderr," kca2.mod");
fprintf(stderr," kdrRL.mod");
fprintf(stderr," mAHP.mod");
fprintf(stderr," na3rp.mod");
fprintf(stderr," naps.mod");
fprintf(stderr, "\n");
    }
_L_Ca_reg();
_L_Ca_inact_reg();
_RCLAMP_reg();
_gh_reg();
_kca2_reg();
_kdrRL_reg();
_mAHP_reg();
_na3rp_reg();
_naps_reg();
}
