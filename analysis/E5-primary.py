"""
RET E5 — Attribution + Common-Cause | EAV-RET-001 | v1.0
Design: 200 blocks A (true), 70 B (common cause), 70 C (mimic), 60 E (unreachable)
= 400 blocks, 2000 trials. Each block: 4 perturbation trials 0.5,1.0,1.5,2.0x base + 1 sham.
Primary: Se = share A blocks RAC=1, Sp = share B,C,E blocks RAC=0.
Threshold: lower 95% Clopper-Pearson Se >=0.90 AND Sp >=0.90.
RAC = q1*q2*q3*q4*q5. See Table 11.
"""
import numpy as np, json
from ret_core import clopper_pearson, spearman

def eval_block(block):
    # block: dict with keys:
    # Ris>0 (bool), Ti, d_tau, Ti_pred, pert_doses[], sham_dose, thetaM,
    # pert_sizes [0.5,1.0,1.5,2.0], doses_by_size [], sham_dose_target,
    # ref_doses []
    q1 = bool(block["Ris_gt_0"])
    q2 = bool(block["Ti"] >= block["d_tau"] and abs(block["Ti"]-block["Ti_pred"]) <= max(0.10*block["Ti_pred"], 0.0005))
    # q3: lower 95% bootstrap bound (pert - sham) > thetaM
    # For a single block, use the 4 pert trials vs sham: bootstrap mean diff
    diff = np.array(block["pert_doses"]) - block["sham_dose"]
    rng = np.random.default_rng(20261024)
    boots = [np.mean(rng.choice(diff, size=len(diff), replace=True)) for _ in range(10000)]
    q3 = bool(np.percentile(boots, 2.5) > block["thetaM"])
    # q4: Spearman >=0.8 between size and dose
    q4 = bool(spearman(block["pert_sizes"], block["doses_by_size"]) >= 0.8)
    # q5: sham dose at target <= thetaM AND all ref doses <= thetaM
    q5 = bool(block["sham_dose_target"] <= block["thetaM"] and np.all(np.array(block["ref_doses"]) <= block["thetaM"]))
    rac = int(q1 and q2 and q3 and q4 and q5)
    return {"q": [int(q1),int(q2),int(q3),int(q4),int(q5)], "RAC": rac,
            "first_fail": next((i+1 for i, q in enumerate([q1,q2,q3,q4,q5]) if not q), None)}

def analyse_e5(blocks_by_condition):
    # blocks_by_condition: {"A": [block,...], "B": [...], "C": [...], "E": [...]}
    results = {}
    for cond, blocks in blocks_by_condition.items():
        evals = [eval_block(b) for b in blocks]
        results[cond] = evals
    nA = len(results["A"])
    n_non = len(results["B"]) + len(results["C"]) + len(results["E"])
    k_se = sum(e["RAC"] for e in results["A"])
    k_sp = sum(1 - e["RAC"] for e in results["B"] + results["C"] + results["E"])
    Se = k_se / nA if nA else float("nan")
    Sp = k_sp / n_non if n_non else float("nan")
    se_lo, se_hi = clopper_pearson(k_se, nA)
    sp_lo, sp_hi = clopper_pearson(k_sp, n_non)
    # Specificity per B/C/E
    per = {}
    for cond in ["B","C","E"]:
        ev = results[cond]
        k = sum(1 - e["RAC"] for e in ev)
        lo, hi = clopper_pearson(k, len(ev))
        per[cond] = {"n": len(ev), "correct_reject": int(k), "Sp": k/len(ev) if ev else float("nan"), "Sp_95CI": [lo, hi]}
    # First failing criterion per non-ripple block
    first_fail_counts = {}
    for cond in ["B","C","E"]:
        counts = {1:0,2:0,3:0,4:0,5:0,None:0}
        for e in results[cond]:
            if e["RAC"] == 0:
                counts[e["first_fail"]] += 1
        first_fail_counts[cond] = counts
    out = {"Se": float(Se), "Se_95CI": [se_lo, se_hi], "Se_lower": float(se_lo),
           "Sp": float(Sp), "Sp_95CI": [sp_lo, sp_hi], "Sp_lower": float(sp_lo),
           "specificity_by_condition": per,
           "first_fail_counts": first_fail_counts,
           "H4_supported": bool(se_lo >= 0.90 and sp_lo >= 0.90),
           "note": "Example: 195/200 correct -> lower 95% bound 0.948; 190/200 -> 0.917."}
    print(json.dumps(out, indent=2)); return out

if __name__ == "__main__":
    print("E5-primary loaded. Call analyse_e5(blocks_by_condition). No data in v1.0.")
