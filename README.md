# ESP32-S3 Arduino Uno

_ESP32-S3 Module embeded on Arduino Uno board_

![ESP32-S3 Arduino Uno](https://github.com/alexandrebobkov/ESP32-S3_Arduino-Uno/blob/main/assets/ESP32-Uno-Board-v2.png)

![ESP32-S3 Arduino Uno](https://github.com/alexandrebobkov/ESP32-S3_Arduino-Uno/blob/main/assets/ESP32-Uno-assembled.jpg)

## I2C Pins

The schematic excerpt provided below illustrates the wiring configuration for the __SDA__ and __SCL__ lines. Specifically, the __SDA__ line is connected to _GPIO 8_, while the __SCL__ line is connected to _GPIO 9_ on the ESP32-S3 module.

![ESP32-S3 Module Pinouts](assets/ESP32-Uno-Board-Module-Pinout.png)

The image of PCB board below shows the physical location of SDA and SCL terminals.
![ESP32-S3 DevBoard Pinouts](assets/ESP32-Uno-Board-GPIO.png)



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



