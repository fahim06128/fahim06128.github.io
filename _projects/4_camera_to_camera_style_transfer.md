---
layout: page
title: "Camera-to-Camera Style Transfer"
description: "StarGAN v2 deep generative model for cross-camera sensor style transfer trained on 55,000+ image patches."
img: assets/img/projects/camera-style-transfer/style_transfer_results.png
importance: 1
category: Deep Learning & Vision
github: https://github.com/fahim06128/Camera-to-Camera-Style-Transfer
---

### Overview

A deep generative framework exploring cross-domain image translation between distinct physical camera sensors using StarGAN v2. By isolating sensor-specific color science, lens vignetting, and noise signatures, the network synthesizes authentic cross-camera image representations without requiring paired multi-camera captures.

### Key Technical Contributions

- **Generative Architecture:** Implemented and trained a multi-domain StarGAN v2 GAN architecture utilizing generator, discriminator, and style encoder networks for camera sensor translation.
- **Data Engineering:** Engineered a high-throughput data pipeline preprocessing the IEEE SP Cup 2018 dataset into 55,000+ standardized 256x256 image patches across diverse sensor domains.
- **Latent Space Evaluation:** Analyzed latent space cluster separability using t-SNE embeddings, demonstrating tight style disentanglement and robust preservation of spatial content structure.
- **Loss Formulation:** Monitored multi-objective losses (adversarial, style reconstruction, style diversity, and cycle consistency) to prevent mode collapse and color artifacting.

### Tools & Technologies

- **Frameworks:** PyTorch, torchvision, NumPy, scikit-learn
- **Dataset:** IEEE SP Cup 2018 Dataset
- **Analysis:** t-SNE Embedding Analysis, Generator Loss Profiling

