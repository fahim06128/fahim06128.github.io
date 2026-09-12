---
layout: page
title: "Smart Prepaid Energy Meter with Recharging System"
description: "IoT-enabled digital energy metering and wireless prepaid billing architecture with automated relay disconnect."
img: assets/img/projects/smart-energy-meter/energy_meter_hardware.png
importance: 1
category: Embedded Systems & IoT
github: https://github.com/fahim06128/GSM-Based-Smart-Prepaid-Energy-Meter-with-Recharging-System
---

### Overview

An IoT-enabled digital energy metering and automated billing system designed to eliminate manual meter readings and automate electricity management. The device features continuous high-precision AC power monitoring, wireless SMS prepaid recharge authentication, and automated relay disconnection when credits expire.

### Key Technical Contributions

- **Power Sensing:** Interfaced ACS712 current sensors and precision voltage transformers with an Arduino microcontroller to compute true RMS real-time power and energy units.
- **Wireless Billing:** Integrated SIM800L GSM/GPRS module for automated two-way SMS communication: handling prepaid recharge token validation, balance alerts, and usage telemetry.
- **Automated Disconnect:** Programmed fail-safe automated relay cutoff logic, physically severing the power delivery circuit upon balance exhaustion and restoring power upon valid recharge.
- **LCD Interface:** Constructed a 16x2 I2C LCD interface providing transparent consumer readouts of remaining account balance, cumulative kWh units, and active load wattage.

### Tools & Technologies

- **Hardware & Firmware:** Arduino, SIM800L GSM, ACS712 Current Sensor, Voltage Transformer, Relay Module
- **Connectivity:** GSM/GPRS Cellular SMS Telemetry

