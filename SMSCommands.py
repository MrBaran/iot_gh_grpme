import collections

class SMSCommand(object):
    command = None
    gh_function = None
    description = None
    result = None

    def __init__(self, command, gh_function, description, result):
        self.command = command
        self.gh_function = gh_function
        self.description = description
        self.result = result

class SMSCommands(collections.OrderedDict):
    """List of IoT Greenhouse SMS commands"""
    #commands = None

    def __init__(self):
        #self = collections.OrderedDict()
        cmd = SMSCommand("#help", "send_command_list()", "Lists valid IoT Greenhouse texting commands.",None)
        self[cmd.command] = cmd
        cmd = SMSCommand("#help-verbose","send_command_details()","Detailed help on using the IoT Greenhouse texting service.",None)
        self[cmd.command] = cmd
        cmd = SMSCommand("#temp","send_temperature()","Sends current temperature value.",None)
        self[cmd.command] = cmd
        cmd = SMSCommand("#t","send_temperature()","Sends current temperature value.",None)
        self[cmd.command] = cmd
        cmd = SMSCommand("#open","ghs.servo.move(1)","Opens greenhouse louvers.","Greenhouse is open.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#o","ghs.servo.move(1)","Opens greenhouse louvers.","Greenhouse is open.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#close","ghs.servo.move(0)","Closes greenhouse louvers.","Greenhouse is closed.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#c","ghs.servo.move(0)","Closes greenhouse louvers.","Greenhouse is closed.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#fan-on","ghs.fan.on()","Activates fan.","Fan is on.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#f+","ghs.fan.on()","Activates fan.","Fan is on.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#fan-off","ghs.fan.off()","Deactivates fan.","Fan is off.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#f-","ghs.fan.off()","Deactivates fan.","Fan is off.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#lamp-on","ghs.lamps.white.on()","Activates white LED lamp.","White LED lamp is on.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#l+","ghs.lamps.white.on()","Activates white LED lamp.","White LED lamp is on.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#lamp-off","ghs.lamps.white.off()","Deactivates white LED lamp.","White LED lamp is off.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#l-","ghs.lamps.white.off()","Deactivates white LED lamp.","White LED lamp is off.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#beep","ghs.buzzer.beep()","Activates buzzer.","Buzzer was beeped.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#b","ghs.buzzer.beep()","Activates buzzer.","Buzzer was beeped.")
        self[cmd.command] = cmd
        cmd = SMSCommand("#about",None,"Provides an overview of the IoT Greenhouse system.","The IoT Greenhouse is a learning system developed to teach the fundamentals of Python programming and Internet of Things (IoT). It removes barriers of existing IoT training solutions by abstracting both hardware and software components. Students interact with hardware without challenges that building prototype circuits create. Additionally students quickly create robust Python code to control the system using APIs provided by the  IoT Greenhouse Service software.")
        self[cmd.command] = cmd

def unit_test():
    cmds = SMSCommands()
    for key, value in cmds.items():
        print("%s\t\t%s" % (key, value.gh_function))

if __name__ == "__main__":
    unit_test()