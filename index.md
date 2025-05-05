---
layout: default
title: "ESP32-S3 Uno DevBoard"
---

{{ page.title }}
================

<i>Explore new possibilities with ESP32-S3 UNO Development Board.</i>

<img src="assets/ESP32-Uno-assembled.jpg">

![ESP32-S3 Arduino Uno](assets/ESP32-Uno-assembled.jpg)

<a href="schematic.md"><b>Schematic Link 1</b></a>

[Schematic Link 2](schematic.md)

<a href="{{% link schematic.md %}}">Schematic Link 3</a>

<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a>
    </li>
  {% endfor %}
</ul>
