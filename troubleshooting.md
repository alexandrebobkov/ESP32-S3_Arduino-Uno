---
layout: default
title: "Troubleshooting Steps"
---

{{ page.title }}
================

# Cannot Flash Micropython

## Symptoms

### Thonny shows error while flashing Micropython using Windows
Possible causes:
  - Windows is blocking access to Espressif Serial device

### Device manager alternates visibility of DevBoard from connected to disconnected
Possible causes:
  - Strapping pins pull-up resistors or capacitors are incorrect

### Issues during uploading the firmware
Possible causes:
  - ESP32-S3 Module was not properly soldered; some pads have poor connection. Consider re-flowing/re-soldering
  - USB-C reciptacle was not properly soldered; some pads have poor connection. Consider re-flowing/re-soldering
