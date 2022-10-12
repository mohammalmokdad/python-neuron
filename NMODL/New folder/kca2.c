/* Created by Language version: 7.7.0 */
/* VECTORIZED */
#define NRN_VECTORIZED 1
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "mech_api.h"
#undef PI
#define nil 0
#include "md1redef.h"
#include "section.h"
#include "nrniv_mf.h"
#include "md2redef.h"
 
#if METHOD3
extern int _method3;
#endif

#if !NRNGPU
#undef exp
#define exp hoc_Exp
extern double hoc_Exp(double);
#endif
 
#define nrn_init _nrn_init__kca2
#define _nrn_initial _nrn_initial__kca2
#define nrn_cur _nrn_cur__kca2
#define _nrn_current _nrn_current__kca2
#define nrn_jacob _nrn_jacob__kca2
#define nrn_state _nrn_state__kca2
#define _net_receive _net_receive__kca2 
#define rates rates__kca2 
#define states states__kca2 
 
#define _threadargscomma_ _p, _ppvar, _thread, _nt,
#define _threadargsprotocomma_ double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt,
#define _threadargs_ _p, _ppvar, _thread, _nt
#define _threadargsproto_ double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt
 	/*SUPPRESS 761*/
	/*SUPPRESS 762*/
	/*SUPPRESS 763*/
	/*SUPPRESS 765*/
	 extern double *getarg();
 /* Thread safe. No static _p or _ppvar. */
 
#define t _nt->_t
#define dt _nt->_dt
#define g _p[0]
#define g_columnindex 0
#define depth1 _p[1]
#define depth1_columnindex 1
#define taur1 _p[2]
#define taur1_columnindex 2
#define depth2 _p[3]
#define depth2_columnindex 3
#define taur2 _p[4]
#define taur2_columnindex 4
#define ik _p[5]
#define ik_columnindex 5
#define ica _p[6]
#define ica_columnindex 6
#define icaL _p[7]
#define icaL_columnindex 7
#define n _p[8]
#define n_columnindex 8
#define ca _p[9]
#define ca_columnindex 9
#define caL _p[10]
#define caL_columnindex 10
#define cai _p[11]
#define cai_columnindex 11
#define ek _p[12]
#define ek_columnindex 12
#define ninf _p[13]
#define ninf_columnindex 13
#define ntau _p[14]
#define ntau_columnindex 14
#define drive_channel1 _p[15]
#define drive_channel1_columnindex 15
#define drive_channel2 _p[16]
#define drive_channel2_columnindex 16
#define Dn _p[17]
#define Dn_columnindex 17
#define Dca _p[18]
#define Dca_columnindex 18
#define DcaL _p[19]
#define DcaL_columnindex 19
#define v _p[20]
#define v_columnindex 20
#define _g _p[21]
#define _g_columnindex 21
#define _ion_ek	*_ppvar[0]._pval
#define _ion_ik	*_ppvar[1]._pval
#define _ion_dikdv	*_ppvar[2]._pval
#define _ion_ica	*_ppvar[3]._pval
#define _ion_cai	*_ppvar[4]._pval
#define _style_ca	*((int*)_ppvar[5]._pvoid)
#define _ion_icaL	*_ppvar[6]._pval
 
#if MAC
#if !defined(v)
#define v _mlhv
#endif
#if !defined(h)
#define h _mlhh
#endif
#endif
 
