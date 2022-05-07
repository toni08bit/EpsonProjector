import time
import requests
from requests.auth import HTTPDigestAuth


destination = {
    "Prefix": "http://",
    "Host": "192.168.88.1",
    "Port": "80",
    "Suffix": "/" 
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
    "VolumeUp": ("KEY","56")
}

getHeaders = {
    "Accept-Encoding": "gzip, deflate",
    "Accept": "application/json, text/plain",
    "Referer": destination["Prefix"] + destination["Host"] + "/cgi-bin/Remote/Basic_Control",
    "Connection": "keep-alive"
}


def sendCommand(commandParams):
    address = destination["Prefix"] + destination["Host"] + ":" + destination["Port"] + "/cgi-bin/Remote/directsend"
    response = requests.get(address,headers=getHeaders,params=commandParams,auth=HTTPDigestAuth("EPSONWEB","88888888"))
    return response

class luiCommands:
    def keyCommand():
        repeat = 1
        delay = 0
        commandString = ""

        try:
            print(">>> Repeat? (Number)")
            repeat = int(input())
            print(">>> Delay? (Number)")
            delay = int(input())
            print(">>> Raw Command? (String)")
            commandString = input()
        except:
            print("Could not read input. (Terminating...)")
            return
        
        try:
            if not keyList[commandString]:
                print("Key does not exist. (Terminating...)")
                return
            if delay > 0:
                print("Delaying... (" +  + ")")
                time.sleep(delay)
            for i in range(repeat + 1):
                print("Sending... (" + str(i) + ")")
                response = processingFunctions.sendCommand({
                    keyList[commandString][0]: keyList[commandString][1]
                })
                print("Delivered. (Code: " + '"' + str(response.status_code) + '")')
        except Exception as error:
            print("Could not send command. (Following...)")
            print(error)

luiCommands.keyCommand()
