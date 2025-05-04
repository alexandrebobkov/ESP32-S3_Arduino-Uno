# ESP32-S3 Arduino Uno

_ESP32-S3 Module embeded on Arduino Uno board_

![ESP32-S3 Arduino Uno](https://github.com/alexandrebobkov/ESP32-S3_Arduino-Uno/blob/main/assets/ESP32-Uno-Board-v2.png)


### Micropython LED Blinky Code
```code Python
import esp, esp32, time, os, _thread
from machine import Pin, SoftI2C, I2C

def status_led():
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
print("MCU Temperature: ", esp32.mcu_temperature(), "C")

led = Pin(45, Pin.OUT)
led.value(0)
_thread.start_new_thread(status_led, ())
```



