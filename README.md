
# EpsonProjector v2 (incomplete, refer to v1)
## What's this?
I am very certain that I am the first person ever to crack the Epson Projector's WiFi Network passwords and possibly the digital names for the remote control buttons, please read the following to understand.

### It's NOT just ONE password
Every Epson Projector that supports replacing the physical remote control with a remote control inside the Epson iProjection app, archieves communication via a publicly visible, but password-protected WiFi Network. Although the projector does not directly give you the wifi password in clear text, it does provide you with a qr code which you can scan with the iProjection app. The iProjection app then proceeds to decode the wifi password of the projector and join the wifi network, (without ever showing you the password of course).

Unfortunately iOS does not reveal WiFi passwords you have already entered, up until the 12th September of 2022 (the release of iOS 16), which reveals all of the wifi passwords that you have entered or that were shared with you.

Luckily for us, I had physical access to multiple Epson Projectors on which I could log into their Remote Controls and put together a list of WiFi names and passwords! It was only a question of comprehending the link between the Projectors name and the unique wifi passwords.

Fast-forwarding a few months: I have understood most of the logic of the passwords (and have included a very little of it in the repository), and also conducted a few successful tests with them.

## Requirements
All of them **might be** be pre-installed, please check before attempting to install.
- PyPi `requests` module (`pip install requests`)
- Linux `nmcli` command (`apt install nmcli`)

## Limitations
I have only confirmed the project to be working with projector IDs that start with EBE and have a -EE in them. This should cover most Epson projector models, but I might add support for other ones in the future, feel free to fork if you know what you're doing.
This project is also built on **Linux**, feel free to fork.

## Usage Guide
### control.py
The control.py script utilizes scripts from the /src/scripts folder, to simulate sequences of physical key-presses. The "language" is not standard and is only invented for this project. The following is a list of all valid commands.

**Comments**
*Syntax*

    # <comment>

*Example*

    # This is a valid comment, you can only comment a whole line.
    key power 1 # This is not a valid comment, and will raise an error.

**Key Press**
*Syntax*

    key <name> <repeat>

*Example*

    # This presses the "Volume Up" button five times
    key volume_up 5

|**Key (\<name\>)**|**Function**|
|---------|---------------|
|`power`|The Power Button. (*Some models require you to press the button twice, to confirm turning it off.*)|
|`hdmi1`|Switch the input to the first HDMI port.|
|`hdmi2`|Switch the input to the second HDMI port.|
|`computer1`|Switch the input to the first VGA port.|
|`computer2`|Switch the input to the second VGA port.|
|`video`|Switch the input to the RCA (Composite Video) ports.|
|`usb_display`|*SOURCE 51* (I do not know the difference between `usb` and `usb_display`, but the software uses 2 different IDs for them.)|
|`usb`|*SOURCE 52* (refer to `usb_display`)|
|`lan`|Switch the input to LAN video.|
|`screen_mirroring`|Switch the input to wirelessly transmitted video (e. g. iProjection)|
|`source_search`|Makes the projector search through every source above to find a signal.|
|`av_mute`|Button to toggle muting audio and video at the same time.|
|`freeze`|Button to freeze/unfreeze the current frame.|
|`volume_down`|Lower the volume one step down (*Most models go up to 15 or 20 levels*).|
|`volume_up`|Raise the volume one step up.|
|`ok`|Press the OK button.|
|`left`|Press the <- button.|
|`up`|Press the /\ button.|
|`right`|Press the -> button.|
|`down`|Press the \/ button.|

**Sleep**
*Syntax*

    sleep <milliseconds>

*Example*

    # This stops the script for 1.5 seconds
    sleep 1500

**Settings (not implemented)**
*Syntax*

    set <key> <value>

*Example*

    # This is not implemented yet.

### finder.py
The finder.py script can be ran to scan for Epson Projectors with their WiFi enabled and dump their SSIDs into the *list.txt* file. You might need to modify the `name_regex` and `ssid_position` variables based on your configuration (**but please don't touch them if everything is working as expected**).

#### name_regex
If your projector networks are being ignored, create a new regex for the names or manually enter them into the *list.txt* file.

#### ssid_position
If your scanned SSIDs do not match with the networks in your area and have names like 3F or 1A, your get an OutOfRange error, you should try modifying the ssid_position number until realistic network names appear.
If you want to dive in even deeper, you could just run the `nmcli -t dev wifi` command in your terminal and split the lines at `:` and count up to the position that the SSID is in. If you cannot get this problem solved, open an Issue.

### generate_key.py
Attempts to generate WiFi passwords for every projector from *list.txt*, outputs the results and writes it to *passwords.txt*.
