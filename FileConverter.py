from PythonFileLibrary.Reader import *
from PythonFileLibrary.HelperFunctions import *

"""
    FileConverter.py

    Converts a RobotC file into a .cpp file.
"""

class FileConverter(Reader):
    def __init__(self, fileName):
        super().__init__(fileName)

        self.convertedFile = [];

        try:
            self.Convert()
        except AssertionError as error:
            print(error)

    # Get lines that have '#pragma config' in them. File
    # can still be naviagted normally.
    def GetConfig(self):
        for line in self.CleanRead():
            if '#pragma' in line and 'config' in line:
                yield line.strip('\n')

        self.ResetReader()

    def ConvertPragma(self):

        arguments = []

        # Get config() arguments
        for pragma in self.GetConfig():
            pragma = RemoveElements(pragma, ['#pragma', '(', ')', 'config', ' '])
            args = pragma.split(',')
            arguments.append(args)


        convertedPragma = []
        # Step 1: Turn motor and sensor ports into variables.
        for arg in arguments:
            type = arg[0]
            name = arg[2]
            convertedPragma.append("%sPort %s;\n" % (type, name))

        #Step 2: Use Cortex::config() to configure the ports.
        convertedPragma.append("void SetUp() {\n")
        for arg in arguments:
            type = arg[0]
            name = arg[2]
            port = arg[1]

            if type == "Motor":

                reversed = arg[-1] == 'reversed'

                convertedPragma.append("\tCortex::config(\"%s\", %s, %s, %s);\n" % (name, name, port, reversed))
            else:
                convertedPragma.append("\tCortex::config(\"%s\", %s, %s);\n" % (name, name, port))

        convertedPragma.append('}\n')

        return convertedPragma


    def Convert(self):
        assert self.canParse, "FileConverter.py: Could not read \"%s\"" % (self.fileName)

        for i in self.ConvertPragma():
            print (i)
