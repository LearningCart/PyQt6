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

**Idea 8:**
Create note taking application.
Base version: Basic note taking app., stores notes in sqlite database and allows for viewing it later on.,
Advanced version:
While studying we can store different types of notes, like screen recording,text, pictures

**Idea 9:**
Job application tracking application.., it keeps record of all the job applied by date with the description of the jobs.,

**Idea 10:**
Multi-schedule reminder like water, break, excercise, etc., which can be pushed to remote EPS32 based device., 
It runs every seconds and checks which reminders are due., kind of like time frame of video editor., 
walks the time frame and notify to remote device if reminder event occurs

**Idea 11:**
PyQt6 based GUI application that allow viewing multiple Raspberry Pi and ESP32 based streaming cameras., 
Allows to go back in time, and see footages., 

**Idea 12:**
PyQt6 based GUI application that takes pictures via USB camera when gesture is detected.
Gesture can be sensed and send via serial. We can use Wii Nunchuk or APDS 9960 or similar sensor., 
either connected directly via MCP2221, or connected to Arduino ESP32 nano/Raspbery pi pico 2W sending data over UDP.