#if defined(__cplusplus)
extern "C" {
#endif
 static int hoc_nrnpointerindex =  -1;
 static Datum* _extcall_thread;
 static Prop* _extcall_prop;
 /* external NEURON variables */
 extern double celsius;
 /* declaration of user functions */
 static void _hoc_rates(void);
 static int _mechtype;
extern void _nrn_cacheloop_reg(int, int);
extern void hoc_register_prop_size(int, int, int);
extern void hoc_register_limits(int, HocParmLimits*);
extern void hoc_register_units(int, HocParmUnits*);
extern void nrn_promote(Prop*, int, int);
extern Memb_func* memb_func;
 
#define NMODL_TEXT 1
#if NMODL_TEXT
static const char* nmodl_file_text;
static const char* nmodl_filename;
extern void hoc_reg_nmodl_text(int, const char*);
extern void hoc_reg_nmodl_filename(int, const char*);
#endif

 extern void _nrn_setdata_reg(int, void(*)(Prop*));
 static void _setdata(Prop* _prop) {
 _extcall_prop = _prop;
 }
 static void _hoc_setdata() {
 Prop *_prop, *hoc_getdata_range(int);
 _prop = hoc_getdata_range(_mechtype);
   _setdata(_prop);
 hoc_retpushx(1.);
}
 /* connect user functions to hoc names */
 static VoidFunc hoc_intfunc[] = {
 "setdata_kca2", _hoc_setdata,
 "rates_kca2", _hoc_rates,
 0, 0
};
 /* declare global and static user variables */
#define Rb Rb_kca2
 double Rb = 0.1;
#define Ra Ra_kca2
 double Ra = 0.1;
#define cainf cainf_kca2
 double cainf = 0.0001;
#define caix caix_kca2
 double caix = 2;
 /* some parameters have upper and lower limits */
 static HocParmLimits _hoc_parm_limits[] = {
 0,0,0
};
 static HocParmUnits _hoc_parm_units[] = {
 "g_kca2", "S/cm2",
 "depth1_kca2", "um",
 "taur1_kca2", "ms",
 "depth2_kca2", "um",
 "taur2_kca2", "ms",
 "ca_kca2", "mM",
 "caL_kca2", "mM",
 "ik_kca2", "mA/cm2",
 "ica_kca2", "mA/cm2",
 "icaL_kca2", "mA/cm2",
 0,0
};
 static double caL0 = 0;
 static double ca0 = 0;
 static double delta_t = 0.01;
 static double n0 = 0;
 /* connect global user variables to hoc */
 static DoubScal hoc_scdoub[] = {
 "caix_kca2", &caix_kca2,
 "cainf_kca2", &cainf_kca2,
 "Ra_kca2", &Ra_kca2,
 "Rb_kca2", &Rb_kca2,
 0,0
};
 static DoubVec hoc_vdoub[] = {
 0,0,0
};
 static double _sav_indep;
 static void nrn_alloc(Prop*);
static void  nrn_init(NrnThread*, _Memb_list*, int);
static void nrn_state(NrnThread*, _Memb_list*, int);
 static void nrn_cur(NrnThread*, _Memb_list*, int);
static void  nrn_jacob(NrnThread*, _Memb_list*, int);
 
static int _ode_count(int);
static void _ode_map(int, double**, double**, double*, Datum*, double*, int);
static void _ode_spec(NrnThread*, _Memb_list*, int);
static void _ode_matsol(NrnThread*, _Memb_list*, int);
 
#define _cvode_ieq _ppvar[7]._i
 static void _ode_synonym(int, double**, Datum**);
 static void _ode_matsol_instance1(_threadargsproto_);
 /* connect range variables in _p that hoc is supposed to know about */
 static const char *_mechanism[] = {
 "7.7.0",
"kca2",
 "g_kca2",
 "depth1_kca2",
 "taur1_kca2",
 "depth2_kca2",
 "taur2_kca2",
 0,
 "ik_kca2",
 "ica_kca2",
 "icaL_kca2",
 0,
 "n_kca2",
 "ca_kca2",
 "caL_kca2",
 0,
 0};
 static Symbol* _k_sym;
 static Symbol* _ca_sym;
 static Symbol* _caL_sym;
 
extern Prop* need_memb(Symbol*);

static void nrn_alloc(Prop* _prop) {
	Prop *prop_ion;
	double *_p; Datum *_ppvar;
 	_p = nrn_prop_data_alloc(_mechtype, 22, _prop);
 	/*initialize range parameters*/
 	g = 0.03;
 	depth1 = 0.1;
 	taur1 = 20;
 	depth2 = 10;
 	taur2 = 200;
 	_prop->param = _p;
 	_prop->param_size = 22;
 	_ppvar = nrn_prop_datum_alloc(_mechtype, 8, _prop);
 	_prop->dparam = _ppvar;
 	/*connect ionic variables to this model*/
 prop_ion = need_memb(_k_sym);
 nrn_promote(prop_ion, 0, 1);
 	_ppvar[0]._pval = &prop_ion->param[0]; /* ek */
 	_ppvar[1]._pval = &prop_ion->param[3]; /* ik */
 	_ppvar[2]._pval = &prop_ion->param[4]; /* _ion_dikdv */
 prop_ion = need_memb(_ca_sym);
 nrn_check_conc_write(_prop, prop_ion, 1);
 nrn_promote(prop_ion, 3, 0);
 	_ppvar[3]._pval = &prop_ion->param[3]; /* ica */
 	_ppvar[4]._pval = &prop_ion->param[1]; /* cai */
 	_ppvar[5]._pvoid = (void*)(&(prop_ion->dparam[0]._i)); /* iontype for ca */
 prop_ion = need_memb(_caL_sym);
 	_ppvar[6]._pval = &prop_ion->param[3]; /* icaL */
 
}
 static void _initlists();
  /* some states have an absolute tolerance */
 static Symbol** _atollist;
 static HocStateTolerance _hoc_state_tol[] = {
 0,0
};
 static void _update_ion_pointer(Datum*);
 extern Symbol* hoc_lookup(const char*);
extern void _nrn_thread_reg(int, int, void(*)(Datum*));
extern void _nrn_thread_table_reg(int, void(*)(double*, Datum*, Datum*, NrnThread*, int));
extern void hoc_register_tolerance(int, HocStateTolerance*, Symbol***);
extern void _cvode_abstol( Symbol**, double*, int);

 void _kca2_reg() {
	int _vectorized = 1;
  _initlists();
 	ion_reg("k", -10000.);
 	ion_reg("ca", -10000.);
 	ion_reg("caL", -10000.);
 	_k_sym = hoc_lookup("k_ion");
 	_ca_sym = hoc_lookup("ca_ion");
 	_caL_sym = hoc_lookup("caL_ion");
 	register_mech(_mechanism, nrn_alloc,nrn_cur, nrn_jacob, nrn_state, nrn_init, hoc_nrnpointerindex, 1);
 _mechtype = nrn_get_mechtype(_mechanism[1]);
     _nrn_setdata_reg(_mechtype, _setdata);
     _nrn_thread_reg(_mechtype, 2, _update_ion_pointer);
 #if NMODL_TEXT
  hoc_reg_nmodl_text(_mechtype, nmodl_file_text);
  hoc_reg_nmodl_filename(_mechtype, nmodl_filename);
#endif
  hoc_register_prop_size(_mechtype, 22, 8);
  hoc_register_dparam_semantics(_mechtype, 0, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 1, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 2, "k_ion");
  hoc_register_dparam_semantics(_mechtype, 3, "ca_ion");
  hoc_register_dparam_semantics(_mechtype, 4, "ca_ion");
  hoc_register_dparam_semantics(_mechtype, 5, "#ca_ion");
  hoc_register_dparam_semantics(_mechtype, 6, "caL_ion");
  hoc_register_dparam_semantics(_mechtype, 7, "cvodeieq");
 	nrn_writes_conc(_mechtype, 0);
 	hoc_register_cvode(_mechtype, _ode_count, _ode_map, _ode_spec, _ode_matsol);
 	hoc_register_tolerance(_mechtype, _hoc_state_tol, &_atollist);
 	hoc_register_synonym(_mechtype, _ode_synonym);
 	hoc_register_var(hoc_scdoub, hoc_vdoub, hoc_intfunc);
 	ivoc_help("help ?1 kca2 kca2.mod\n");
 hoc_register_limits(_mechtype, _hoc_parm_limits);
 hoc_register_units(_mechtype, _hoc_parm_units);
 }
 
#define FARADAY _nrnunit_FARADAY[_nrnunit_use_legacy_]
static double _nrnunit_FARADAY[2] = {0x1.78e555060882cp+16, 96485.3}; /* 96485.3321233100141 */
static int _reset;
static char *modelname = "";

static int error;
static int _ninits = 0;
static int _match_recurse=1;
static void _modl_cleanup(){ _match_recurse=1;}
static int rates(_threadargsprotocomma_ double);
 
static int _ode_spec1(_threadargsproto_);
/*static int _ode_matsol1(_threadargsproto_);*/
 static int _slist1[3], _dlist1[3];
 static int states(_threadargsproto_);
 
/*CVODE*/
 static int _ode_spec1 (double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt) {int _reset = 0; {
   drive_channel1 = - ( 10000.0 ) * ica / ( 2.0 * FARADAY * depth1 ) ;
   if ( drive_channel1 <= 0. ) {
     drive_channel1 = 0. ;
     }
   Dca = drive_channel1 + ( cainf - ca ) / taur1 ;
   drive_channel2 = - ( 10000.0 ) * icaL / ( 2.0 * FARADAY * depth2 ) ;
   if ( drive_channel2 <= 0. ) {
     drive_channel2 = 0. ;
     }
   DcaL = drive_channel2 + ( cainf - caL ) / taur2 ;
   cai = ca + caL ;
   rates ( _threadargscomma_ cai ) ;
   Dn = ( ninf - n ) / ntau ;
   }
 return _reset;
}
 static int _ode_matsol1 (double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt) {
 drive_channel1 = - ( 10000.0 ) * ica / ( 2.0 * FARADAY * depth1 ) ;
 if ( drive_channel1 <= 0. ) {
   drive_channel1 = 0. ;
   }
 Dca = Dca  / (1. - dt*( ( ( ( - 1.0 ) ) ) / taur1 )) ;
 drive_channel2 = - ( 10000.0 ) * icaL / ( 2.0 * FARADAY * depth2 ) ;
 if ( drive_channel2 <= 0. ) {
   drive_channel2 = 0. ;
   }
 DcaL = DcaL  / (1. - dt*( ( ( ( - 1.0 ) ) ) / taur2 )) ;
 cai = ca + caL ;
 rates ( _threadargscomma_ cai ) ;
 Dn = Dn  / (1. - dt*( ( ( ( - 1.0 ) ) ) / ntau )) ;
  return 0;
}
 /*END CVODE*/
 static int states (double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt) { {
   drive_channel1 = - ( 10000.0 ) * ica / ( 2.0 * FARADAY * depth1 ) ;
   if ( drive_channel1 <= 0. ) {
     drive_channel1 = 0. ;
     }
    ca = ca + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / taur1)))*(- ( drive_channel1 + ( ( cainf ) ) / taur1 ) / ( ( ( ( - 1.0 ) ) ) / taur1 ) - ca) ;
   drive_channel2 = - ( 10000.0 ) * icaL / ( 2.0 * FARADAY * depth2 ) ;
   if ( drive_channel2 <= 0. ) {
     drive_channel2 = 0. ;
     }
    caL = caL + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / taur2)))*(- ( drive_channel2 + ( ( cainf ) ) / taur2 ) / ( ( ( ( - 1.0 ) ) ) / taur2 ) - caL) ;
   cai = ca + caL ;
   rates ( _threadargscomma_ cai ) ;
    n = n + (1. - exp(dt*(( ( ( - 1.0 ) ) ) / ntau)))*(- ( ( ( ninf ) ) / ntau ) / ( ( ( ( - 1.0 ) ) ) / ntau ) - n) ;
   }
  return 0;
}
 
