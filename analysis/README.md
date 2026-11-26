# Analysis — RET
Project EAV-RET-001 | v1.0 | 24 Oct 2026 | Status: NO ANALYSIS YET. Code to be frozen + hashed before collection.
Locked Scripts:
- analysis/E1-checks.py — Check1 dose ≤1e-3, Check2 slope ln Mk vs ln Ω ≤0.02, Check3 cascade freq pattern
- analysis/E2-primary.py — Dose integral 0.2-1.0s, ψ,χ OLS, bootstrap 10000 trials, arrival, recurrence, regime, H3 ratio
- analysis/E3-primary.py — Amplitude RMS gate Ti to Ti+0.5s, n,η nonlinear LS bootstrap, arrival vs ri/cmax
- analysis/E4-primary.py — ψ,χ per domain OLS, bootstrap 10000 trials/scenarios, S3 Ω̂ training → test prediction
- analysis/E5-primary.py — RAC per block, Se,Sp Clopper-Pearson, specificity per B/C/E
Rules: One primary per experiment. Secondary 95% CI, no hypothesis claim. Percentile bootstrap 10000, resampling unit trial/scenario. Equivalence 90% CI. Proportions Clopper-Pearson. Analyst blind to perturbation/sham + condition until code frozen. No optional stopping. Fixed n=32 per condition E2/E3. Deviation from threshold/sample size → experiment not supported.
