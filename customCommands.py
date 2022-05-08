import time
import connector as Connector


commands = {
    # Chains
    "TurnOff": (2,["Power"]),
    "AV-Mute-Flicker": (6,["AV-Mute"]),
    "Source-Flicker": (3,["HDMI2","HDMI1"]),
    "MaxVolume": (15,["VolumeUp"]),
    "MinVolume": (15,["VolumeDown"]),
    # Singles
    "SourceSearch": (1,["SourceSearch"]),
    "Freeze": (1,["Freeze"]),
    "HDMI1": (1,["HDMI1"]),
    "HDMI2": (1,["HDMI2"]),
    "Computer1": (1,["Computer1"]),
    "Computer2": (1,["Computer2"]),
    "Video": (1,["Video"]),
    "USB-Display": (1,["USB-Display"]),
    "USB": (1,["USB"]),
    "LAN": (1,["LAN"])
}


def sendCustomCommand(commandString):
    print("Preparing + Looping to send custom command to Connector... (3)")

    customCommand = commands[commandString]
    for loop in range(customCommand[0]):
        print("Interating through predefined repeat count... (3." + int(loop + 1) + ")")
        for command in customCommand[1]:
            print("FIRING COMMAND! Sending to Connector... (4)")
            response = Connector.sendCommand({
                Connector.keyList[command][0]: Connector.keyList[command][1]
            })
            print("RESPONSE RECEIVED! Connector brought back code " + str(response.status_code) + ".")

class options:
    def repeatWithDelay(arguments):
        print("Executing custom function... (2)")

        loops = int(arguments[1])
        delay = int(arguments[2])

        for loop in range(loops):
            print("Looping inside custom function... (2." + str(loop + 1) + ")")

            time.sleep(delay)
            sendCustomCommand(arguments[0])

    def repeatFor(arguments):
        print("Executing custom function... (2)")

        length = int(arguments[1])

        startTime = time.time()
        while (time.time() - startTime) <= length:
            print("Looping inside custom function... (2.?)")

            sendCustomCommand(arguments[0])

    def simple(arguments):
        print("Executing custom function... (2)")

        sendCustomCommand(arguments[0])

def consoleOptions():
    functionList = [method for method in dir(options) if method.startswith("__") is False]
    fireData = {}

    while not fireData["Function"]:
        print(">>> Function?")
        requestedFunction = input()
        if not (requestedFunction in functionList):
            print("ERROR: Couldn't find " + '"' + requestedFunction + '"' + "!")

    print(">>> Arguments?")
    requestedArguments = input()
    fireData["Arguments"] = requestedArguments.split()
    
    print("Packing and sending... (1)")
    startTime = time.time()
    options[fireData["Function"]](fireData["Arguments"])
    print("FUNCTION COMPLETED! Duration: " + str(time.time() - startTime) + "s.")