static int  rates ( _threadargsprotocomma_ double _lcai ) {
   double _la , _lb ;
  _la = Ra * pow( ( 1e3 * ( _lcai - cainf ) ) , caix ) ;
   _lb = Rb ;
   ntau = 1.0 / ( _la + _lb ) ;
   ninf = _la * ntau ;
     return 0; }
 
static void _hoc_rates(void) {
  double _r;
   double* _p; Datum* _ppvar; Datum* _thread; NrnThread* _nt;
   if (_extcall_prop) {_p = _extcall_prop->param; _ppvar = _extcall_prop->dparam;}else{ _p = (double*)0; _ppvar = (Datum*)0; }
  _thread = _extcall_thread;
  _nt = nrn_threads;
 _r = 1.;
 rates ( _p, _ppvar, _thread, _nt, *getarg(1) );
 hoc_retpushx(_r);
}
 
static int _ode_count(int _type){ return 3;}
 
static void _ode_spec(NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  ek = _ion_ek;
  ica = _ion_ica;
  cai = _ion_cai;
  icaL = _ion_icaL;
     _ode_spec1 (_p, _ppvar, _thread, _nt);
   _ion_cai = cai;
 }}
 
static void _ode_map(int _ieq, double** _pv, double** _pvdot, double* _pp, Datum* _ppd, double* _atol, int _type) { 
	double* _p; Datum* _ppvar;
 	int _i; _p = _pp; _ppvar = _ppd;
	_cvode_ieq = _ieq;
	for (_i=0; _i < 3; ++_i) {
		_pv[_i] = _pp + _slist1[_i];  _pvdot[_i] = _pp + _dlist1[_i];
		_cvode_abstol(_atollist, _atol, _i);
	}
 }
 static void _ode_synonym(int _cnt, double** _pp, Datum** _ppd) { 
	double* _p; Datum* _ppvar;
 	int _i; 
	for (_i=0; _i < _cnt; ++_i) {_p = _pp[_i]; _ppvar = _ppd[_i];
 _ion_cai =  ca + caL ;
 }}
 
