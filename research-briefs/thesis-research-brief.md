# Morphology-Aware ECG Denoising Using Deep Neural Networks for Arrhythmia Detection

**Author:** Md. Fahim | **Institution:** Bangladesh University of Engineering and Technology (BUET)  
**Supervisor:** Dr. Md. Kamrul Hasan, Professor, Department of EEE, BUET | **Period:** July 2025 – June 2026  
**Degree:** B.Sc. in Electrical and Electronic Engineering (EEE 400: Thesis, June 2026)

<!-- Source: Thesis Title Page, Certification & Header (pages i-iv) -->

## Abstract
<!-- Source: Thesis Abstract (page xv / page 16) -->
Electrocardiogram (ECG) recordings in clinical and ambulatory environments are frequently corrupted by baseline wander, muscle artifacts, and electrode motion. These disturbances distort the characteristic morphology of critical waves (P-wave, QRS complex, T-wave), diminishing the accuracy of automated cardiac diagnosis. This thesis investigates deep neural network denoising to recover clean signals from noisy ECG recordings while preserving clinically crucial waveform morphology. Validated across controlled benchmark simulations and downstream clinical interpretation tasks, the framework demonstrates that morphology-preserving denoising substantially improves R-peak detectability and arrhythmia classification performance under severe ambulatory noise.

## Clinical Problem & Motivation
<!-- Source: Thesis Section 1.1–1.3 (pages 1–7) & Section 2.1–2.5 (pages 8–30) -->
Real-world ambulatory cardiac monitoring is plagued by non-stationary noise that heavily overlaps with the clinical frequency spectrum of ECG signals. Traditional linear filters and wavelet methods frequently over-smooth sharp QRS transitions and attenuate low-amplitude P-waves or ST-segments, leading to false diagnostic indicators. The primary challenge is removing high-amplitude interference while maintaining the fine temporal and spectral boundaries that cardiologists and automated diagnostic algorithms rely upon.

## Benchmark Datasets
<!-- Source: Thesis Section 3.10.1–3.10.5 (pages 69–72) & Section 4.1–4.4 (pages 75–85) -->
- **Clean ECG Sources:** MIT-BIH Arrhythmia Database (35,392 test segments) and QT Database (evaluating waveform generalization across diverse ST-T morphologies).
- **Calibrated Noise Source:** MIT-BIH Noise Stress Test Database (NSTDB) covering baseline wander (BW), muscle artifacts (MA), electrode motion (EM), and mixed noise across SNR levels (-6 dB to +18 dB).
- **Downstream Validation:** Icentia 11K single-lead ECG database (200-record subset, >1M evaluated beats) and Georgia 12-lead ECG dataset (Lead II subset across five diagnostic rhythm classes).

## Selected Experimental Findings
<!-- Source: Thesis Section 4.1–4.4, Tables 4.1–4.7, Figures 4.1–4.7 (pages 75–85) -->
- **Signal Reconstruction:** Achieved an average output SNR of 14.79 ± 6.20 dB (input SNR: 5.96 dB; +7.56 dB SNR improvement) and a low Percentage Root-Mean-Square Difference (PRD) of 22.18% on MIT-BIH test segments.
- **Morphology Preservation:** Attained a Waveform Distortion Index (WDI) of 16.12% on MIT-BIH and 27.15% on QTDB, significantly reducing waveform distortion compared to established autoencoder baselines (TCDAE: 37.84% and 54.17%).
- **Beat-Level R-Peak Recovery:** Recovered 193,524 previously missed cardiac beats on the Icentia 11K dataset, raising Pan-Tompkins R-peak detection recall from 69.98% to 87.77% and F1-score from 81.24% to 91.84%.
- **Downstream Arrhythmia Classification:** Improved classification accuracy from 92.6% to 94.1% and macro-F1 from 75.4% to 83.6% on Georgia ECG records, driven by a +31.47% F1 gain on minority Atrial Fibrillation / Flutter.

## Research Conclusion
<!-- Source: Thesis Chapter 5 (pages 87–88) -->
Morphology-aware ECG denoising serves as an effective pre-processing stage for automated cardiac monitoring systems. By prioritizing waveform geometry and clinical feature preservation over simple numerical smoothing, deep neural denoising enhances signal interpretability for portable, wearable, and telemedicine applications.
