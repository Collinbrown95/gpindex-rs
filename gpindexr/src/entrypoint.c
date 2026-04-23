#include <R.h>
#include <Rinternals.h>

extern SEXP R_init_gpindexr_extendr(void);

void R_init_gpindexr(DllInfo *dll) {
  R_registerRoutines(dll, NULL, NULL, NULL, NULL);
  R_useDynamicSymbols(dll, FALSE);
  R_forceSymbols(dll, TRUE);
  R_init_gpindexr_extendr();
}
