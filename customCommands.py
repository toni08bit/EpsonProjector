import time
import connector as Connector


commands = {
    # Chains
    "TurnOff": (2,{"Power"}),
    "AV-Mute-Flicker": (6,{"AV-Mute"}),
    "Source-Flicker": (3,{"HDMI2","HDMI1"}),
    "MaxVolume": (15,{"VolumeUp"}),
    "MinVolume": (15,{"VolumeDown"}),
    # Singles
    "SourceSearch": (1,{"SourceSearch"}),
    "Freeze": (1,{"Freeze"}),
    "HDMI1": (1,{"HDMI1"}),
    "HDMI2": (1,{"HDMI2"}),
    "Computer1": (1,{"Computer1"}),
    "Computer2": (1,{"Computer2"}),
    "Video": (1,{"Video"}),
    "USB-Display": (1,{"USB-Display"}),
    "USB": (1,{"USB"}),
    "LAN": (1,{"LAN"}),
}


def toCommandArgs(commandString):
    return {
        Connector.keyList[commandString][0]: Connector.keyList[commandString][1]
    }

class options:
    def repeatWithDelay(arguments):
        loops = int(arguments[0])
        delay = int(arguments[1])
        commandParams = toCommandArgs(arguments[2])

        for loop in range(loops):
            time.sleep(delay)
            Connector.sendCommand(commandParams)

    def repeatFor():
        #

    def repeatX():
        #

    def simple():
        #