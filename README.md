[![Version](https://img.shields.io/badge/version-1.0-blue)](CHANGELOG.md)
[![Status](https://img.shields.io/badge/status-hypothesis%20%2B%20protocol-orange)](README.md)
[![License](https://img.shields.io/badge/license-CC%20BY%204.0-green)](LEGAL-ETHICS.md)
[![Project](https://img.shields.io/badge/project-EAV--RET--001-purple)](README.md)
[![Data](https://img.shields.io/badge/data-none%20collected-red)](data/README.md)

# Ripple Effect Theory: A Framework for Propagating Change Across Time and Interconnected Systems (RET)

### A ripple is NOT "B followed A." A ripple is a counterfactual difference that survives path, timing, dose, dose-response, and sham.

**Earth Angel Ventures Theoretical Research Paper**

| Field | Entry |
| :--- | :--- |
| **Full Title** | Ripple Effect Theory: A Framework for Propagating Change Across Time and Interconnected Systems |
| **Short Title** | Ripple Effect Theory (RET) |
| **Classification** | Original theoretical proposal with a complete, pre-specified experimental programme (hypothesis and protocol; no empirical data collected) |
| **Research Program** | Earth Angel Ventures Theoretical Science Program: Propagation, Causality, and Interconnected Systems |
| **Project ID** | EAV-RET-001 |
| **Manuscript ID** | EAV-RET-001-M01 |
| **Status** | Complete manuscript for internal review; ready for registration of the protocol before any data collection |
| **Date** | 24 October 2026 |
| **Primary Discipline** | Complex systems science (dynamical systems and network science) |
| **Secondary Disciplines** | Causal inference and statistics; applied physics (wave propagation, electrical networks); systems engineering (cascading failure) |
| **Lead Author** | Angelica Pangan |
| **Research Owner** | Earth Angel Ventures, Philippines |
| **Version** | 1.0 (supersedes working draft EAV-TH-002) |
| **ORCID** | 0009-0007-2793-5008 — https://orcid.org/0009-0007-2793-5008 |
| **Email** | earthangelventuresph@gmail.com |
| **Contact** | +63 991 967 6122 |
| **【entity-GitHub¦canonical_name=GitHub】** | https://github.com/earthangelventuresph |
| **Origin** | Manila, Philippines — Open Internationally |
| **Field** | Life Sciences, Earth Angel Ventures |

> **Verse:** 1 Corinthians 10:31 | Philippians 2:13

---

## 1. DOCUMENT CONTROL

**Lineage.** Version 1.0 supersedes working draft EAV-TH-002. Every proposition of the working draft is retained and formalised.

**Evidence-status legend.**

| Label | Meaning |
| :--- | :--- |
| ESTABLISHED | Published, widely accepted, independently replicated. Background / tool only. |
| HYPOTHESIS | Proposed here in RET, not yet tested. Quantitative falsification rule given. |
| METHOD | Definition / convention / procedure to make hypothesis testable. |

**Contents.** 1 Document Control; 2 Abstract; 3 Research Significance; 4 Highlights; 5 Visual Emblem; 6 Formula Basis Chart; 7 Symbol and Sign Chart; 8 Visual Blueprints; 9 Introduction, Scope, Hypotheses; 10 Formal Model; 11 Extended Mechanisms; 12 Experimental Programme; 13 Comparison + Novelty; 14 Results; 15 Discussion; 16 Conclusion; 17 Ethics; 18 References; 19 Final Declaration.

**Conventions.** Every symbol defined in Table 5. Every equation collected in Formula Basis Chart §6. Vectors/matrices bold in equation images; in text capital A denotes matrix. Quantities SI units. Bracket [x] = unit of measured state variable: volt in electronic network, metre in wave tank, dimensionless count in cascade models. All figures showing model output labelled model-computed illustrations; they are not data.

---

## 2. ABSTRACT

**Background.** A change in one component of an interconnected system often alters other components later in time and elsewhere in space. Studied under separate names: causal inference, nonlinear dynamics, network cascades, wave propagation. No single operational test currently states when a downstream change is a genuine propagated consequence of an initiating event, as opposed to coincidence or shared cause.

**Objective.** To formalise RET as a bounded and falsifiable framework that predicts magnitude, timing, recurrence, and persistence of downstream effects from independently measured couplings, and states exactly when a downstream change may and may not be attributed to an initiating event.

**Methods.** RET defines ripple field as counterfactual difference between disturbed system and baseline (Eq.3). Eight postulates built on linear delayed network response, Ripple Number Ω (spectral radius of hop-gain matrix), causality bound on arrival time, loop-recurrence law, threshold-cascade criterion, five-part Ripple Attribution Criterion, cross-domain parity law. Five experiments with fixed sample sizes and numerical thresholds: computational verification, 16-node electronic network, fluid surface-wave tank, cross-domain parity over three systems, 400-block attribution test.

**Results.** No empirical data collected. No experimental result claimed. Results reported are analytic, derived from equations: hop doses scale as A^k, asymptotic attenuation rate λ = −ln Ω, feedback loop returns pulse after Trec with area ratio Rrec, no ripple can arrive earlier than minimum-delay path distance. Curves in figures computed from model equations, labelled illustrations.

**Interpretation.** Ω is established mathematics (spectral radius criterion of linear stability, input-output analysis, branching processes). RET does NOT claim Ω as new law. Contribution is combination of counterfactual measurement, independently measured couplings, causality bound, pre-registered cross-domain test. If thresholds met, RET supplies shared quantitative vocabulary for propagation in tested domains. If not met, each threshold identifies which postulate fails and scope reduced accordingly.

**Conclusion.** RET presented as complete, testable framework with defined scope, defined measurements, defined failure conditions. Theory does NOT claim every later event is caused by earlier one.

**Keywords:** ripple effect, causality, propagation, feedback systems, dynamical systems, networks, temporal processes, cascading failure, spectral radius, falsifiability.

---

## 3. RESEARCH SIGNIFICANCE

**Scientific significance.** Converts informal ripple idea into measurable quantities: ripple field Δi(t), integrated dose Mi, Ripple Number Ω, arrival time Ti, recurrence ratio Rrec. Supplies causality bound + attribution rule that separate propagation from coincidence, prevents theory from describing any sequence retrospectively as ripple.

**Methodological significance.** All predictions computed from independently measured couplings BEFORE any ripple data recorded, so models carry zero fitted parameters in primary tests. Decisions use equivalence bounds with stated sample sizes. Design allows theory to fail clearly.

**Practical significance.** In three domains tested (electronic networks, surface waves, cascading failure in power grids) framework offers common way to estimate how far and how long disturbance persists, whether feedback loop will amplify or damp it. Same quantities support design choices such as setting coupling gain so Ω stays below 1.

**Limits of claim.** Restricted to systems meeting admissibility conditions §9.6. Social, historical, other systems whose couplings cannot be measured independently are OUTSIDE scope of v1.0.

---

## 4. HIGHLIGHTS

1. Ripple defined as counterfactual difference between disturbed system and baseline, measurable (Eq.3).
2. Total integrated effect M = (I − A)^-1 M(0). When Ω < 1 hop doses decay as Ω^k with attenuation length ℓ = −1/ln Ω (Eq.7, Eq.9).
3. No component can show ripple earlier than minimum-delay path distance dτ(s,i). Violation identifies hidden path or common cause (Eq.12).
4. Feedback loop returns pulse after Trec with area ratio Rrec, fixes number of detectable recurrences and persistence time (Eq.13, Eq.14).
5. Five-criterion Ripple Attribution Criterion converts "B followed A" into testable attribution, sensitivity + specificity lower bounds 0.90 required (Eq.17).
6. Unifying claim is cross-domain parity law with slope ψ = 1 within ±0.15 for three different systems (Eq.23). Failure in domain removes that domain from scope.
7. Scope conditions, sample sizes, thresholds, stopping rules fixed before data collection. No empirical data claimed.

---

## 5. VISUAL EMBLEM — FIGURE 1

**Figure 1. Ripple Effect Theory emblem.** Central filled circle = disturbed source s. Each ring = one hop of propagation; ring line weight decreases to represent attenuation, dashed outer rings = hops whose doses fall toward detection limit. Small circles = components, short lines = couplings. Expression Ω = ρ(A) at base = Ripple Number that governs whether rings shrink or grow.

---

## 6. FORMULA BASIS CHART — FIGURES 2-4

**Figure 2. Panel A (Eq.1-9).** Model definition, linear delayed response, integrated dose, attenuation.
**Figure 3. Panel B (Eq.10-18).** Amplification, delay and causality bound, loop recurrence, persistence, threshold cascade, attribution, detection thresholds.
**Figure 4. Panel C (Eq.19-25).** Continuous-medium attenuation; stochastic, time-varying, layered extensions; parity law; equivalence rule; sample-size rule.

Full word-accurate charts in `paper/figures/`.

**Eq.1 Network equation:** dxi/dt = fi(xi) + Σ_j Wij * gij(xj(t - τij)) + ui(t)
**Eq.2 Perturbation:** x(0) = x0 + ε * es
**Eq.3 Ripple field:** Δi(t) = xi_dist(t) - xi_base(t)
**Eq.4 Reachability:** Ris > 0 iff directed path s→i with nonzero couplings
**Eq.5 Linear delayed:** dΔi/dt = -κi Δi(t) + Σ_j Γij Δj(t - τij) + ε δ(t) [i=s]
**Eq.6 Hop gain:** Aij = Γij / κi
**Eq.7 Total dose:** M = A M + M(0)  →  M = (I - A)^-1 M(0), M(0) = (ε/κs) es
**Eq.8 Hop doses:** M(k) = A^k M(0), Mk = sum_i Mi(k)
**Eq.9 Attenuation:** Mk ≃ K0 Ω^k, λ = -ln Ω, ℓ = 1/λ
**Eq.10 Amplification:** Gs = (sum_i Mi) / M(0)_s
**Eq.11 Minimum-delay path:** dτ(s,i) = min_{π in Ξ(s→i)} Σ_{(j→i) in π} τij
**Eq.12 Causality bound:** Ti ≥ dτ(s,i)
**Eq.13 Recurrence:** Trec = Σ_{Λ} (τij + 1/κi), Rrec = Π_{Λ} Aij
**Eq.14 Persistence:** P = Trec * ln(θM / Mfp) / ln(Rrec) for Rrec < 1
**Eq.15 Threshold activation:** yi(t) = H( Σ_j Wij yj / Σ_j Wij - φi )
**Eq.16 Threshold Ripple Number:** Ωφ = ρ(BNB), cascade iff Ωφ > 1
**Eq.17 Attribution:** RACi = Π_{m=1..5} qm,i
**Eq.18 Detection:** θ = 3σ0, θM = 3σM, detection needs mc=5 consecutive samples > θ
**Eq.19 Continuous media:** a(r) = a0 * (r0/r)^((d-1)/2) * exp[-η(r - r0)]
**Eq.20 Stochastic:** J C + C J^T + Q = 0, J = -diag(κ) + Γ
**Eq.21 Time-varying:** ΩL = ρ( A(L)...A(1) )^(1/L)
**Eq.22 Layered:** A = [[A11, A12],[A21, A22]], Ω = ρ(A)
**Eq.23 Parity:** ln Mobs = ψ ln Mpred + χ
**Eq.24 Equivalence:** Support iff 90% CI ψ ⊂ [0.85,1.15] AND 90% CI χ ⊂ [-0.10,+0.10]
**Eq.25 Sample size:** n ≥ ((z_{1-α/2}+z_{1-β}) * σplan / δeq)^2 → n ≥ 30.06 → n=32 used

---

## 7. SYMBOL AND SIGN CHART — TABLE 5 (FULL)

| Symbol | Definition | Unit |
| :--- | :--- | :--- |
| i, j | Component indices: i receiving, j sending | 1 |
| s | Source (disturbed) component | 1 |
| N | Number of components | count |
| k | Hop number: couplings traversed | count |
| m | Attribution criterion index 1-5 | 1 |
| v | Sample offset 0 to mc−1 | count |
| L | Number of time-ordered snapshots | count |
| Y | Number of interdependent layers | count |
| n | Independent trials per condition | count |
| xi(t) | State of component i at time t | [x] |
| x, x0 | State vector + baseline | [x] |
| xi_base, xi_dist | Baseline run / disturbed run | [x] |
| t | Time | s |
| ε | Perturbation magnitude | [x] |
| es | Unit vector 1 at source, 0 elsewhere | 1 |
| ui(t) | External input to i | [x]/s |
| Δi(t) | Ripple field: x_dist − x_base | [x] |
| fi | Intrinsic dynamics of i | [x]/s |
| gij | Coupling function j→i | [x]/s |
| Wij | Coupling weight j→i | 1 |
| τij | Transport delay j→i | s |
| κi | Relaxation rate, κi = −∂fi/∂xi at baseline | 1/s |
| Γij | Linearised coupling, Wij ∂gij/∂xj | 1/s |
| Γ | Matrix of Γij | 1/s |
| Aij | Hop gain, Aij = Γij/κi | 1 |
| A, \|A\| | Hop-gain matrix + absolute values | 1 |
| A(l) | Hop-gain matrix l-th snapshot | 1 |
| Aab | Block coupling layer b to a | 1 |
| I, 1 | Identity matrix + vector of ones | 1 |
| cg | Gain-scale factor multiplying every Aij | 1 |
| Mi | Integrated ripple dose, time integral of Δi | [x]·s |
| M, M(0) | Dose vector + source dose, M(0) = (ε/κs) es | [x]·s |
| M(k) | Dose from effects traversed exactly k couplings | [x]·s |
| Mk | Total hop-k dose, sum Mi(k) | [x]·s |
| Mfp | First-pass dose around loop | [x]·s |
| Mobs, Mpred | Observed dose + frozen predicted dose | [x]·s |
| K0 | Prefactor asymptotic hop-dose decay | [x]·s |
| Ris | Reachability index s→i | 1 |
| Ω | Ripple Number, Ω = ρ(A) | 1 |
| Ω0 | Ripple Number at cg=1; critical gain cg* = 1/Ω0 | 1 |
| ρ(·) | Spectral radius: largest absolute eigenvalue | 1 |
| λ | Attenuation rate per hop, λ = −ln Ω | 1 per hop |
| ℓ | Attenuation length, ℓ = 1/λ | hops |
| Gs | Ripple amplification factor for source s | 1 |
| dτ(s,i) | Minimum-delay path distance s→i | s |
| Ξ(s→i) | Set of directed paths s→i; π one path | — |
| Ti | Arrival time at i | s |
| θ | Amplitude threshold, θ = 3σ0 | [x] |
| θM | Dose threshold, θM = 3σM | [x]·s |
| σ0 | SD baseline noise of Δi | [x] |
| σM | SD baseline dose integral | [x]·s |
| h | Sampling period | s |
| mc | Consecutive samples must exceed θ, fixed 5 | count |
| Λ | Directed simple loop | — |
| Trec | Loop recurrence period | s |
| Rrec | Loop recurrence ratio | 1 |
| P | Persistence time: recurrences remain above θM | s |
| yi(t) | Activation state (0/1) | 1 |
| H(·) | Heaviside step: 1 if arg ≥0 else 0 | 1 |
| φi | Activation threshold, fraction total incoming weight | 1 |
| BNB | Non-backtracking matrix on edges that can trigger vulnerable component | 1 |
| Ωφ | Threshold-cascade Ripple Number, ρ(BNB) | 1 |
| S | Cascade size: fraction active at end | 1 |
| ν | Mean degree | 1 |
| b, pb | Degree b + fraction with degree b | 1 |
| a(r) | Wave amplitude at distance r | [x] |
| a0 | Amplitude at reference r0 | [x] |
| r, r0 | Distance + reference distance | m |
| d | Spatial dimension (1,2,3) | 1 |
| η | Spatial damping coefficient | 1/m |
| J | Jacobian, J = −diag(κ) + Γ | 1/s |
| C | Stationary covariance of ripple field | [x]² |
| Q | Noise intensity matrix | [x]²/s |
| ΩL | Ripple Number of L snapshots | 1 |
| RACi | Ripple Attribution Criterion (1 accept, 0 reject) | 1 |
| qm,i | Indicator criterion m met at i | 1 |
| RS | Spearman rank correlation | 1 |
| Se, Sp | Sensitivity + specificity of attribution | 1 |
| ψ, χ | Parity slope + offset, ln Mobs = ψ ln Mpred + χ | 1 |
| δeq | Half-width equivalence region | as quantity |
| CI90% | Two-sided 90% CI | as quantity |
| α, β | Type I 0.05 + Type II 0.10 | 1 |
| zp | Normal quantile at p | 1 |
| σplan | Planning SD per-trial estimate ψ (0.25) | 1 |

**Defined Terms — Table 6:** Ripple = downstream change satisfying all 5 RAC criteria Eq.17. Ripple field = Δi(t) Eq.3. Dose = time integral Mi. Hop = one coupling traversed. Ripple Number Ω=ρ(A). Baseline = same system without perturbation, sham trials or stated model. Sham trial = same trigger/timing/recording, perturbation source disconnected. Common cause = influence on several components without passing through couplings from source. Frozen prediction = model prediction written to time-stamped file + hashed before ripple data. Equivalence region = interval around predicted value inside which 90% CI must lie for support. Admissible system = meets A1-A5 §9.6.

---

## 8. VISUAL BLUEPRINTS — FIGURES 5-17

| Fig | Title |
| :--- | :--- |
| 5 | Core structure: disturbance ε at s, solid arrows directed couplings gain Γij delay τij, arranged by hop, dashed arrows feedback couplings creating loops (P5) |
| 6 | Hop-propagation operator: source dose M(0) × A once per hop, total dose sum, finite only when Ω<1 (Eq.8) |
| 7 | One coupling + one component: signal from j delayed τij, × Γij, + external input, relaxed κi. Nonlinear: threshold gate φi → activation yi |
| 8 | Hop dose vs hop for 4 Ω values, normalised by source. Ω<1 straight line log plot slope ln Ω. Ω=1 persists, Ω>1 grows. Computed Eq.8, 8-component example |
| 9 | Ripple field along feed-forward chain 5 components. Each hop + delay τ=1.0, ×0.7. Arrows = causality bound dτ(s,i) Eq.11. No curve may rise above θ before arrow. Doses nodes 0-4 = 1.00, 0.70, 0.49, 0.34, 0.24 × source = A^k |
| 10 | Directed ring 4 components + pulse recurrence. Pulse returns after Trec=4.80 with Rrec=0.74 = 0.240 per pass. Pass-to-pass ratios 0.2400, 0.2401, 0.2410 agree Rrec Eq.13 |
| 11 | Threshold activation + cascade size vs mean degree. Left: activates when active fraction neighbours reaches φi. Right: simulated cascade freq + mean size random graphs φ=0.18. Dotted 1.04 < ν < 5.74 where Ωφ>1 Eq.16 |
| 12 | Amplitude vs distance d=1,2,3. Geometric spreading (r0/r)^(d−1)/2 + exponential damping Eq.19. d=1 only damping A0e^−λr. Computed ηr0=0.1 |
| 13 | Decision flow RAC. Downstream change accepted only if all 5 criteria hold in sequence. Failure of any rejects (Eq.17) |
| 14 | Electronic coupled-node apparatus (E2+E5). Network under test (8 nodes) + physically separate reference (8 nodes) recorded together. Perturbations, randomisation, frozen predictions one computer. Common-cause injector reaches both, used only E5 |
| 15 | Radial tank + channel (E3). 8 probes radial tank different distances/azimuths. 6 probes channel. Sham raises source tip above water so probe signal only from frame vibration |
| 16 | Timing one trial + order within block. Every trial 3.0 s. Perturbation + sham share same trigger/recording. Order within block of 4 set by permuted-block random numbers |
| 17 | Acceptance region parity law. Domain supports only if 90% CI parity slope in [0.85,1.15] and offset in [−0.10,+0.10]. Design only, no data |

---

## 9. INTRODUCTION, SCOPE, HYPOTHESES

### 9.1 Context
Initial event does not end with immediate effect. Change in one component can influence others, which influence further components. Consequences may diminish, persist, amplify, reverse, or return to original. RET studies propagation as one problem with one set of measured quantities. Ripple in fluid, disturbance in electrical network, cascade of line outages in power grid can share mathematical structure without sharing same physics. RET requires each application states its own mechanism, components, measurements. Does NOT assume model working in one physical system explains social, biological, historical events.

### 9.2 Established knowledge — RET does NOT claim as new
Counterfactual causal effect + potential-outcomes [1,5]. Linear response, stability, delay differential dynamics [2,40]. Network structure, small-world + scale-free, dynamics on networks [3,4,28,29]. Growth/decay threshold by spectral radius: reproduction numbers epidemics [10,11,12], input-output economics [13,25], branching-process cascading failure [19]. Threshold cascades + percolation [14,15,16]. Geometric spreading + damping linear waves [24]. Temporal precedence not sufficient for causation; dose-response, specificity, control required [1,38].

### 9.3 Established vs Hypothesis — Table 7
| Topic | Established | RET Hypothesis |
| :--- | :--- | :--- |
| Linear response | Linear delayed network dose M=(I−A)^-1 M(0) [2,40] | Independently measured κi,Γij,τij predict observed doses parity ψ=1±0.15 |
| Growth/decay | Spectral radius decides growth/decay [10,11,13,40] | Ω single quantity governs hop-dose decay + critical gain in all tested domains |
| Timing | Effects cannot precede causes along finite-delay path | Bound Ti≥dτ(s,i) separates propagation from common causes in practice |
| Loops | Feedback loop gain <1 produces decaying recurrences | Trec + Rrec predict period + dose ratio within 5% and ±0.10 ln ratio |
| Cascades | Threshold cascades percolation-type [14,16] | Ωφ>1 predicts cascade window + generations in power-grid model |
| Attribution | Precedence alone ≠ causation [1,38] | Five-criterion RAC reaches Se + Sp lower bounds 0.90 |
| Unity | Each domain own validated models | Single parity law same slope+offset holds electronic, fluid, power-grid |

### 9.4 Related approaches — Table 8
Potential outcomes/graphical causal [1,5]: counterfactual contrast, no dynamic propagation model with timing+magnitude. Granger/transfer entropy/CCM [6,7,8]: predictive info flow, no dose from independent couplings. Nonlinear dynamics/chaos [2,9]: trajectory divergence, not spatial/network path. Network science [3,4,28,29]: structure, no attribution/parity. Epidemic thresholds [10,11,12]: domain-specific, no common attribution. Input-output [13,25]: aggregate data, no counterfactual lab control. Cascading failure [14-19]: domain-specific, no link to linear-response + waves. Wave propagation [24]: continuous media only. Early-warning/self-organised criticality [26,27]: proximity to transitions, not propagation of specific disturbance. Self-exciting/synchronising [20,22,23]: statistical/synchronisation stability, not dose prediction single disturbance. Contagion geometry/resilience [34,35]: few parameters, no attribution rule. Temporal networks [21]: structure, RET adds dose-based measure §11.

### 9.5 Knowledge gap
No framework combines four: (1) counterfactual measure, (2) prediction only from independently measured couplings, (3) causality bound as rejection test for hidden paths/common causes, (4) pre-registered test whether one parity law holds across physically different systems. RET supplies four + thresholds at which each fails.

### 9.6 Scope + Admissibility — Table 9
| Code | Condition | How checked |
| :--- | :--- | :--- |
| A1 | Bounded, components listed + measured individually | Component list + measurement channel per component in protocol |
| A2 | Baseline observable + noise estimable | Baseline window ≥0.2 s or 50 samples before every perturbation |
| A3 | Perturbation controllable size at chosen component, with sham | Perturbation generator with disconnect switch |
| A4 | Couplings κi,Γij,τij measurable independently of ripple under test | Identification runs completed + frozen before ripple trials |
| A5 | Predictions, thresholds, sample sizes fixed before collection | Hashed prediction file + registered protocol |
Version 1.0 also requires small perturbations: dose at 2× base perturbation within 10% of 2× dose at base (linearity check). Larger perturbations require threshold regime P6. Historical, social, economic events OUTSIDE scope: couplings cannot be measured independently under A4 and no sham under A3.

### 9.7 Research Questions + Hypotheses — Table 10
Primary Q: For admissible systems, can magnitude, timing, recurrence, persistence of downstream effects be predicted from independently measured couplings, and can propagation be distinguished from coincidence + common cause?
| ID | Statement | Postulates | Test |
| :--- | :--- | :--- | :--- |
| H0 null | Apparent downstream effects explained by background, shared causes, local dynamics, measurement error, chance | None | All |
| H1 | Controlled perturbation produces downstream changes exceeding sham at every component predicted to respond | P1,P2 | E2,E3 |
| H2 | Observed propagation predicted from independently measured connections | P2-P5,P8 | E2,E3,E4 |
| H3 | Network structure + feedback explain persistence + magnitude beyond initial event only | P3,P5 | E2 |
| H4 | RAC separates true ripples from common-cause + mimicked sequences | P7 | E5 |
| H5 | One parity law ψ=1 χ=0 holds across electronic, fluid, power-grid | P8 | E4 |
| H6 | Criterion Ωφ>1 predicts when threshold cascades possible | P6 | E1,E4 |

---

## 10. FORMAL MODEL — 8 POSTULATES

### Model Definition Eq.1-3
Bounded system N components. State xi(t) obeys network equation Eq.1. fi own dynamics. gij coupling j→i, weight Wij, delay τij, external ui(t). Perturbation ε at source s at time zero Eq.2: es = 1 at source, 0 elsewhere. Measured quantity ripple field Eq.3: Δi(t) = xi_dist − xi_base. Baseline obtained by sham trials: same trigger/recording, perturbation absent. Same system both conditions, shared background cancels in Δi(t) when acts equally. Component Δi(t) within detection threshold throughout = not reached.

### P1 Coupling-conditioned propagation Eq.4
Change at s can alter i only through directed path nonzero couplings s→i. If no path, ripple field zero within noise. Any change at i without path attributed to common cause or chance. Ris counts, positive weights, all paths up to N hops s→i. Positive exactly when i reachable from s. A defined P2. Test: disconnected reference component E2,E5: every component |Δi|≤θ throughout response window. Status: Need for coupling path ESTABLISHED. Hypothesis identified coupling graph complete enough in tested apparatus.

### P2 Linear delayed response + conserved dose Eq.5-7
Small perturbation, ripple field obeys linear delayed Eq.5. Integrated dose given exactly by hop-gain matrix A Eq.7. κi how fast i returns to rest. Γij how strongly ripple at j drives i. Hop gain Aij=Γij/κi = fraction dose of j that i receives. Mi total area under ripple curve i. M(0) dose source alone. Test: Dose from integrating Eq.5 over all time. Delays do not change integral, ripple returns to zero, so κiMi = Σ ΓijMj + source ε at i=s. Dividing κi gives M=AM+M(0) Eq.7. Every reachable component observed dose = frozen prediction, parity slope ψ in [0.85,1.15] (E2,E4). Status: Derivation exact for linear delayed system ESTABLISHED [2,40]. Hypothesis apparatus in linear regime for chosen ε and κi,Γij,τij identifiable accurately enough.

### P3 Ripple Number, attenuation, amplification Eq.8-10
Spectral radius Ω=ρ(A) decides fate. Ω<1 dose traversed k couplings decays as Ω^k, total finite. Ω=1 persists. Ω>1 grows until nonlinearity limits. M(k) dose passed exactly k couplings. Mk sum over components. Ω factor multiplied each further hop. Attenuation λ=−ln Ω same on log scale, ℓ=1/λ hops over which dose falls by e. Gs total dose / source dose. Test: Asymptotic decay Mk≃K0Ω^k for nonnegative primitive A by Perron-Frobenius [40]. If coupling graph no loop, A nilpotent, Ω=0, effect vanishes after ≤N−1 hops. Tests: critical gain cg*=1/Ω0 (E2) + dose ratio between passes of loop (E2,P5). Status: Mathematics ESTABLISHED [10,11,13,40]. Hypothesis Ω measured from independent identification predicts regime + decay of real apparatus.

### P4 Arrival time + causality bound Eq.11,12,18
Ripple cannot arrive at i earlier than minimum-delay path distance from source. Arrival = first time ripple field exceeds detection threshold for mc=5 consecutive samples. Predicted arrival by solving Eq.5 numerically with measured parameters. dτ(s,i) smallest sum transport delays along any path s→i. Ti detected arrival. θ=3× baseline noise σ0, θM=3× baseline σM dose integral. Independent Gaussian, 5 consecutive above θ gives false-alarm ~4×10^-15 per detection window. Correlated noise raises value, why sham always recorded. Test: ≤5% trials may show Ti<dτ(s,i), median |Ti−Tipred| ≤ larger of 10% prediction and 0.5 ms electronic (E2). Wave tank no probe may detect burst earlier than ri/cmax, cmax largest group speed measured in channel (E3). Early arrival signals hidden path or common cause. Status: Bound follows finite delay ESTABLISHED. Hypothesis practical discriminator against vibration, grounding, shared-input artefacts.

### P5 Feedback, recurrence, persistence Eq.13-14
Single directed loop returns pulse to origin after recurrence period = loop delay. Each pass multiplies dose by product hop gains around loop. Rrec<1 recurrences decay, persistence finite. Λ loop. Around loop each coupling contributes transport delay τij + delay 1/κi relaxation i. Rrec loop gain. Mfp dose first pass. P time until dose recurrence falls below θM. Test: Delay 1/κi exact mean delay (centroid) first-order relaxation, dose gain Aij exact by P2, formulas follow for loop only loop of network. Directed ring E2 measured period within 5% Trec, ln measured pass-to-pass dose ratio within ±0.10 ln Rrec. Status: Loop mathematics ESTABLISHED. Hypothesis apparatus follows within limits. Applies to topologies with exactly one directed loop; multi-loop NOT claimed v1.0.

### P6 Threshold cascades Eq.15-16
Component activates when active share incoming weight reaches threshold, global cascade possible iff threshold Ripple Number Ωφ>1. yi(t) 1 when active. H step 1 when active incoming weight reaches fraction φi total incoming weight. BNB built on directed edges j→i for which single active neighbour j can trigger i, forbids immediate backtracking. Random graph degree pb, mean ν, one threshold φ, Ωφ=Σ b(b−1)pb/ν, criterion Watts [14] with non-backtracking [16]. Test: E1 random graphs φ=0.18 cascade frequency ≥0.50 at every tested mean degree in [νlo+1.0, νhi−1.0] and ≤0.05 for ν≤νlo−0.5 and ν≥νhi+0.75, where νlo=1.04 νhi=5.74 roots Ωφ=1. E4 generation counts power-grid cascade model must follow parity. Status: Criterion ESTABLISHED random graphs [14,15,16]. Hypothesis use as Ripple Number within RET + application to power-grid cascade model.

### P7 Ripple Attribution Criterion Eq.17 — Table 11
Downstream change at i attributed to propagation from s iff all 5 criteria Table 11 met. Attribution score product 5 indicators =1 only when every criterion holds. qm,i 1 when criterion m met at i else 0. Criteria require in turn coupling path, correct timing, measurable dose, dose rises with perturbation size, absence under controls. Test: E5 lower 95% Clopper-Pearson bound [32] sensitivity ≥0.90 and specificity ≥0.90, each from 200 independent decision blocks. Status: Criteria motivated by counterfactual causal inference + Hill-type evidence [1,5,38]. Combination + numerical thresholds HYPOTHESES RET.
| Criterion | Condition | Operational rule |
| :--- | :--- | :--- |
| C1 Path | Directed coupling path s→i exists | Ris>0 using only couplings \|Γij\| >3× identification SE |
| C2 Timing | Arrival respects causality + prediction | Ti≥dτ(s,i) and \|Ti−Tipred\|≤max(10% Tipred, 0.5 ms) |
| C3 Magnitude | Ripple exceeds noise | Lower 95% bootstrap bound (dose perturbation − dose sham) exceeds θM |
| C4 Dose-response | Larger perturbations larger doses | Spearman RS≥0.8 between perturbation size + dose over 4 sizes [37] |
| C5 Controls | Sham + reference show no response | Sham dose at i + all doses reference ≤θM |

### P8 Cross-domain parity law Eq.23-24
Admissible systems different physical kinds, frozen predictions + observed doses obey one parity relation slope 1 offset 0 on ln scale. Tested separately each domain, supported in domain only if 90% CI slope in [0.85,1.15] and offset in [−0.10,+0.10]. Mobs observed response magnitude, defined each domain E4: dose networks, gated RMS amplitude waves, generation count cascades. Mpred predicted in advance from independently measured parameters. ψ=1 every factor change prediction appears same factor observation. χ=0 no systematic over/under. δeq half-width equivalence region. Test: E4 estimates ψ,χ for 3 domains. Unified law supported only if all 3 pass. If domain fails, law withdrawn for that domain, retained for those passing. Status: Central + unproven hypothesis RET. NOT established by existing literature.

### Worked Example — Table 12
Three-component system κi=2.0 s-1 all, source s=1, ε=1.0 [x]. Numbers computed from equations; NOT empirical.
| Quantity | Value |
| :--- | :--- |
| Hop-gain A rows 1-3 | Row1: 0,0.30,0.10. Row2: 0.40,0,0.20. Row3: 0.20,0.30,0 |
| Source dose M(0)=(ε/κ1)e1 | (0.500,0,0) [x]·s |
| Ripple Number Ω=ρ(A) | 0.498 (below 1, total finite) |
| Attenuation λ=−ln Ω + length ℓ | 0.697 per hop + 1.44 hops |
| Total dose M=(I−A)^-1 M(0) | (0.606,0.284,0.206) [x]·s |
| Amplification G1 | 2.19 |
| Hop totals Mk k=0-5 | 0.500,0.300,0.150,0.072,0.0372,0.0180 |
| Ratios Mk+1/Mk k=0-4 | 0.600,0.500,0.480,0.517,0.484 (approaching Ω=0.498) |

---

## 11. EXTENDED MECHANISMS

Only X1 + X2 used in experiments v1.0. X3 + X4 mathematical statements without claimed empirical support; using them in experiment requires new registered protocol.

**X1 Continuous media Eq.19.** In continuous medium dimension d, amplitude decreases with distance by geometric spreading + damping. a0 amplitude at r0. Factor (r0/r)^(d−1)/2 spreading energy over growing wavefront: 1 plane wave d=1, 1/√r circular d=2, 1/r spherical d=3. Factor exp[−η(r−r0)] damping η. d=1 reduces to exponential law original working draft. Test: E3 fitted spreading exponent (d−1)/2 must have 90% CI inside [0.40,0.60] radial tank and inside [−0.10,+0.10] channel. Status: ESTABLISHED linear damped waves [24]. Hypothesis use same parity format as networks.

**X2 Stochastic ripple Eq.20.** Components driven by white noise intensity Q, baseline fluctuation stationary covariance C solves matrix equation, detection threshold follows diagonal. J Jacobian linear system without delays. C covariance fluctuations around baseline, diagonal Cii variance σ0,i² noise at i. Holds for delays small vs 1/κi [39]. Test: E2 baseline SD predicted Eq.20, Q measured isolated components, must agree measured within 20% (secondary, reported without hypothesis claim). Status: Equation ESTABLISHED [39]. Use predicted noise for threshold setting methodological choice RET.

**X3 Time-varying couplings Eq.21.** If couplings change in L ordered steps, long-run growth factor per step = geometric-mean spectral radius product snapshots. A(l) hop-gain during l-th step, applied order l=1 to L. ΩL<1 dose decays over full cycle even if single snapshot Ω≥1. Test: NOT tested v1.0. Status: Mathematical based on temporal networks [21]; no empirical support claimed.

**X4 Interdependent layers Eq.22.** For Y coupled layers, e.g. power + communication, hop-gain block matrix, Ripple Number spectral radius. Aab block couples layer b to a. Cross-layer blocks allow disturbance move between layers. Interdependence can raise Ω above either layer alone [18]. Test: NOT tested v1.0. Status: Mathematical; no empirical support claimed.

---

## 12. EXPERIMENTAL PROGRAMME + FALSIFICATION

Every apparatus value, sample size, decision threshold fixed here, before data collected. Experiment gives one of two outcomes: supported or not supported. Experiment that cannot be completed under rules counts as not supported. Theory must state in advance what observation would refute it [33].

### 12.1 Common Rules — Table 13
Registration: Protocol registered public preregistration service (OSF) with date stamp before identification runs E2 begin. Frozen predictions: All predictions computed from independently measured parameters written to one file. SHA-256 hash recorded in registration before any ripple trial. Blinding: Trial files coded identifiers. Analyst does not know perturbation vs sham until analysis code frozen + hashed. Randomisation: Trial order permuted blocks. Random seed = first 8 hex digits of hash of frozen prediction file, converted to integer, recorded. Detection: θ=3σ0, θM=3σM, estimated baseline window each trial. Detection needs mc=5 consecutive samples above θ. Statistics: Percentile bootstrap 10,000 resamples; resampling unit trial. Equivalence uses 90% interval Eq.24. Proportions Clopper-Pearson [32]. Bootstrap Efron+Tibshirani [31], equivalence Schuirmann [30]. Multiplicity: Each primary outcome one pre-specified decision about one postulate. Framework-level claim requires all primary decisions pass, so no adjustment (intersection-union). Secondary reported 95% intervals, no hypothesis claim. Sample size: Eq.25 α=0.05 β=0.10 σplan=0.25 δeq=0.15 gives n≥30.06 so n=31. Design uses n=32 trials per condition to fit blocks of four. If observed SD per-trial estimate exceeds 0.25, experiment declared underpowered + counts not supported. Exclusions: Trial excluded only pre-specified quality flags: converter clipping, supply voltage outside ±5% nominal, temperature outside 23±2°C (electronic) or 20.0±0.5°C (tank), or logged operator event. Excluded trials replaced by new trials same block. If >10% trials in condition excluded, condition repeated once in full. Second failure counts not supported. Deviations: Every deviation logged date+reason + reported final report. Deviation from threshold or sample size makes affected experiment not supported. Order + gate: E1 first. If E1 not supported, E2-E5 not started until fault corrected + E1 repeated once. Order after E1: E2, E5, E3, then E4.

### 12.2 E1 Computational Verification — Table 14
Tests: Mathematical statements P2,P3,P6 as implemented in analysis code (H2 part, H6). Apparatus: Python 3 NumPy SciPy double precision one computer; versions + seeds recorded. Graph families: Erdős-Rényi, Watts-Strogatz (6 neighbours, rewiring 0.1) [28], Barabási-Albert (3 links per new node) [29], each N=200. Weights uniform (0,1), scaled Ω=0.5,0.7,0.9; κi=1, τij uniform 0.5-1.5. Procedure: (1) For 1,000 graphs per family+Ω, compute dose (I−A)^-1 M(0) + hop totals Mk k=0-40. (2) For 100 graphs per family+Ω, integrate Eq.5 RK4 step 0.005 to t=1,500 + integrate ripple field to Mi. (3) Simulate threshold Eq.15 φ=0.18 Erdős-Rényi N=10,000 mean ν 0.25-9.00 steps 0.25: 10 graphs per ν + 200 single-seed runs per graph. Run cascade if >5% active. Primary: All three checks met. Analysis Check1: every graph step2 largest relative difference integrated dose vs (I−A)^-1 M(0) over components dose >10^-6 M(0) ≤10^-3. Check2: every graph step1 primitive A slope ln Mk k=20-40 differs ln Ω ≤0.02. Check3: cascade frequency ≥0.50 at every tested ν in [2.04,4.74] and ≤0.05 for every tested ν ≤0.54 and ν ≥6.49, where 1.04+5.74 roots Ωφ=1. Falsification: Any check not met = computational form affected postulate not supported. Second reviewer audits code once + E1 repeated once. Two failures end support affected postulate. Alternatives excluded: Integration error (step halving same to 10^-4); coding fault (independent implementation second reviewer must reproduce Check1); finite-size (N=10,000 + 2,000 runs per ν). Ethics: No human/animal/hazardous. Illustration §8.7 used N=3,000 different seeds; generated while drafting, NOT part of E1.

### 12.3 E2 Electronic Coupled-Node Network — Table 15
Tests: P1-P5 + X2; H1,H2,H3. Apparatus: 16 node boards, each first-order op-amp stage R=2.00 kΩ (0.1%) C=100 nF (1%), nominal κ=5,000 s-1. Programmable coupling modules gain 0-1.5 steps ≤0.005 + buffered delay 1.0-50.0 ms steps 0.02 ms. Analogue crosspoint switch sets topology. AWG 16-bit supplies 0.500 V pulse width 50 μs at source. Simultaneous-sampling 16-bit converter records all 16 nodes at 50 kS/s (h=20 μs). Shielded enclosure 23±2°C linear ±12 V supply. 8 nodes network under test + 8 nodes reference with no coupling (Fig.14). Topologies: T1 directed ring 6 nodes delay 5.0 ms per coupling, Trec=6×(5.0+0.2)=31.2 ms, gains a=0.5,0.7,0.9 (Rrec=a^6=0.0156,0.1176,0.5314). T2 8-node Fig.14 couplings 1→2,2→3,3→4,4→5,5→1,5→6,6→7,7→8,8→4,2→5 delays 4,5,6,7,8,9,10,11,12,13 ms in order, so dτ(1,i) 4,9,15,17,26,36,47 ms nodes 2-8. Nominal gain 0.30 every coupling (nominal Ω0=0.389). T2 run at gain-scale cgΩ0=0.50,0.70,0.85,0.95,1.05,1.20,1.50, source node 1 both topologies. Procedure: (1) Identification: measure κi step response, Γij small-signal sinusoids 50 Hz 10 repeats, τij cross-correlation, every node+coupling. (2) Compute A,Ω0,dτ, all predictions incl. predicted arrival Eq.5, freeze. (3) Trials 3.0 s (Fig.16): 0.2 s baseline, perturbation/sham at 0.2 s, response window to 1.0 s, washout 2.0 s. Every condition 32 perturbation + 32 sham in permuted blocks of four. (4) Linearity series: cgΩ0=0.50 T2, 32 trials each perturbation sizes 0.5,1.0,1.5,2.0× base pulse. Primary: Parity slope ψ + offset χ Eq.23 over all pairs (condition,node) predicted dose ≥5θM, using subcritical: T1 three gains + T2 cgΩ0=0.50,0.70,0.85,0.95. Secondary: (a) H1 every node predicted dose ≥5θM lower 95% bound (dose perturbation−sham) exceeds θM. (b) Arrival times vs predictions + causality bound. (c) Recurrence period + pass-to-pass ratio T1, persistence at a=0.9. (d) Regime classification: each T2 level predicted late-to-peak ratio rend outside 0.35-0.65, share trials observed rend falls predicted side of 0.50. rend = |Δ1| at 0.9 s / peak. (e) H3 ratio RMSE ln dose full model vs initial-event-only model keeping only direct couplings source. (f) Linearity §9.6. (g) Baseline noise vs Eq.20. (h) Negative control: reference 90% interval dose difference perturbation−sham inside [−θM,+θM] all 8 nodes. Analysis: Dose time integral baseline-corrected response 0.2-1.0 s. ψ,χ OLS over (condition,node) pairs. Percentile bootstrap resamples trials within each cell, recomputes cell means, re-estimates ψ,χ. Model no fitted parameters. Falsification: H2 not supported if 90% ψ not inside [0.85,1.15] or 90% χ not inside [−0.10,+0.10]. H1 not supported if any must-respond node fails (a). P4 not supported if >5% trials Ti<dτ(1,i), or median absolute arrival error > larger of 10% prediction and 0.5 ms. P5 not supported if recurrence period differs Trec >5% or ln dose ratio differs ln Rrec >0.10. P3 not supported if regime concordance (d) <90% at any qualifying level. H3 not supported if upper 95% bound error ratio (e) ≥0.80. Failed negative control (h) voids session; repeated once, second failure H1 not supported. Alternatives excluded: Ground loops + shared-supply (reference + separate linear supply; crosstalk ≤−80 dB before every session); drift (identification repeated end each session, voided if any κi or Γij changed >2%); clipping (trial excluded); delay quantisation (delays measured, not assumed); temperature logged. Ethics: Low-voltage ±12 V. No human/animal. Standard electrical safety, lead-free solder.

### 12.4 E3 Fluid Surface-Wave Tank — Table 16
Tests: P1,P4 + X1; H1,H2. Apparatus: Acrylic tank 1.50×1.50 m 0.10 m walls, deionised water conductivity <5 μS/cm to 20.0±0.2 mm at 20.0±0.5°C, vibration-isolated table. Absorbing beach reflection ≤0.05 measured before first run. Electromagnetic shaker 4 mm stainless tip delivers tone burst 8 Hz, 3 cycles, Hann window, 0.50 mm peak at source. 8 capacitive wave probes resolution ≤10 μm sampled 1 kHz at r=0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45 m azimuths 45° apart. Channel 2.50×0.10 m plunger across width + 6 probes x=0.20,0.52,0.84,1.16,1.48,1.80 m (Fig.15). Procedure: (1) Calibrate every probe 5 static depth changes ±1 mm require linear fit R²≥0.999. (2) Skim surface + rest 10 min before each session; rest 120 s between runs. (3) Channel 32 perturbation + 32 sham runs estimate front speed successive probes; cmax = mean 32 estimates + 3 SD. (4) Radial tank 32 perturbation + 32 sham permuted blocks, probe-to-radius assignment rotated over 4 sessions of 8 runs so each probe visits 4 radii. Sham raises tip 5 mm above water identical drive. (5) Odd perturbation runs calibration half, even test half. Primary: Fitted spreading exponent n ln a = ln a0 − n ln(r/r0) − η(r−r0) radial tank (prediction n=0.5) + channel (prediction n=0). Secondary: (a) H1 each 8 radii lower 95% bound amplitude difference (perturbation−sham) exceeds θ. (b) Arrival times vs ri/cmax. (c) Damping η both geometries. (d) Parity data E4: n fixed 0.5 + η fitted calibration half, predicted amplitudes test half. Analysis: Amplitude ai RMS probe signal gate Ti to Ti+0.5 s, after subtraction mean sham amplitude. Ti follows Eq.12. Exponent + η fitted nonlinear least squares each bootstrap resample runs. Gate ends before first reflection returns. Falsification: Spreading law not supported if 90% n radial not inside [0.40,0.60], or 90% n channel not inside [−0.10,+0.10]. H1 not supported if any radius fails (a). P4 not supported if any probe detects burst before ri/cmax in >5% runs. Alternatives excluded: Reflections (beach+gating); frame vibration (sham+isolation); surface contamination (skimming+10-min rest; surface tension drop-weight before+after each session, voided if changes >5%); probe bias (rotation probes over radii); meniscus (probe calibration). Ethics: No human/animal. Water spill + electrical separation: shaker + probe electronics outside tank + GFCI.

### 12.5 E4 Cross-Domain Parity Test — Table 17
Tests: P8 + P6 (power-grid); H5,H6. Domains: S1 electronic E2. S2 wave tank E3 radial tank test half. S3 cascading-failure model IEEE 118-bus transmission test case (public data), solved AC power-flow solver (software+version recorded) with branching-process estimation generation counts [19]. Response M: S1 dose. S2 gated RMS amplitude. S3 number line trips Nk at cascade generation k. S3 procedure: Line rating =1.10× base-case apparent-power flow, minimum 30 MVA. Scenarios: each 186 lines initial outage, load scale 0.9,1.0,1.1,1.2, 5 random load-noise seeds (±5% per bus), giving 3,720 scenarios. Generation g+1 = lines loading exceeds 100% rating after generation g removed. Islands without generation dropped, islands with generation rebalanced proportional scaling. Power flow fails to converge = blackout that island. Scenarios odd index fixed random ordering (seed recorded) training set, others test set. Predictions: S1+S2 frozen predictions E2+E3. S3: Ω̂ = total trips generations 2+ / total generations 1+ in training set, prediction test set ln(N̄k/N̄1)=(k−1) ln Ω̂ k=1-6, N̄k mean over all test scenarios. Generations <30 trips total dropped. If <5% scenarios reach generation 3, tolerance changed once to 1.05. If shortfall remains, S3 declared non-informative + claim E4 restricted to two domains. Primary: Each domain parity slope ψ + offset χ Eq.23. Analysis: OLS pairs (ln Mpred, ln Mobs); percentile bootstrap 10,000 resamples trials (S1,S2) or scenarios (S3). Falsification: Domain supports parity if 90% ψ inside [0.85,1.15] and 90% χ inside [−0.10,+0.10]. Unified law H5 supported only if every informative domain supports. If one domain fails, law withdrawn for that domain + scope reduced to domains passing. H6 supported in power-grid only if S3 passes. Alternatives excluded: Circularity S3 (training/test disjoint); S2 (calibration/test halves disjoint); S1 (all parameters from identification runs); selective reporting (all three domains reported whatever outcome). Ethics: Uses E2+E3 data + public simulation data. No human.

### 12.6 E5 Attribution + Common-Cause Test — Table 18
Tests: P7; H4. Apparatus: Apparatus E2 with common-cause injector (band-limited Gaussian noise 0-2 kHz, 5 mV RMS) reaching all 16 nodes. Topology T2 cgΩ0=0.70 with reference. Target node 8 (dτ=47 ms), predicted dose ≥5θM. Conditions: A true ripple: perturbation node 1, couplings on. B common cause: injector delivers one pulse to all 16 nodes at once; node 1 not perturbed; couplings on. C mimic: all couplings zero; delayed copies predicted ripple each node injected at each node, delays dτ(1,i) + predicted amplitude, so sequence imitates propagation. E unreachable: perturbation node 1 couplings on; target node 9 in reference. Procedure: Decision block contains 4 perturbation trials 0.5,1.0,1.5,2.0× base pulse + 1 sham trial, random order. Identification runs (as E2) precede every group 20 blocks, couplings in state of condition under test. Five criteria Table 11 evaluated each block on target node. Design 200 blocks A, 70 B, 70 C, 60 E, so 400 blocks + 2,000 trials total. Truth labels: A blocks true ripples. B,C,E not ripples by construction. Primary: Sensitivity Se = share A blocks RAC=1 + specificity Sp = share B,C,E blocks RAC=0. Secondary: Specificity separately B,C,E Clopper-Pearson; first criterion rejecting each non-ripple block. Analysis: All criteria rules fixed Table 11. Analyst blind to condition each block until analysis code frozen. Intervals Se,Sp Clopper-Pearson [32]. Example 195 correct in 200 gives lower 95% bound 0.948, 190 gives 0.917. Falsification: H4 not supported if lower 95% bound Se <0.90 or lower 95% bound Sp <0.90. Alternatives excluded: Drift (identification repeated per 20 blocks); analyst expectation (blinding); order effects (random order within blocks + random order blocks across conditions); non-independence (each block separate decision unit, trials not shared between blocks). Ethics: As E2.

### 12.7 Summary Thresholds — Table 19
| Hypothesis | Experiment | Metric | Supported if | If not supported |
| :--- | :--- | :--- | :--- | :--- |
| H1 | E2,E3 | Lower 95% bound response difference must-respond | Above θM (E2) or θ (E3) every such component | Propagation withdrawn for that apparatus |
| H2 | E2,E3,E4 | ψ,χ parity | 90% ψ [0.85,1.15] + χ [−0.10,+0.10] | Prediction from independent couplings withdrawn for that domain |
| H3 | E2 | Upper 95% bound error ratio full vs initial-only | Below 0.80 | Structure+feedback withdrawn |
| H4 | E5 | Lower 95% bounds Se,Sp | Both ≥0.90 | Attribution withdrawn |
| H5 | E4 | ψ,χ every informative domain | All domains pass | Parity withdrawn failing domains |
| H6 | E1,E4 | Cascade freq pattern; S3 parity | E1 Check3 met + S3 passes | Threshold criterion withdrawn |
| P4 | E2,E3 | Share arrivals earlier than bound | ≤5% | Causality-bound withdrawn |
| P5 | E2 | Recurrence period error + ln dose-ratio error | Within 5% + ±0.10 | Loop law withdrawn |
| P3 | E2 | Regime concordance | ≥90% each qualifying level | Ripple Number withdrawn for apparatus |
| Spreading X1 | E3 | Exponent n | Radial [0.40,0.60]; channel [−0.10,+0.10] | Continuous-medium extension withdrawn |

### 12.8 Execution Order — Table 20
1 Register protocol; freeze analysis code | Registration receipt + code hash recorded
2 Run E1 | All three checks met
3 E2 identification + prediction freeze | Hash prediction file recorded
4 E2 trials | Quality rules §12.1 met
5 E5 trials | Apparatus identification stable within 2%
6 E3 trials | Probe calibration R²≥0.999; beach reflection ≤0.05
7 E4 analysis | E2,E3,S3 data complete
8 Final report | All experiments reported whatever outcome

---

## 13. COMPARISON + NOVELTY

### 13.1 Comparison — Table 21
| Factor | Standard models | RET position |
| :--- | :--- | :--- |
| Scope | Each framework tied to one domain | Bounded to admissible systems §9.6 + tested 3 domains |
| Causal attribution | Association or identification rules [1,5,6,7] | Five-criterion rule + causality bound + numerical thresholds |
| Magnitude | Domain-specific response functions | Dose from independently measured couplings, M=(I−A)^-1 M(0) |
| Time | Lags estimated from data | Arrival bounded by dτ + predicted from measured delays |
| Feedback | Stability analysis | Recurrence period + ratio as measurable predictions |
| Nonlinearity | Threshold models [14,36] | Threshold Ripple Number Ωφ within same formalism |
| Cross-domain claim | Usually not tested | Parity law equivalence thresholds 3 domains |
| Falsifiability | Varies | Every postulate numerical failure condition §12.7 |

### 13.2 Statement on Ω + Originality
Ripple Number Ω = spectral radius gain matrix. Same mathematical object as reproduction number next-generation matrix [11], Leontief inverse condition [13], mean offspring branching process [19], linear stability criterion [2]. RET does NOT claim Ω as new quantity. What manuscript proposes as new is combination of counterfactual ripple field, dose-based prediction from independently measured couplings, causality bound as rejection test, five-criterion attribution rule, pre-registered parity test across domains. Claim of novelty depends on literature search below.

### 13.3 Novelty Verification Protocol — Table 22
Databases: Scopus, Web of Science, Google Scholar, arXiv, IEEE Xplore, APS journals. Window: 1 Jan 1900 to date of search. Search strings: (1) ("ripple effect" OR "propagation of disturbances") AND ("causal attribution" OR counterfactual) AND (network OR "dynamical system"). (2) ("spectral radius" OR "reproduction number") AND cascade AND ("cross-domain" OR "universal"). (3) ("perturbation propagation") AND (parity OR "equivalence test" OR preregistered). Inclusion: Peer-reviewed articles, books, preprints containing at least one of four elements knowledge gap §9.5. Decision: If one source contains all four elements, claim novelty for combination withdrawn + manuscript retitled as synthesis of established methods. If no source contains all four, claim kept + numbers records screened/included reported. Status: Protocol fixed. Search NOT executed in this version. Until executed + recorded, novelty of combination is claim, NOT finding.

---

## 14. RESULTS

No empirical data collected. No experiment §12 run. Every cell Table 23 states no observed value exists. No result, confirmation, support claimed.
| Experiment | Primary outcome | Observed value | Interpretation |
| :--- | :--- | :--- | :--- |
| E1 | Three computational checks | No data; no observed value | None; checks not run |
| E2 | Parity ψ,χ; secondary (a)-(h) | No data | None; apparatus not run |
| E3 | Spreading exponent n radial + channel | No data | None; tank not run |
| E4 | Parity slope+offset each 3 domains | No data | None; no domain analysed |
| E5 | Sensitivity + specificity attribution | No data | None; no block recorded |

### 14.1 Analytic Results Derived
(1) Dose linear delayed network M=(I−A)^-1 M(0) because relaxation + delay conserve area pulse §10.3. (2) Nonnegative primitive A total hop dose scales Ω^k, so λ=−ln Ω §10.4. (3) Worked example Table 12 gives Ω=0.498 G1=2.19. (4) Single directed loop recurrence period sum delays + dose ratio product gains, model-computed ring Fig.10 reproduces Rrec=0.2401 to four digits. (5) Random graphs φ=0.18 criterion Ωφ>1 holds 1.04<ν<5.74.

---

## 15. DISCUSSION, LIMITATIONS, PLANNED VERSIONS

### 15.1 Interpretation
RET states disturbance of bounded system can be followed through couplings with small set measured quantities. Framework gives ripple definition that can fail: downstream change is ripple only if coupling path exists, timing respects causality bound, exceeds noise, grows with perturbation size, absent under control. Sequence not meeting criteria NOT described as ripple. Theory therefore does NOT state every later event caused by earlier one. Strongest claim parity law P8. If holds, same few quantities (A,Ω,dτ,Trec) describe electronic network, surface wave, power-grid cascade with same prediction error structure. If holds only some domains, result more modest + still useful: RET applies in domains passing.

### 15.2 Consequences — Table 24 Decision Matrix
| Outcome | Consequence v1.0 |
| :--- | :--- |
| E1 not supported | Computational forms affected postulates not supported; E2-E5 do not proceed until fault corrected §12.1 |
| E2+E3 supported, E4 supported all 3 domains | Parity law supported tested systems. v2.0 reports result + extends scope only by new registered protocol |
| E2+E3 supported, E4 supported 2 domains | Parity withdrawn failing domain, retained two passing |
| E2 or E3 not supported | Prediction from independent couplings withdrawn for that apparatus, failing postulate named by thresholds §12.7 |
| E5 not supported | Attribution withdrawn. P1-P6 remain testable without it |
| All not supported | RET v1.0 rejected as predictive framework. Null H0 retained |

### 15.3 Limitations — Table 25
| Limitation | Handling |
| :--- | :--- |
| Broad theory can become too general to falsify, almost any sequence described afterwards as ripple | Predictions+thresholds frozen before testing; attribution rejects sequences without coupling path, correct timing, control checks; scope limited A1-A5 |
| Postulates linear while real systems nonlinear | Linearity check §9.6 limits perturbation size; threshold regime covered P6; larger nonlinearities out of scope |
| Couplings can change during measurement | Identification repeated end each session, sessions changes >2% voided; time-varying covered mathematically X3 but not claimed |
| Multi-loop topologies not covered by recurrence law | P5 claimed only topologies exactly one directed loop |
| S3 power-grid test depends on modelling choices rating + island handling | All choices fixed §12.5 before run, S3 allowed declared non-informative by stated rule |
| Mathematical models candidate formalisations of concept in original working draft, not equations recorded by author | Labelled as formalisations, only tests §12 can make them part of supported theory |
| No data exist | All results labelled not collected; derived statements labelled analytic |
| Equations, figures, numerical illustrations prepared with AI assistance | Author must check independently, qualified reviewer should verify derivations before submission |

### 15.4 Domains — Table 26
| Domain | Status v1.0 | Basis |
| :--- | :--- | :--- |
| Electronic networks | In scope; tested E2+E5 | A1-A5 met by apparatus |
| Surface waves thin water layer | In scope; tested E3 | Continuous medium measurable damping X1 |
| Cascading failure power-grid model | In scope as simulation; tested E4 S3 | Public test case + fixed rules |
| Ecological systems | Outside scope | Couplings cannot yet be measured independently A4 + sham not available |
| Social, economic, historical | Outside scope | A3+A4 not met; no claim made |

### 15.5 Planned Versions — Table 27
| Version | Content | Condition |
| :--- | :--- | :--- |
| 1.0 | This manuscript: complete theory + protocol | Released |
| 1.1 | Adds executed novelty search §13.3 + decision | Search executed + recorded |
| 2.0 | Reports results E1-E5 vs thresholds §12.7, whatever they are | All experiments completed under protocol |
| 2.x | Any extension scope (e.g. ecological or time-varying couplings) with new registered protocol | New protocol registered before collection |

---

## 16. CONCLUSION

RET presented as complete, bounded, testable framework for studying how disturbances propagate through interconnected systems. Defines ripple as counterfactual difference, predicts dose, timing, recurrence, persistence from independently measured couplings, gives five-criterion rule separating propagation from coincidence + common cause. Specifies five experiments with fixed sample sizes + numerical thresholds. Scientific value depends on outcome. If parity law holds in three physically different systems, theory supplies shared quantitative description of propagation. If fails, thresholds show which postulate fails + scope reduced. In both cases theory does NOT claim every subsequent event caused by earlier one.

---

## 17. ETHICS, TRANSPARENCY, INTEGRITY — Table 28
| Item | Statement |
| :--- | :--- |
| Ethics approval | Not applicable. Experiments use electronic circuits, water, public simulation data. No human, animals, personal data. Study adding human/social data requires ethics approval before collection |
| Funding | No external funding declared. Earth Angel Ventures research owner |
| Competing interests | Author affiliated Earth Angel Ventures, research owner. No other competing interest declared. Author confirms at signature |
| Author contributions | Angelica Pangan: conceptualisation, original theoretical proposal, supervision of manuscript |
| Use of AI tools | Claude (Anthropic) used under direction of author to formalise theory, draft text, typeset equations, compute illustrative curves, generate figures. Author responsible for content. Equations + derivations must be checked independently before submission |
| Data availability | No data exist. After collection, raw data, frozen predictions, hash record deposited open repository before final report |
| Code availability | No analysis code registered yet. Illustration scripts NOT part of any result. Analysis code frozen, hashed, deposited with registration |
| Protocol registration | Planned §12.1 before E2 identification runs |
| Safety | Low-voltage electronics + water tank only. No hazardous materials, biological agents, radiation |
| Reference verification | References prepared from established literature, NOT matched to live database in this version. §18 lists verification status |

---

## 18. REFERENCES — ALL 40, VERIFICATION REQUIRED

[1] Pearl (2009) Causality [2] Strogatz (2015) Nonlinear Dynamics and Chaos [3] Newman (2010) Networks [4] Newman (2003) Structure/function complex networks SIAM Review 45(2)167-256 [5] Rubin (1974) Estimating causal effects J Educ Psych 66(5)688-701 [6] Granger (1969) Econometrica 37(3)424-438 [7] Schreiber (2000) Measuring info transfer PRL 85(2)461-464 [8] Sugihara et al (2012) Detecting causality Science 338:496-500 [9] Lorenz (1963) J Atmos Sci 20(2)130-141 [10] Kermack+McKendrick (1927) Proc Roy Soc A 115:700-721 [11] Diekmann et al (1990) J Math Biol 28:365-382 [12] Pastor-Satorras+Vespignani (2001) PRL 86:3200-3203 [13] Leontief (1936) Rev Econ Stat 18(3)105-125 [14] Watts (2002) PNAS 99(9)5766-5771 [15] Gleeson+Cahalane (2007) PRE 75:056103 [16] Karrer et al (2014) PRL 113:208702 [17] Motter+Lai (2002) PRE 66:065102 [18] Buldyrev et al (2010) Nature 464:1025-1028 [19] Dobson et al (2007) Chaos 17:026103 [20] Hawkes (1971) Biometrika 58:83-90 [21] Holme+Saramäki (2012) Phys Rep 519:97-125 [22] Pecora+Carroll (1998) PRL 80:2109-2112 [23] Arenas et al (2008) Phys Rep 469:93-153 [24] Whitham (1974) Linear and Nonlinear Waves [25] Acemoglu et al (2012) Econometrica 80:1977-2016 [26] Scheffer et al (2009) Nature 461:53-59 [27] Bak et al (1987) PRL 59:381-384 [28] Watts+Strogatz (1998) Nature 393:440-442 [29] Barabási+Albert (1999) Science 286:509-512 [30] Schuirmann (1987) J Pharmacokinet Biopharm 15:657-680 [31] Efron+Tibshirani (1993) Intro to Bootstrap [32] Clopper+Pearson (1934) Biometrika 26:404-413 [33] Popper (1959) Logic of Scientific Discovery [34] Brockmann+Helbing (2013) Science 342:1337-1342 [35] Gao et al (2016) Nature 530:307-312 [36] Granovetter (1978) Am J Sociol 83:1420-1443 [37] Spearman (1904) Am J Psych 15:72-101 [38] Hill (1965) Proc Roy Soc Med 58:295-300 [39] Gardiner (2009) Stochastic Methods 4th ed [40] Horn+Johnson (2013) Matrix Analysis 2nd ed.
**Status for ALL 40:** Not independently verified in this version; check against publisher record before submission. The three works cited in original working draft are items 1,2,3. They support established methods for causality, nonlinear dynamics, network propagation and do NOT establish RET as new law.

---

## 19. FINAL DECLARATION

This manuscript presents Ripple Effect Theory as original theoretical proposal with complete + pre-specified experimental programme. No empirical data collected. No experimental result claimed. Established mathematical methods cited as established. Novelty of combination depends on literature search §13.3, NOT executed in this version.
Author: Angelica Pangan, Earth Angel Ventures, Philippines.
Signature: ______________________________ Date: ______________________

**Earth Angel Ventures Research Standard:** The standard is not how extraordinary a claim sounds, but how reliably the evidence supports it and how well others can examine, challenge, reproduce, and build upon the work.

## More Files
- [COMPANY.md](COMPANY.md) | [RESEARCHER.md](RESEARCHER.md) | [LEGAL-ETHICS.md](LEGAL-ETHICS.md) | [CONTACT.md](CONTACT.md)
- [CONTRIBUTING.md](CONTRIBUTING.md) | [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) | [SECURITY.md](SECURITY.md)
- [FUNDING.md](FUNDING.md) | [ROADMAP.md](ROADMAP.md) | [FAQ.md](FAQ.md) | [GLOSSARY.md](GLOSSARY.md) | [PRESS-KIT.md](PRESS-KIT.md)
- [CITATION.cff](CITATION.cff) | [CHANGELOG.md](CHANGELOG.md)
- [Protocols](protocols/) | [Figures](paper/figures/README.md) | [Data](data/README.md) | [Analysis](analysis/README.md)

## Protocols
- [E1 Computational Verification](protocols/E1-computational-verification.md)
- [E2 Electronic Coupled-Node Network](protocols/E2-electronic-network.md)
- [E3 Fluid Surface-Wave Tank](protocols/E3-wave-tank.md)
- [E4 Cross-Domain Parity Test](protocols/E4-cross-domain-parity.md)
- [E5 Attribution and Common-Cause Test](protocols/E5-attribution-common-cause.md)

## Figures
- [Figure-01 Emblem](paper/figures/Figure-01-Emblem.md) | [Figure-02 Formula Panel A](paper/figures/Figure-02-Formula-Panel-A.md) | [Figure-03 Formula Panel B](paper/figures/Figure-03-Formula-Panel-B.md) | [Figure-04 Formula Panel C](paper/figures/Figure-04-Formula-Panel-C.md) | [Figure-05 Core Structure](paper/figures/Figure-05-Core-Structure.md)
- [Figure-06 Hop Operator](paper/figures/Figure-06-Hop-Operator.md) | [Figure-07 Coupling Gate](paper/figures/Figure-07-Coupling-Gate.md) | [Figure-08 Attenuation Regimes](paper/figures/Figure-08-Attenuation-Regimes.md) | [Figure-09 Delay Causality](paper/figures/Figure-09-Delay-Causality.md) | [Figure-10 Feedback Loop](paper/figures/Figure-10-Feedback-Loop.md)
- [Figure-11 Threshold Cascade](paper/figures/Figure-11-Threshold-Cascade.md) | [Figure-12 Continuous Media](paper/figures/Figure-12-Continuous-Media.md) | [Figure-13 Attribution Flow](paper/figures/Figure-13-Attribution-Flow.md) | [Figure-14 Electronic Architecture](paper/figures/Figure-14-Electronic-Architecture.md) | [Figure-15 Wave Tank](paper/figures/Figure-15-Wave-Tank.md)
- [Figure-16 Trial Timing](paper/figures/Figure-16-Trial-Timing.md) | [Figure-17 Parity Acceptance](paper/figures/Figure-17-Parity-Acceptance.md)

# ret-ripple-effect-theory
Ripple Effect Theory: A Framework for Propagating Change Across Time and Interconnected Systems - Hypothesis + Protocol. A ripple is a counterfactual difference that survives path, timing, dose, dose-response, and sham. No data collected yet.