static void _ode_matsol_instance1(_threadargsproto_) {
 _ode_matsol1 (_p, _ppvar, _thread, _nt);
 }
 
static void _ode_matsol(NrnThread* _nt, _Memb_list* _ml, int _type) {
   double* _p; Datum* _ppvar; Datum* _thread;
   Node* _nd; double _v; int _iml, _cntml;
  _cntml = _ml->_nodecount;
  _thread = _ml->_thread;
  for (_iml = 0; _iml < _cntml; ++_iml) {
    _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
    _nd = _ml->_nodelist[_iml];
    v = NODEV(_nd);
  ek = _ion_ek;
  ica = _ion_ica;
  cai = _ion_cai;
  icaL = _ion_icaL;
 _ode_matsol_instance1(_threadargs_);
 }}
 extern void nrn_update_ion_pointer(Symbol*, Datum*, int, int);
 static void _update_ion_pointer(Datum* _ppvar) {
   nrn_update_ion_pointer(_k_sym, _ppvar, 0, 0);
   nrn_update_ion_pointer(_k_sym, _ppvar, 1, 3);
   nrn_update_ion_pointer(_k_sym, _ppvar, 2, 4);
   nrn_update_ion_pointer(_ca_sym, _ppvar, 3, 3);
   nrn_update_ion_pointer(_ca_sym, _ppvar, 4, 1);
   nrn_update_ion_pointer(_caL_sym, _ppvar, 6, 3);
 }

