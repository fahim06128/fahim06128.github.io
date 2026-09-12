---
layout: page
title: "HIVE-R: Swarm Drone System for GPS-Denied Rescue"
description: "Autonomous swarm drone architecture for flood search-and-rescue in GPS-denied environments using Visual SLAM and edge YOLOv8."
img: assets/img/projects/hive-r/drone_platform.png
importance: 2
category: Robotics & Vision
---

### Overview

A bio-inspired autonomous swarm drone framework engineered for search-and-rescue operations in flood disasters and GPS-denied environments. Powered by an onboard Raspberry Pi 4 companion computer and Pixhawk flight controller, the drone performs visual odometry mapping and edge neural detection of stranded humans in degraded visibility.

### Key Technical Contributions

- **Flight & Processing Integration:** Interfaced Raspberry Pi 4 companion computer with Pixhawk flight controller via MAVLink for autonomous waypoint navigation and flight stabilization.
- **GPS-Denied Navigation:** Developed Visual Odometry and SLAM pipelines using monocular camera streams to build spatial feature maps and establish pseudo-GPS coordinate references.
- **Edge AI Target Detection:** Deployed a lightweight YOLOv8 Nano model on edge compute with fuzzy data augmentation to detect human victims under adverse weather and occlusions.
- **Telemetry Protocol:** Formulated a swarm telemetry protocol relaying georeferenced survivor coordinates back to Ground Control Stations for rapid emergency deployment.

### Tools & Technologies

- **Software:** Python, ROS, TensorFlow, YOLOv8 Nano, Visual SLAM, OpenCV
- **Hardware:** Raspberry Pi 4, Pixhawk Flight Controller, Swarm Drone Platform

