"""
RET E3 — Wave Tank Primary | EAV-RET-001 | v1.0
Primary: spreading exponent n radial (pred 0.5) + channel (pred 0).
Model: ln a = ln a0 - n*ln(r/r0) - eta*(r-r0)
"""
import numpy as np, json
from scipy.optimize import curve_fit

R_RADIAL = np.array([0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45])
X_CHANNEL = np.array([0.20,0.52,0.84,1.16,1.48,1.80])
R0 = 0.10

def model_log(r, log_a0, n, eta, r0=R0):
    return log_a0 - n*np.log(r/r0) - eta*(r-r0)

def fit_n_eta(r, a):
    # a = amplitudes per radius (mean over runs)
    popt,_=curve_fit(model_log, r, np.log(a), p0=[np.log(a[0]),0.5,0.1], maxfev=10000)
    return float(popt[1]), float(popt[2]), float(popt[0])

def bootstrap_n(r, amps_runs, n_boot=10000, seed=20261024):
    # amps_runs: shape (n_runs, n_radii)
    rng=np.random.default_rng(seed); ns=[]; etas=[]
    for _ in range(n_boot):
        idx=rng.integers(0, amps_runs.shape[0], size=amps_runs.shape[0])
        mean_amp=np.mean(amps_runs[idx], axis=0)
        try:
            n, eta, _ = fit_n_eta(r, mean_amp); ns.append(n); etas.append(eta)
        except Exception: continue
    return float(np.percentile(ns,5)), float(np.percentile(ns,95)), float(np.percentile(etas,5)), float(np.percentile(etas,95))

def analyse_e3(radial_amps, channel_amps):
    # radial_amps: (32,8), channel_amps: (32,6)
    n_r, eta_r, _ = fit_n_eta(R_RADIAL, np.mean(radial_amps, axis=0))
    n_c, eta_c, _ = fit_n_eta(X_CHANNEL, np.mean(channel_amps, axis=0), )
    # For channel, r0 should be 0.20 (first probe) — refit with r0=0.20
    def model_c(x, la0, n, eta): return la0 - n*np.log(x/0.20) - eta*(x-0.20)
    from scipy.optimize import curve_fit as cf
    popt,_=cf(model_c, X_CHANNEL, np.log(np.mean(channel_amps,axis=0)), p0=[0,0,0.1])
    n_c=float(popt[1]); eta_c=float(popt[2])
    n_r_lo, n_r_hi, _, _ = bootstrap_n(R_RADIAL, radial_amps)
    # Channel bootstrap
    rng=np.random.default_rng(20261024); ncs=[]
    for _ in range(10000):
        idx=rng.integers(0, channel_amps.shape[0], size=channel_amps.shape[0])
        m=np.mean(channel_amps[idx],axis=0)
        try:
            p,_=cf(model_c, X_CHANNEL, np.log(m), p0=[0,0,0.1]); ncs.append(float(p[1]))
        except Exception: pass
    n_c_lo, n_c_hi = float(np.percentile(ncs,5)), float(np.percentile(ncs,95))
    out={"radial_n":n_r,"radial_n_90CI":[n_r_lo,n_r_hi],"radial_eta":eta_r,
         "channel_n":n_c,"channel_n_90CI":[n_c_lo,n_c_hi],"channel_eta":eta_c,
         "spreading_supported":bool(0.40<=n_r_lo and n_r_hi<=0.60 and -0.10<=n_c_lo and n_c_hi<=0.10)}
    print(json.dumps(out, indent=2)); return out

if __name__=="__main__":
    print("E3-primary loaded. Call analyse_e3(radial_amps, channel_amps). No data in v1.0.")