static void initmodel(double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt) {
  int _i; double _save;{
  caL = caL0;
  ca = ca0;
  n = n0;
 {
   ca = cainf ;
   caL = 0.0 ;
   cai = cainf ;
   rates ( _threadargscomma_ cai ) ;
   n = ninf ;
   }
 
}
}

static void nrn_init(NrnThread* _nt, _Memb_list* _ml, int _type){
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v = _v;
  ek = _ion_ek;
  ica = _ion_ica;
  cai = _ion_cai;
  icaL = _ion_icaL;
 initmodel(_p, _ppvar, _thread, _nt);
   _ion_cai = cai;
  nrn_wrote_conc(_ca_sym, (&(_ion_cai)) - 1, _style_ca);
}
}

static double _nrn_current(double* _p, Datum* _ppvar, Datum* _thread, NrnThread* _nt, double _v){double _current=0.;v=_v;{ {
   ik = g * n * ( v - ek ) ;
   }
 _current += ik;

} return _current;
}

static void nrn_cur(NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; double _rhs, _v; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
  ek = _ion_ek;
  ica = _ion_ica;
  cai = _ion_cai;
  icaL = _ion_icaL;
 _g = _nrn_current(_p, _ppvar, _thread, _nt, _v + .001);
 	{ double _dik;
  _dik = ik;
 _rhs = _nrn_current(_p, _ppvar, _thread, _nt, _v);
  _ion_dikdv += (_dik - ik)/.001 ;
 	}
 _g = (_g - _rhs)/.001;
  _ion_ik += ik ;
  _ion_cai = cai;
#if CACHEVEC
  if (use_cachevec) {
	VEC_RHS(_ni[_iml]) -= _rhs;
  }else
#endif
  {
	NODERHS(_nd) -= _rhs;
  }
 
}
 
}

