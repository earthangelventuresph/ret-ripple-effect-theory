"""
RET CORE — Shared functions for E1-E5
EAV-RET-001 | v1.0 | 24 Oct 2026 | Angelica Pangan
No data. Pure math from manuscript Eq.1-25.
"""
import numpy as np
from scipy import stats

# --- FROZEN CONSTANTS ---
MC = 5
THETA_K = 3.0
ALPHA = 0.05
N_BOOT = 10000
PSI_LO, PSI_HI = 0.85, 1.15
CHI_LO, CHI_HI = -0.10, 0.10
SE_SP_MIN = 0.90

def spectral_radius(A):
    A = np.asarray(A, dtype=float)
    return float(np.max(np.abs(np.linalg.eigvals(A))))

def hop_gain(Gamma, kappa):
    Gamma = np.asarray(Gamma, dtype=float); kappa = np.asarray(kappa, dtype=float)
    return Gamma / kappa[:, None]

def total_dose(A, M0):
    A = np.asarray(A, dtype=float); M0 = np.asarray(M0, dtype=float)
    return np.linalg.solve(np.eye(A.shape[0]) - A, M0)

def hop_doses(A, M0, Kmax):
    out = []
    cur = np.asarray(M0, dtype=float)
    for k in range(Kmax+1):
        out.append(cur.copy())
        cur = A @ cur
    return out

def hop_totals(A, M0, Kmax):
    return np.array([np.sum(v) for v in hop_doses(A, M0, Kmax)])

def attenuation_lambda(Omega):
    return float(-np.log(Omega)) if Omega > 0 else float('inf')

def attenuation_length(Omega):
    lam = attenuation_lambda(Omega)
    return 1.0/lam if lam > 0 and np.isfinite(lam) else float('inf')

def amplification(M, M0_s):
    return float(np.sum(M) / M0_s) if M0_s != 0 else float('nan')

def min_delay_path(tau, s, target):
    # Dijkstra on delays. tau[i,j] = delay j->i. tau[i,j]=inf if no coupling.
    import heapq
    N = tau.shape[0]
    dist = np.full(N, np.inf); dist[s] = 0.0
    pq = [(0.0, s)]
    while pq:
        d,u = heapq.heappop(pq)
        if d > dist[u]: continue
        for v in range(N):
            w = tau[v, u]
            if np.isfinite(w) and dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return float(dist[target]), dist

def reachability(A):
    # Ris >0 iff path exists. Boolean reachability via powers.
    N = A.shape[0]
    B = (np.abs(A) > 0).astype(int)
    R = np.eye(N, dtype=int)
    P = np.eye(N, dtype=int)
    for _ in range(N):
        P = P @ B
        R = np.clip(R + P, 0, 1)
    return R

def arrival_time(t, delta, theta, mc=MC):
    # First time delta exceeds theta for mc consecutive samples
    above = np.abs(delta) > theta
    for i in range(len(delta)-mc+1):
        if np.all(above[i:i+mc]):
            return float(t[i])
    return float('nan')

def dose_integral(t, delta):
    return float(np.trapezoid(delta, t))

def parity_fit(ln_pred, ln_obs):
    # OLS ln_obs = psi*ln_pred + chi
    X = np.column_stack([ln_pred, np.ones_like(ln_pred)])
    coef, *_ = np.linalg.lstsq(X, ln_obs, rcond=None)
    return float(coef[0]), float(coef[1])

def bootstrap_parity(ln_pred, ln_obs, groups, n_boot=N_BOOT, seed=20261024):
    # Resample trials within each cell (group), recompute cell means, refit.
    rng = np.random.default_rng(seed)
    uniq = np.unique(groups)
    psis, chis = [], []
    for _ in range(n_boot):
        lp, lo = [], []
        for g in uniq:
            idx = np.where(groups==g)[0]
            samp = rng.choice(idx, size=len(idx), replace=True)
            lp.append(np.mean(ln_pred[samp])); lo.append(np.mean(ln_obs[samp]))
        psi, chi = parity_fit(np.array(lp), np.array(lo))
        psis.append(psi); chis.append(chi)
    return (float(np.percentile(psis,5)), float(np.percentile(psis,95)),
            float(np.percentile(chis,5)), float(np.percentile(chis,95)))

def clopper_pearson(k, n, alpha=0.05):
    # Two-sided 95% CI. Lower bound used for Se/Sp.
    if n == 0: return (0.0, 1.0)
    lo = stats.beta.ppf(alpha/2, k, n-k+1) if k>0 else 0.0
    hi = stats.beta.ppf(1-alpha/2, k+1, n-k) if k<n else 1.0
    return float(lo), float(hi)

def spearman(x, y):
    return float(stats.spearmanr(x, y).statistic)

def worked_example():
    A = np.array([[0,0.30,0.10],[0.40,0,0.20],[0.20,0.30,0]], dtype=float)
    kappa = np.array([2.0,2.0,2.0]); eps = 1.0; s=0
    M0 = np.zeros(3); M0[s]=eps/kappa[s]
    M = total_dose(A, M0)
    Om = spectral_radius(A)
    Mk = hop_totals(A, M0, 5)
    return {"A":A.tolist(),"M0":M0.tolist(),"M":M.tolist(),"Omega":Om,
            "lambda":-np.log(Om),"ell":1/(-np.log(Om)),"G1":float(np.sum(M)/M0[s]),"Mk":Mk.tolist()}

if __name__ == "__main__":
    import json; print(json.dumps(worked_example(), indent=2))
    # Expected: Omega 0.498, M [0.606,0.284,0.206], G1 2.19, Mk [0.5,0.3,0.15,0.072,0.0372,0.018]
