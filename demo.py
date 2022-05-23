print("Loading libraries...")
import time
import connector as Connector


commands = {
    "TurnOff": (2,["Power"]),
    "AV-Mute-Flicker": (2,["AV-Mute"]),
    "Source-Flicker": (2,["HDMI2","HDMI1"]),
    "MaxVolume": (15,["VolumeUp"]),
    "MinVolume": (15,["VolumeDown"])
}


def sendCustomCommand(commandString):
    print("Preparing + Looping to send custom command to Connector... (3)")

    if commandString in commands:
        print("Called custom command found... (3)")
        customCommand = commands[commandString]
    else:
        print("WARNING: Called command not seen as a custom command, sending raw... (3)")
        customCommand = (1,[commandString])

    for loop in range(customCommand[0]):
        print("Interating through predefined repeat count... (3." + str(loop + 1) + ")")
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

    print("----- FUNCTIONS -----")
    for functionName in functionList:
        print("- " + functionName)
    print("----- FUNCTIONS -----")

    while not "Function" in fireData.keys():
        print(">>> Function?")
        requestedFunction = input()
        if requestedFunction == "exit":
            quit()
        if not (requestedFunction in functionList):
            print("ERROR: Couldn't find " + '"' + requestedFunction + '"' + "!")
            continue
        fireData["Function"] = options.__dict__[requestedFunction]

    print(">>> Arguments?")
    requestedArguments = input()
    fireData["Arguments"] = requestedArguments.split()
    
    print("Packing and sending... (1)")
    startTime = time.time()
    fireData["Function"](fireData["Arguments"])
    print("FUNCTION COMPLETED! Duration: " + str(round((time.time() - startTime) * 100) / 100) + "s.")

consoleOptions()
