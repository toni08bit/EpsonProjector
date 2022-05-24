# EpsonProjector

## What's this?
Took my time to explore the hacky firmware of Epson Projectors.
This module allows you to do different things with your projector (Confirmed working with projector model "EB-992f"), including:
- A full key list which covers keycodes for every button there is on the physical remote
- Easy functions to set elementary things, eg: Source or Power
- A little "demo" (demo.py) which covers those easy functions

This diagram might help you understand:

![Diagram](https://user-images.githubusercontent.com/95703244/169970116-f027b608-6bb5-4f73-ad5d-13e9ab33441a.png)


## Requirements
- No packages! This module is coded from scratch, by just using the "requests" (pre-installed) pip module to simulate a web session.
- Passwords and Usernames: Password configuration is located inside the "connector" module.
- Before running any commands: Enable and Connect to the Projectors WiFi or LAN.  
  You can enable WiFi inside the "Network" Settings Category.  
  I have NOT found out the default WiFi password yet! Although you can set it at the same location where you have enabled the WiFi.
