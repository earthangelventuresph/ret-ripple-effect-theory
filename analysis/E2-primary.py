"""
RET E2 — Electronic Network Primary | EAV-RET-001 | v1.0
Primary: psi, chi over (condition,node) predicted dose >=5*thetaM, subcritical only.
T1 3 gains + T2 cgOmega0 0.50,0.70,0.85,0.95. Bootstrap 10000.
"""
import numpy as np, json
from ret_core import parity_fit, bootstrap_parity, arrival_time, dose_integral, spectral_radius

# FROZEN
H = 20e-6  # 20 us
T_BASE_END, T_PERT, T_RESP_END = 0.2, 0.2, 1.0
N_TRIALS = 32
THETA_M_FACTOR = 5.0
PSI_LO, PSI_HI = 0.85, 1.15
CHI_LO, CHI_HI = -0.10, 0.10

def compute_dose(t, delta):
    mask=(t>=T_BASE_END)&(t<=T_RESP_END)
    return dose_integral(t[mask], delta[mask])

def analyse_e2(cells):
    # cells: list of dicts {condition, node, ln_pred, ln_obs_trials[], thetaM, d_tau, Ti_pred, Ti_trials[], ...}
    # Build cell means
    ln_pred=[]; ln_obs=[]; groups=[]
    for ci, c in enumerate(cells):
        if c["pred_dose"] < THETA_M_FACTOR*c["thetaM"]: continue
        if c["condition"] not in ["T1_a0.5","T1_a0.7","T1_a0.9","T2_0.50","T2_0.70","T2_0.85","T2_0.95"]: continue
        ln_pred.append(np.log(c["pred_dose"])); ln_obs.append(np.log(np.mean(c["obs_doses"]))); groups.append(ci)
    ln_pred=np.array(ln_pred); ln_obs=np.array(ln_obs); groups=np.array(groups)
    psi, chi = parity_fit(ln_pred, ln_obs)
    # Bootstrap: need per-trial ln_obs per cell
    # Rebuild per-trial arrays for bootstrap_parity
    lp_all=[]; lo_all=[]; g_all=[]
    for ci, c in enumerate(cells):
        if c["pred_dose"] < THETA_M_FACTOR*c["thetaM"]: continue
        if c["condition"] not in ["T1_a0.5","T1_a0.7","T1_a0.9","T2_0.50","T2_0.70","T2_0.85","T2_0.95"]: continue
        for d in c["obs_doses"]:
            lp_all.append(np.log(c["pred_dose"])); lo_all.append(np.log(d)); g_all.append(ci)
    psi_lo, psi_hi, chi_lo, chi_hi = bootstrap_parity(np.array(lp_all), np.array(lo_all), np.array(g_all))
    h2_supported = (PSI_LO<=psi_lo and psi_hi<=PSI_HI and CHI_LO<=chi_lo and chi_hi<=CHI_HI)
    # H1: every must-respond node lower 95% bound dose diff > thetaM
    h1_fail=[]
    for c in cells:
        if c["pred_dose"] < THETA_M_FACTOR*c["thetaM"]: continue
        diff=np.array(c["pert_doses"])-np.array(c["sham_doses"])
        # Bootstrap 95% lower bound
        rng=np.random.default_rng(20261024)
        boots=[np.mean(rng.choice(diff,size=len(diff),replace=True)) for _ in range(10000)]
        lo=np.percentile(boots,2.5)
        if lo<=c["thetaM"]: h1_fail.append(c["condition"]+":"+str(c["node"]))
    # P4: >5% Ti<d_tau or median |Ti-Tipred| > max(10%,0.5ms)
    early=0; total=0; errs=[]
    for c in cells:
        for ti in c.get("Ti_trials",[]):
            total+=1; early+= (ti < c["d_tau"]); errs.append(abs(ti-c["Ti_pred"]))
    p4_fail = (early/total>0.05 if total else False) or (np.median(errs)>max(0.10*np.median([c["Ti_pred"] for c in cells]),0.0005) if errs else False)
    # P5: T1 recurrence
    # Caller passes Trec_pred, Trec_obs, Rrec_pred, Rrec_obs
    out={"psi":psi,"chi":chi,"psi_90CI":[psi_lo,psi_hi],"chi_90CI":[chi_lo,chi_hi],
         "H2_supported":bool(h2_supported),"H1_fail_nodes":h1_fail,"H1_supported":len(h1_fail)==0,
         "P4_early_frac":early/total if total else None,"P4_median_err":float(np.median(errs)) if errs else None,"P4_supported":not p4_fail}
    print(json.dumps(out, indent=2)); return out

if __name__=="__main__":
    print("E2-primary loaded. Call analyse_e2(cells) with real trial data. No data in v1.0.")
