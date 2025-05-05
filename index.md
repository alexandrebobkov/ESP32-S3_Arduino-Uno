---
layout: default
title: "ESP32-S3 Uno Development Board"
---

{{ page.title }}
================

<i>Discover new opportunities with the ESP32-S3 UNO Development Board.</i>
<p>Unlock a world of innovative possibilities with the ESP32-S3 UNO Development Board. This versatile platform empowers developers to create cutting-edge applications, leveraging its advanced features and robust performance. Whether you're working on IoT projects, embedded systems, or automation tasks, the ESP32-S3 UNO Development Board offers the flexibility, power and quick implementation needed to bring your ideas to life.</p>
<p>Explore its capabilities and push the boundaries of your creativity and technical expertise.</p>

<img src="assets/ESP32-Uno-assembled.jpg" width="35%"/>

[Schematic](schematic.md)

[Specs](specs.md)

## Compatibility with MicroPython

Integrating the ESP32-S3 UNO Development Board with MicroPython offers several compelling benefits:

1. Ease of Use
MicroPython simplifies the development process by allowing developers to write code in Python, a high-level, easy-to-read programming language. This reduces the learning curve for beginners and accelerates development for experienced programmers.

2. Rapid Prototyping
With MicroPython, developers can quickly prototype and test their ideas. The interactive REPL (Read-Eval-Print Loop) enables immediate feedback and debugging, making it easier to iterate and refine projects.

3. Extensive Libraries
MicroPython comes with a rich set of libraries that support various functionalities, including networking, sensor interfacing, and data processing. This extensive library support allows developers to leverage pre-built modules and focus on the unique aspects of their projects.

4. Cross-Platform Compatibility
MicroPython code can be easily ported across different hardware platforms that support MicroPython. This cross-platform compatibility ensures that projects developed on the ESP32-S3 UNO can be adapted to other MicroPython-compatible boards with minimal changes.

5. Community Support
The MicroPython community is active and growing, providing a wealth of resources, tutorials, and forums for troubleshooting and collaboration. This community support can be invaluable for both novice and experienced developers.

6. Efficient Resource Management
MicroPython is designed to run efficiently on microcontrollers, making it well-suited for resource-constrained environments. It allows developers to manage memory and processing power effectively, ensuring optimal performance of their applications.

7. Enhanced Connectivity
The ESP32-S3 UNO Development Board offers robust connectivity options, including Wi-Fi and Bluetooth. MicroPython's networking libraries make it straightforward to implement IoT applications, enabling seamless communication between devices.

8. Versatility
Combining the ESP32-S3 UNO with MicroPython opens up a wide range of applications, from simple sensor monitoring to complex automation systems. The versatility of this fusion allows developers to explore diverse project ideas and innovate freely.

9. Educational Value
MicroPython's simplicity and the ESP32-S3 UNO's capabilities make this combination an excellent educational tool. It provides a practical platform for learning programming, electronics, and IoT concepts, fostering a deeper understanding of technology.

10. Cost-Effective Development
Both the ESP32-S3 UNO Development Board and MicroPython are cost-effective solutions, making them accessible to hobbyists, educators, and professionals alike. This affordability encourages experimentation and innovation without significant financial investment.

## I2C Pins

The schematic excerpt provided below illustrates the wiring configuration for the __SDA__ and __SCL__ lines. Specifically, the __SDA__ line is connected to _GPIO 8_, while the __SCL__ line is connected to _GPIO 9_ on the ESP32-S3 module.

<img src="assets/ESP32-Uno-Board-Module-Pinout.png" width="50%"/>

The image of the PCB board below depicts the physical locations of the __SDA__ and __SCL__ terminals.
<img src="assets/ESP32-Uno-Board-GPIO.png" width="50%"/>

### Micropython LED Blinky Code

``` python
import esp, esp32, time, os, _thread
from machine import Pin, SoftI2C

# An infinite loop thread to blink LED
def status_led():
    # Blink pattern blink-blink-pause
    while True:
        led.value(1)
        time.sleep_ms(250)
        led.value(0)
        time.sleep_ms(250)
        led.value(1)
        time.sleep_ms(250)
        led.value(0)
        time.sleep_ms(750)

# Display information about ESP32S3 module
print(os.uname())
print("Flash size: ", esp.flash_size()/1024/1024, "Mb")
#rint("MCU Temperature: ", esp32.mcu_temperature(), "C")
print("MCU Temperature: {:4.1f} C".format(esp32.mcu_temperature()))

# Configure LED pin and start the blinky loop thread
led = Pin(45, Pin.OUT)
led.value(0)
_thread.start_new_thread(status_led, ())
```