static void nrn_jacob(NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml];
#if CACHEVEC
  if (use_cachevec) {
	VEC_D(_ni[_iml]) += _g;
  }else
#endif
  {
     _nd = _ml->_nodelist[_iml];
	NODED(_nd) += _g;
  }
 
}
 
}

static void nrn_state(NrnThread* _nt, _Memb_list* _ml, int _type) {
double* _p; Datum* _ppvar; Datum* _thread;
Node *_nd; double _v = 0.0; int* _ni; int _iml, _cntml;
#if CACHEVEC
    _ni = _ml->_nodeindices;
#endif
_cntml = _ml->_nodecount;
_thread = _ml->_thread;
for (_iml = 0; _iml < _cntml; ++_iml) {
 _p = _ml->_data[_iml]; _ppvar = _ml->_pdata[_iml];
 _nd = _ml->_nodelist[_iml];
#if CACHEVEC
  if (use_cachevec) {
    _v = VEC_V(_ni[_iml]);
  }else
#endif
  {
    _nd = _ml->_nodelist[_iml];
    _v = NODEV(_nd);
  }
 v=_v;
{
  ek = _ion_ek;
  ica = _ion_ica;
  cai = _ion_cai;
  icaL = _ion_icaL;
 {   states(_p, _ppvar, _thread, _nt);
  }   _ion_cai = cai;
}}

}

static void terminal(){}

static void _initlists(){
 double _x; double* _p = &_x;
 int _i; static int _first = 1;
  if (!_first) return;
 _slist1[0] = ca_columnindex;  _dlist1[0] = Dca_columnindex;
 _slist1[1] = caL_columnindex;  _dlist1[1] = DcaL_columnindex;
 _slist1[2] = n_columnindex;  _dlist1[2] = Dn_columnindex;
_first = 0;
}

#if defined(__cplusplus)
} /* extern "C" */
#endif

