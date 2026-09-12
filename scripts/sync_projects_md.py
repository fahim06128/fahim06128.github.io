import os

projects = [
    {
        'file': '1_automated_object_transportation.md',
        'title': 'Automated Object Transportation System',
        'desc': 'Autonomous robotic pick-and-drop system using ESP32, overhead camera ArUco tracking, and YOLOv11-seg obstacle detection.',
        'img': 'assets/img/projects/automated-transport/overhead_workspace.png',
        'importance': 1,
        'category': 'Robotics & Vision',
        'content': """### Overview

An automated robotic pick-and-drop platform combining overhead computer vision and mobile edge robotics. The system tracks dynamic objects and robot coordinates via overhead camera feeds, executes instance segmentation on moving obstacles, and transmits optimized collision-free trajectories to an ESP32 robot in real time.

### Key Technical Contributions

- **Mobile Chassis & Gripper:** Fabricated a custom 3D-printed differential-drive mobile chassis with a servo-actuated precision gripper for target pick-and-drop manipulation.
- **Vision-Guided Localization:** Implemented ArUco marker tracking with homography transformation in OpenCV to maintain sub-centimeter overhead localization and continuous robot pose estimation.
- **Dynamic Obstacle Segmentation:** Integrated YOLOv11-seg instance segmentation to isolate moving obstacles and planned real-time optimal routes via the A* trajectory search algorithm.
- **Telemetry Protocol:** Engineered low-latency bi-directional Wi-Fi telemetry between the central processing PC and onboard ESP32 controller.

### Tools & Technologies

- **Software:** Python, OpenCV, YOLOv11-seg, A* Path Planning
- **Hardware:** ESP32 Microcontroller, Servo Gripper, 3D-Printed Chassis, Overhead Camera Setup
"""
    },
    {
        'file': '2_hive_r_swarm_drone.md',
        'title': 'HIVE-R: Swarm Drone System for GPS-Denied Rescue',
        'desc': 'Autonomous swarm drone architecture for flood search-and-rescue in GPS-denied environments using Visual SLAM and edge YOLOv8.',
        'img': 'assets/img/projects/hive-r/drone_platform.png',
        'importance': 2,
        'category': 'Robotics & Vision',
        'content': """### Overview

A bio-inspired autonomous swarm drone framework engineered for search-and-rescue operations in flood disasters and GPS-denied environments. Powered by an onboard Raspberry Pi 4 companion computer and Pixhawk flight controller, the drone performs visual odometry mapping and edge neural detection of stranded humans in degraded visibility.

### Key Technical Contributions

- **Flight & Processing Integration:** Interfaced Raspberry Pi 4 companion computer with Pixhawk flight controller via MAVLink for autonomous waypoint navigation and flight stabilization.
- **GPS-Denied Navigation:** Developed Visual Odometry and SLAM pipelines using monocular camera streams to build spatial feature maps and establish pseudo-GPS coordinate references.
- **Edge AI Target Detection:** Deployed a lightweight YOLOv8 Nano model on edge compute with fuzzy data augmentation to detect human victims under adverse weather and occlusions.
- **Telemetry Protocol:** Formulated a swarm telemetry protocol relaying georeferenced survivor coordinates back to Ground Control Stations for rapid emergency deployment.

### Tools & Technologies

- **Software:** Python, ROS, TensorFlow, YOLOv8 Nano, Visual SLAM, OpenCV
- **Hardware:** Raspberry Pi 4, Pixhawk Flight Controller, Swarm Drone Platform
"""
    },
    {
        'file': '3_smart_prepaid_energy_meter.md',
        'title': 'Smart Prepaid Energy Meter with Recharging System',
        'desc': 'IoT-enabled digital energy metering and wireless prepaid billing architecture with automated relay disconnect.',
        'img': 'assets/img/projects/smart-energy-meter/energy_meter_hardware.png',
        'importance': 1,
        'category': 'Embedded Systems & IoT',
        'content': """### Overview

An IoT-enabled digital energy metering and automated billing system designed to eliminate manual meter readings and automate electricity management. The device features continuous high-precision AC power monitoring, wireless SMS prepaid recharge authentication, and automated relay disconnection when credits expire.

### Key Technical Contributions

- **Power Sensing:** Interfaced ACS712 current sensors and precision voltage transformers with an Arduino microcontroller to compute true RMS real-time power and energy units.
- **Wireless Billing:** Integrated SIM800L GSM/GPRS module for automated two-way SMS communication: handling prepaid recharge token validation, balance alerts, and usage telemetry.
- **Automated Disconnect:** Programmed fail-safe automated relay cutoff logic, physically severing the power delivery circuit upon balance exhaustion and restoring power upon valid recharge.
- **LCD Interface:** Constructed a 16x2 I2C LCD interface providing transparent consumer readouts of remaining account balance, cumulative kWh units, and active load wattage.

### Tools & Technologies

- **Hardware & Firmware:** Arduino, SIM800L GSM, ACS712 Current Sensor, Voltage Transformer, Relay Module
- **Connectivity:** GSM/GPRS Cellular SMS Telemetry
"""
    },
    {
        'file': '4_camera_to_camera_style_transfer.md',
        'title': 'Camera-to-Camera Style Transfer',
        'desc': 'StarGAN v2 deep generative model for cross-camera sensor style transfer trained on 55,000+ image patches.',
        'img': 'assets/img/projects/camera-style-transfer/style_transfer_results.png',
        'importance': 1,
        'category': 'Deep Learning & Vision',
        'content': """### Overview

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
"""
    },
    {
        'file': '5_two_player_pong_cpld.md',
        'title': 'Two-Player Pong Game on CPLD',
        'desc': 'Hardware-synthesized real-time Pong game implemented in Verilog HDL on CPLD with custom FSMs and LED matrix output.',
        'img': 'assets/img/projects/pong-cpld/pong_cpld_setup.png',
        'importance': 1,
        'category': 'Digital Systems & Hardware',
        'content': """### Overview

A fully hardware-synthesized, real-time interactive two-player Pong video game implemented purely at the gate and register-transfer level in Verilog HDL. Deployed on an Altera MAX II CPLD development board, the system drives an 8x8 LED dot matrix display via high-speed row-column multiplexing with zero CPU or software overhead.

### Key Technical Contributions

- **RTL & Digital Logic:** Designed modular Verilog HDL architectures incorporating frequency clock dividers, ball velocity controllers, collision detection logic, and paddle position registers.
- **Finite State Machine:** Formulated a robust Finite State Machine (FSM) managing game phases: start/serve, active trajectory simulation, wall/paddle boundary reflection, score recording, and game over.
- **Display Multiplexing:** Implemented high-speed dynamic refresh multiplexing to concurrently drive the 8x8 LED dot matrix without flicker, rendering paddles, ball, and score.
- **Verification & Deployment:** Synthesized and verified the complete design in Intel Quartus II, mapping pin assignments to physical pushbuttons and dual seven-segment score displays.

### Tools & Technologies

- **Hardware:** Altera MAX II CPLD Development Board, 8x8 LED Dot Matrix, 7-Segment Displays, Pushbuttons
- **Design Tools:** Verilog HDL, Intel Quartus II
"""
    },
    {
        'file': '6_smart_walking_stick.md',
        'title': 'IoT-Based Smart Walking Stick for Visually Impaired',
        'desc': 'Assistive embedded mobility device with ultrasonic obstacle detection, moisture sensing, and GSM/GPS emergency dispatch.',
        'img': 'assets/img/projects/smart-walking-stick/walking_stick_prototype.png',
        'importance': 2,
        'category': 'Embedded Systems & IoT',
        'content': """### Overview

An assistive embedded mobility system designed to enhance navigation safety and situational awareness for the visually impaired and elderly. Featuring multi-zone ultrasonic obstacle detection, ground moisture sensing, real-time GPS tracking, and automatic SOS emergency dispatch over cellular networks.

### Key Technical Contributions

- **Obstacle Detection:** Deployed multi-range ultrasonic sensors to detect head-level and knee-level obstacles up to 3 meters away, providing proportional frequency audio-haptic feedback.
- **Moisture Sensing:** Integrated surface probe electrodes at the tip of the stick to detect standing water, puddles, and slippery terrain, triggering distinct tactile buzzer warnings.
- **Emergency Telemetry:** Incorporated NEO-6M GPS and SIM800L GSM modules with an emergency panic pushbutton, dispatching immediate emergency SMS alerts with live Google Maps coordinates.
- **Power Management:** Engineered an energy-efficient power regulation circuit supporting rechargeable lithium-ion battery operation with low-power sleep state transitions.

### Tools & Technologies

- **Hardware:** Microcontroller, HC-SR04 Ultrasonic Sensors, NEO-6M GPS, SIM800L GSM, Haptic Vibration Motors, Buzzer
- **Applications:** Assistive Robotics & Human-Machine Interfacing
"""
    },
    {
        'file': '7_duplex_lifi_communication.md',
        'title': 'Duplex Communication Using Li-Fi',
        'desc': 'Bidirectional optical wireless communication transceiver system using visible light for full-duplex analog and digital transmission.',
        'img': 'assets/img/projects/lifi-comm/lifi_transceiver_hardware.png',
        'importance': 2,
        'category': 'Digital Systems & Hardware',
        'content': """### Overview

A bidirectional optical wireless communication (Li-Fi) transceiver system utilizing visible light to simultaneously transmit and receive analog audio and digital telemetry. The design achieves full-duplex transmission over free space using optical isolation, eliminating electromagnetic interference common in RF channels.

### Key Technical Contributions

- **Transmitter Design:** Engineered optical transmitter driver circuits modulating high-luminosity LEDs with pre-amplified audio and sensor signals across the optical line-of-sight channel.
- **Receiver Architecture:** Constructed high-gain, low-noise photodetector receiver stages featuring optical bandpass filtering, transimpedance amplification, and active noise filtering.
- **Full-Duplex Isolation:** Established full-duplex simultaneous bi-directional communication channels using spatial alignment and distinct optical wavelength pairing to eliminate self-interference.
- **Signal Integrity Analysis:** Analyzed transmission fidelity and signal integrity using high-speed digital oscilloscopes, demonstrating clear waveform reproduction and high SNR under indoor ambient light.

### Tools & Technologies

- **Hardware:** High-Speed LEDs, Photodetectors, Transimpedance Amplifiers, Active Filter Circuits
- **Domains:** Optical Wireless Communications, Optoelectronics, Analog Circuit Design
"""
    }
]

for p in projects:
    file_path = os.path.join('_projects', p['file'])
    content = f"""---
layout: page
title: "{p['title']}"
description: "{p['desc']}"
img: {p['img']}
importance: {p['importance']}
category: {p['category']}
github: https://github.com/fahim06128
---

{p['content']}
"""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print('Updated all 7 _projects markdown files.')
