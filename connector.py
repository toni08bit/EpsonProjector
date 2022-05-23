import time
import requests
from requests.auth import HTTPDigestAuth


destination = {
    "Prefix": "http://",
    "Host": "192.168.88.1", # This might variate!
    "Port": "80",
    "Suffix": "/" 
}
credentials = {
    "Username": "EPSONWEB",
    "Password": "88888888" # Default is 8x "8" OR "admin" (!!!)
}

keyList = {
    # Sources
    "Power": ("KEY","3B"),
    "HDMI1": ("SOURCE","30"),
    "HDMI2": ("SOURCE","A0"),
    "Computer1": ("SOURCE","10"),
    "Computer2": ("SOURCE","20"),
    "Video": ("SOURCE","41"),
    "USB-Display": ("SOURCE","51"),
    "USB": ("SOURCE","52"),
    "LAN": ("SOURCE","53"),
    "ScreenMirroring": ("SOURCE","56"),
    # Keys
    "SourceSearch": ("KEY","67"),
    "AV-Mute": ("KEY","3E"),
    "Freeze": ("KEY","47"),
    "VolumeDown": ("KEY","57"),
    "VolumeUp": ("KEY","56"),
    "Ok": ("KEY","49"),
    "Left": ("KEY","5A"),
    "Up": ("KEY","58"),
    "Right": ("KEY","5B"),
    "Down": ("KEY","59")
}

getHeaders = {
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json, text/plain",
    "Referer": destination["Prefix"] + destination["Host"] + "/cgi-bin/Remote/Basic_Control",
    "Connection": "keep-alive"
}


def sendCommand(commandParams):
    address = destination["Prefix"] + destination["Host"] + ":" + destination["Port"] + "/cgi-bin/Remote/directsend"
    response = requests.get(address,headers=getHeaders,params=commandParams,auth=HTTPDigestAuth(credentials.get("Username"),credentials.get("Password")))
    return response
