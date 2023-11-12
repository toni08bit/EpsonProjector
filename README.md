# EpsonProjector v2 (incomplete, refer to v1)

## What's this?
I am very certain that I am the first person ever to crack the Epson Projector's WiFi Network passwords and possibly the digital names for the remote control buttons, please read the following to understand.

### It's NOT just ONE password
Every Epson Projector that supports replacing the physical remote control with a remote control inside the Epson iProjection app, archieves communication via a publicly visible, but password-protected WiFi Network. Although the projector does not directly give you the wifi password in clear text, it does provide you with a qr code which you can scan with the iProjection app. The iProjection app then proceeds to decode the wifi password of the projector and join the wifi network, (without ever showing you the password of course).

Unfortunately iOS does not reveal WiFi passwords you have already entered, up until the 12th September of 2022 (the release of iOS 16), which reveals all of the wifi passwords that you have entered or that were shared with you.

Luckily for us, I had physical access to multiple Epson Projectors on which I could log into their Remote Controls and put together a list of WiFi names and passwords! It was only a question of comprehending the link between the Projectors name and the unique wifi passwords.

Fast-forwarding a few months: I have understood most of the logic of the passwords (and have included a very little of it in the repository), and also conducted a few successful tests with them.

## Requirements
All of them COULD be pre-installed, please check before attempting to install.
- PyPi "requests" module (pip install requests)
- Linux "nmcli" command (apt install nmcli)

## Limitations
I have only confirmed the project to be working with projector IDs that start with EBE and have a -EE in them. This should cover most Epson projector models, but I might add support for other ones in the future, feel free to fork if you know what you're doing.

## Usage Guide
TODO