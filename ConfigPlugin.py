from PythonFileLibrary.HelperFunctions import *
from Plugin import *

"""
    ConfigPlugin.py

    A plugin responsible for configuring motors and sensors.
"""
class ConfigPlugin(Plugin):
    def __init__(self, reader):
        super().__init__(reader)

    # Get lines that have '#pragma config' in them. File
    # can still be navigated normally.
    def GetConfigLines(self):
        for line in self.reader.CleanRead():
            if '#pragma config' in line:
                yield line.strip('\n')

        self.reader.ResetReader()


    # Get the arguments passed into all '#pragma config()'s
    # as a list of lists.
    def GetArguments(self):
        arguments = []
        for pragma in self.GetConfigLines():
            pragma = RemoveElements(pragma, ['#pragma', '(', ')', 'config', ' '])
            args = pragma.split(',')
            arguments.append(args)

        return arguments


    def Convert(self):
        convertedFile = []

        # Step 1: Turn motor and sensor ports into variables.
        configArguments = self.GetArguments()
        for arguments in configArguments:
            type, name = arguments[0], arguments[2]

            # Naming scheme E.x.: "MotorPort leftMotor;"
            convertedFile.append("%sPort %s;\n" % (type, name))


        # Step 2: Use Cortex::config() to configure the ports.
        configFunctions = ""
        for arg in configArguments:
            type, port, name = arg[0], arg[1], arg[2]

            if type == "Motor":
                reversed = arg[-1] == 'reversed'
                configFunctions += "\tconfig(\"%s\", %s, %s, %s);\n" % (name, name, port, str(reversed).lower())
            else:
                configFunctions += "\tconfig(\"%s\", %s, %s);\n" % (name, name, port)

        # Step 3: Write it down onto the list.
        setUp = [
        "void SetUp() {\n"
        "%s" % (configFunctions),
        "};"
        ]
        convertedFile.extend(setUp)

        return convertedFile
