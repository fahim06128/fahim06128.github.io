---
layout: page
title: "Two-Player Pong Game on CPLD"
description: "Hardware-synthesized real-time Pong game implemented in Verilog HDL on CPLD with custom FSMs and LED matrix output."
img: assets/img/projects/pong-cpld/pong_cpld_setup.png
importance: 1
category: Digital Systems & Hardware
github: https://github.com/fahim06128/Two-Player-Pong-Game-on-CPLD
---

### Overview

A fully hardware-synthesized, real-time interactive two-player Pong video game implemented purely at the gate and register-transfer level in Verilog HDL. Deployed on an Altera MAX II CPLD development board, the system drives an 8x8 LED dot matrix display via high-speed row-column multiplexing with zero CPU or software overhead.

### Key Technical Contributions

- **RTL & Digital Logic:** Designed modular Verilog HDL architectures incorporating frequency clock dividers, ball velocity controllers, collision detection logic, and paddle position registers.
- **Finite State Machine:** Formulated a robust Finite State Machine (FSM) managing game phases: start/serve, active trajectory simulation, wall/paddle boundary reflection, score recording, and game over.
- **Display Multiplexing:** Implemented high-speed dynamic refresh multiplexing to concurrently drive the 8x8 LED dot matrix without flicker, rendering paddles, ball, and score.
- **Verification & Deployment:** Synthesized and verified the complete design in Intel Quartus II, mapping pin assignments to physical pushbuttons and dual seven-segment score displays.

### Tools & Technologies

- **Hardware:** Altera MAX II CPLD Development Board, 8x8 LED Dot Matrix, 7-Segment Displays, Pushbuttons
- **Design Tools:** Verilog HDL, Intel Quartus II