#if NMODL_TEXT
static const char* nmodl_filename = "kca2.mod";
static const char* nmodl_file_text = 
  "\n"
  " COMMENT\n"
  " \n"
  " kca2.mod\n"
  " \n"
  " Calcium-dependent potassium channel\n"
  " Based on\n"
  " Pennefather (1990) -- sympathetic ganglion cells\n"
  " taken from\n"
  " Reuveni et al (1993) -- neocortical cells\n"
  " \n"
  " Author: Zach Mainen, Salk Institute, 1995, zach@salk.edu\n"
  " modified Jan,2000 by RKP;modified July 2005 to include a contribution from calcium\n"
  "flowing through L channels\n"
  " 	\n"
  " ENDCOMMENT\n"
  "\n"
  " NEURON {\n"
  " 	SUFFIX kca2\n"
  " 	USEION k READ ek WRITE ik\n"
  " 	USEION ca READ ica WRITE cai\n"
  "  USEION caL READ icaL 	\n"
  "  RANGE n, g,ik,cai,ica,icaL,depth1,taur1,depth2,taur2\n"
  " 	GLOBAL Ra, Rb, caix\n"
  " }\n"
  " \n"
  " UNITS {\n"
  " 	(mA) = (milliamp)\n"
  " 	(mV) = (millivolt)\n"
  " 	(S) = (siemens)\n"
  " 	(um) = (micron)\n"
  " 	(molar) = (1/liter)			: moles do not appear in units\n"
  " 	(mM)	= (millimolar)\n"
  " 	(msM)	= (ms mM)\n"
  " 	FARADAY = (faraday) (coulomb)\n"
  " } \n"
  " \n"
  " PARAMETER {\n"
  " 	g = 0.03   	(S/cm2)	\n"
  " 	v 		(mV)\n"
  " 	cai  		(mM)\n"
  " 	caix = 2	\n"
  "  cainf=0.0001\n"
  " 	depth1	= .1	(um)		: depth of shell\n"
  " 	taur1	= 20	(ms)		: rate of calcium removal\n"
  " 	depth2	= 10	(um)		: depth of shell\n"
  " 	taur2	= 200	(ms)		: rate of calcium removal\n"
  "								\n"
  "  Ra   = 0.1		: max act rate  \n"
  " 	Rb   = 0.1		: max deact rate \n"
  " \n"
  " 	celsius		(degC)\n"
  " } \n"
  " \n"
  " \n"
  " ASSIGNED {\n"
  " 	ik 		(mA/cm2)\n"
  "	 ica (mA/cm2)\n"
  " 	icaL (mA/cm2)\n"
  " 	ek		(mV)\n"
  " 	ninf\n"
  " 	ntau 		(ms)	\n"
  "  drive_channel1	(mM/ms)\n"
  "  drive_channel2	(mM/ms)\n"
  " }\n"
  "  \n"
  " \n"
  " STATE { \n"
  " n \n"
  " ca (mM)\n"
  "	caL (mM)\n"
  "}\n"
  " \n"
  " INITIAL { \n"
  "	ca=cainf\n"
  " caL=0\n"
  " cai=cainf\n"
  " rates(cai)\n"
  " 	n = ninf\n"
  " }\n"
  " \n"
  " BREAKPOINT {\n"
  "         SOLVE states METHOD cnexp\n"
  " 	ik =  g *n* (v - ek)\n"
  " } \n"
  " \n"
  "\n"
  "DERIVATIVE states {  \n"
  " 	drive_channel1 =  - (10000) * ica/ (2 * FARADAY * depth1)\n"
  " 	if (drive_channel1 <= 0.) { drive_channel1 = 0. }	: cannot pump inward\n"
  " 	ca' = drive_channel1 + (cainf-ca)/taur1\n"
  " 	drive_channel2 =  - (10000) * icaL/ (2 * FARADAY * depth2)\n"
  " 	if (drive_channel2 <= 0.) { drive_channel2 = 0. }	: cannot pump inward\n"
  " 	caL' = drive_channel2 + (cainf-caL)/taur2\n"
  " 	cai = ca + caL\n"
  "\n"
  "          rates(cai)    \n"
  "         n' = (ninf-n)/ntau\n"
  "}\n"
  "PROCEDURE rates(cai(mM)) {  LOCAL a,b\n"
  "							UNITSOFF\n"
  "         a = Ra * (1e3*(cai  -cainf))^caix		: rate constant depends on cai in uM\n"
  "         b = Rb\n"
  "         ntau = 1/(a+b)\n"
  "        	ninf = a*ntau\n"
  "					UNITSON\n"
  " }\n"
  ;
#endif
