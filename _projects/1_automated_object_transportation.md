---
layout: page
title: "Automated Object Transportation System"
description: "Autonomous robotic pick-and-drop system using ESP32, overhead camera ArUco tracking, and YOLOv11-seg obstacle detection."
img: assets/img/projects/automated-transport/overhead_workspace.png
importance: 1
category: Robotics & Vision
---

### Overview

An automated robotic pick-and-drop platform combining overhead computer vision and mobile edge robotics. The system tracks dynamic objects and robot coordinates via overhead camera feeds, executes instance segmentation on moving obstacles, and transmits optimized collision-free trajectories to an ESP32 robot in real time.

### Key Technical Contributions

- **Mobile Chassis & Gripper:** Fabricated a custom 3D-printed differential-drive mobile chassis with a servo-actuated precision gripper for target pick-and-drop manipulation.
- **Vision-Guided Localization:** Implemented ArUco marker tracking with homography transformation in OpenCV to maintain sub-centimeter overhead localization and continuous robot pose estimation.
- **Dynamic Obstacle Segmentation:** Integrated YOLOv11-seg instance segmentation to isolate moving obstacles and planned real-time optimal routes via the A* trajectory search algorithm.
- **Telemetry Protocol:** Engineered low-latency bi-directional Wi-Fi telemetry between the central processing PC and onboard ESP32 controller.

### Tools & Technologies

- **Software:** Python, OpenCV, YOLOv11-seg, A* Path Planning
- **Hardware:** ESP32 Microcontroller, Servo Gripper, 3D-Printed Chassis, Overhead Camera Setup

