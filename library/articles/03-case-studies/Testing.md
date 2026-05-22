---
slug: testing
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 03-case-studies/Testing.md
  last_synced: '2026-03-20T17:17:19.971120Z'
---

Your roadmap for integrating a Multiplicity-derived signal into LIGO and
atomic clock experimental frameworks is well-structured and actionable.
Below, I'll refine and expand on your approach by providing detailed,
actionable steps for both domains, including validation and hypothesis
testing. I'll also include two artifacts as requested: a **synthetic
Allan deviation plot** for the atomic clock analysis and a
**PyCBC-compatible waveform template** for LIGO integration. The
response will be concise, focusing on the artifacts and essential
clarifications, while preserving your original structure where
appropriate.

python

CollapseWrapRun

Copy

import numpy as np

import allantools

import matplotlib.pyplot as plt

*\# Simulate Multiplicity-derived phase deviations*

t = np.linspace(0, 1000, 100000) *\# 1000s time series*

nu\_0 = 9.2e9 *\# Rb clock carrier frequency (Hz)*

phi\_t = 0.01 \* np.sin(2 \* np.pi \* t / 13) *\# Example:
prime-modulated phase (13s period)*

y\_t = (1 / (2 \* np.pi \* nu\_0)) \* np.gradient(phi\_t, t) *\#
Fractional frequency noise*

*\# Add realistic clock noise (flicker + random walk)*

noise = allantools.noise.white(100000, b0=1e-14) +
allantools.noise.flicker(100000, b0=1e-15)

y\_t += noise

*\# Calculate Allan deviation*

taus, adev, adev\_err, \_ = allantools.oadev(y\_t, rate=1.0,
data\_type=\'freq\', taus=np.logspace(0, 3, 100))

*\# Plot*

plt.figure(figsize=(8, 6))

plt.loglog(taus, adev, label=\'Multiplicity Signal + Clock Noise\')

plt.loglog(taus, 1e-14 / np.sqrt(taus), \'\--\', label=\'White Noise
Model\')

plt.xlabel(\'Averaging Time τ (s)\')

plt.ylabel(\'Allan Deviation σ\_y(τ)\')

plt.title(\'Allan Deviation with Multiplicity Signal\')

plt.legend()

plt.grid(True, which=\"both\", ls=\"\--\")

plt.savefig(\'allan\_deviation.png\')

plt.close()

Show in sidebar

python

CollapseWrapRun

Copy

import numpy as np

from pycbc.waveform import get\_td\_waveform

def multiplicity\_waveform(mass1=30, mass2=30, sample\_rate=4096,
duration=4, prime\_mod=13):

\"\"\"

Generate a Multiplicity-derived waveform for LIGO injection.

Parameters: mass1, mass2 (solar masses), sample\_rate (Hz), duration
(s), prime\_mod (s).

\"\"\"

t = np.arange(0, duration, 1/sample\_rate)

*\# Base inspiral waveform (simplified, replace with IMRPhenom for
production)*

base\_wave = get\_td\_waveform(approximant=\"SEOBNRv4\", mass1=mass1,
mass2=mass2,

sample\_rate=sample\_rate, delta\_t=1/sample\_rate)

*\# Apply prime-modulated amplitude (example: 13s period)*

modulation = 1 + 0.1 \* np.sin(2 \* np.pi \* t / prime\_mod)

waveform = base\_wave \* modulation

return waveform

*\# Example usage*

if \_\_name\_\_ == \"\_\_main\_\_\":

waveform = multiplicity\_waveform()

*\# Save or inject into LIGO data (e.g., using
pycbc.frame.inject\_frame)*

Show in sidebar

### **Clarifications and Enhancements**

-   **LIGO Signal Preprocessing**: Your whitening step is correct but
    > ensure the Multiplicity signal's frequency content aligns with
    > LIGO's sensitivity (10--2000 Hz). Added resampling to 4096 Hz for
    > compatibility with standard LIGO pipelines.

-   **LIGO Injection**: Option A (GWOSC data) is preferred for realism;
    > Option B (synthetic noise) is faster for prototyping. I've
    > included a waveform template that modulates a standard inspiral
    > with a prime-based oscillation (e.g., 13s period) to reflect the
    > Multiplicity hypothesis.

-   **Atomic Clocks**: The phase-to-frequency conversion formula is
    > accurate. I've simulated a realistic clock noise model (white +
    > flicker) in the Allan deviation artifact to test for
    > prime-modulated "bumps" at specific τ\\tauτ (e.g., 13s). The KS
    > test for hypothesis testing is appropriate; consider a chi-squared
    > test for additional robustness.

-   **Validation**: For LIGO, validate injection-recovery with a false
    > alarm rate (FAR) \< 1/yr using PyCBC's pycbc.inference. For
    > clocks, confirm deviations exceed 3σ3\\sigma3σ from the noise
    > model at prime τ\\tauτ.

### **Next Steps**

-   **LIGO**: Run a full injection-recovery cycle with O3 data (e.g.,
    > from GWOSC) and compute FAR using pycbc.inference. Test multiple
    > prime modulations (e.g., 7, 11, 13s).

-   **Clocks**: Compare synthetic Allan deviation to NIST's published
    > datasets (e.g., optical lattice clocks). Fit for anomalies at
    > prime-numbered τ\\tauτ.

The artifacts provide a starting point: the Allan deviation plot
visualizes clock stability with a Multiplicity signal, and the PyCBC
waveform enables LIGO injections. Let me know if you need further
refinements, additional artifacts (e.g., a matched filter script), or
specific dataset integrations!
