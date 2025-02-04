## My excercise files while learning PyQt6

### About
This repository contains all the examples I created on-the fly while learning PyQt6.

### Source:
Most of my learning is based on the resources from:
https://www.pythonguis.com/pyqt6-tutorial/

### TODO
To create full projects utilizing the skills and knowledge.,

**Idea 1:** 
Arduino ESP32 nano running UDP server and PyQt6 based GUI will trigger
changes in the system parameter to change physical parameters.

**Idea 2:**
MatrixEngine?

**Idea 3:**
Multi-lingual relay control board over UDP/ESP-NOW*/LoRa*

***NOTE:***

_ESP-NOW*_ - Need to talk to serially connected ESP32 first 
which will relay the message to remote Arduino ESP32 Nano
receiving message via ESP-NOW protocol

_LoRa*_   - We can directly talk to USB LoRa dongle or 
we can send/recevie via ESP32 over serial and it will
act as a bridge between remote LoRa relay board.

**Idea 4:**
Bluetooth controlled relay board and UI is in PyQt6.
For accessing BLE, we need BlueGiga v1.2 dongle or we can use BleuIO dongle using pygatt

**Idea 5:**
BNO085 or similar 9-DoF sensor data visualized through the PyQt6 based UI..,

**Idea 6:**
Complete tutorial project on using PyQt6 to create embedded system test bench., 

**Idea 7:**
PyQt6 based GUI tool to read the pdf file selected by the user and create mind-map of key concepts :O