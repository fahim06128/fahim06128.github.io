# Weakly Supervised Temporal Action Localization for Non-Intrusive Load Monitoring

**Author:** Md. Fahim | **Institution:** Bangladesh University of Engineering and Technology (BUET)  
**Affiliation:** Department of Electrical and Electronic Engineering, BUET | **Period:** 2025 – Present  
**Status:** Ongoing Research / Active Investigation

<!-- Source: Verified research trajectory and project documentation -->

## Research Problem
<!-- Source: NILM formulation; CamAL paper Section I (arXiv:2506.05895) -->
Non-Intrusive Load Monitoring (NILM) involves disaggregating the total aggregate electrical power recorded by a single smart meter into individual appliance usage patterns, operation timestamps, and energy consumption profiles. As smart meters are deployed worldwide, NILM provides vital transparency for household demand response and grid efficiency. However, disaggregating overlapping appliance signatures from a single composite power measurement remains a difficult ill-posed inverse problem.

## Motivation & Scalability Bottlenecks
<!-- Source: CamAL paper Section I, Introduction & Related Work -->
State-of-the-art deep learning NILM frameworks predominantly rely on strongly supervised models that require high-frequency sub-metered power logs for each individual appliance during training. Collecting plug-level ground truth requires intrusive in-home sensor deployments, is prohibitively expensive, and cannot scale to millions of diverse households. Conversely, coarse household-level binary labels (indicating whether an appliance exists or operated during a billing/monitoring cycle) are readily accessible from surveys, metadata, or billing records without physical submetering.

## Current Research Direction
<!-- Source: Ongoing research plan and investigation focus -->
This research investigates the adaptation of Weakly Supervised Temporal Action Localization (WTAL) principles to continuous smart-meter energy series:
- **Temporal Event Localization:** Formulating appliance operation as temporal actions, learning to identify precise turn-on [t_on] and turn-off [t_off] boundaries from aggregate power profiles without submetered ground truth.
- **Class Activation Mapping (CAM):** Studying temporal attention heads and class activation maps over multi-scale sequence representations to generate appliance-specific activation signals.
- **Overlapping Load Disaggregation:** Developing training formulations capable of separating concurrent activations (e.g., inductive motor spikes coinciding with cyclic heating elements).

## Methodological Starting Point
<!-- Source: CamAL paper, Adrien Petralia et al., ICDE 2025 (arXiv:2506.05895) — Reference Baseline -->
- **Foundational Paper:** Adrien Petralia, Paul Boniol, Philippe Charpentier, and Themis Palpanas, *"Few Labels are all you need: A Weakly Supervised Framework for Appliance Localization in Smart-Meter Series"*, **IEEE International Conference on Data Engineering (ICDE 2025)**.
- **Methodological Context:** Petralia et al. established that merging deep sequence classifiers with class activation mapping enables appliance pattern localization using up to 5,200× fewer training labels than fully supervised baselines while maintaining high localization accuracy. This work serves as the primary literature foundation for extending WTAL to broader NILM disaggregation settings.

## Target Evaluation & Status
<!-- Source: Benchmark targets and ongoing investigation scope -->
- **Target Benchmark Datasets:** Open-access smart-meter collections including UK-DALE, REFIT, and IDEAL, focusing on high-consumption appliances (dishwashers, washing machines, heat pumps).
- **Current Status:** Formulation of temporal feature extraction networks and loss objectives under weak household supervision; experimental evaluation of localization thresholds against standard energy disaggregation metrics.
