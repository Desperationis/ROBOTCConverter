import os
from Converter import *

"""
    MainConverter.py

    Converts a RobotC file using main conversion.

    You should use this conversion if:
        File has task main
        Uses #pragma config to set up motors

    Main files are basically the file that runs the program and includes
    any external libraries.
"""
class MainConverter(Converter):
    def __init__(self, rawFileName, outputFileName):
        super().__init__(rawFileName, outputFileName)

    def Convert(self, includeStatements):
        if self.canConvert:
            self.ConvertImportStatements(includeStatements)
            self.ConvertPragmaStatements()
            self.ConvertMainFunction()
            self.ConvertRest()

    def ConvertImportStatements(self, includeStatements):
        self.RefreshRead()
        self.outputFile.write("#pragma once\n")
        for line in includeStatements:
            self.outputFile.write(line)
        self.outputFile.write("\n\n")

    def ConvertPragmaStatements(self):
        # Converts compiler-exclusive pragma statements into my own functions.

        pragmas = []

        # Search for pragmas
        self.RefreshRead()
        for line in self.rawFile.readlines():

            if line.find("#pragma") != -1:

                for i in range(10):
                    # strip garbage completely
                    line = line.replace("  ", " ")
                    line = line.replace("(", "")
                    line = line.replace(")", "")
                    line = line.strip()
                args = line.split(", ")

                if line.find("Motor") != -1:
                    args[0] = "Motor"
                    pragmas.append(args)

        # Write em down
        for args in pragmas:
            variableString = "MotorPort {0};\n"
            self.outputFile.write(variableString.format(args[2]))

        self.outputFile.write("void SetUp() {\n")
        for args in pragmas:
            isReversed = "false"
            if "reversed" in args:
                isReversed = "true"

            funcString = "\tconfig(\"{0}\", {1}, {2}, {3});\n"
            self.outputFile.write(funcString.format(args[2], args[2], args[1], isReversed))
        self.outputFile.write("}\n\n")

    def ConvertMainFunction(self):
        self.RefreshRead()
        for line in self.rawFile.readlines():
            if line.find("main()") != -1:
                self.outputFile.write("task programMain() {\n")
                break

            elif "task" in line or "void" in line or "int" in line or "bool" in line or "float" in line or "double" in line:
                self.outputFile.write(line)


    def ConvertRest(self):
        canWrite = False

        self.RefreshRead()
        for line in self.rawFile.readlines():
            if canWrite:
                self.outputFile.write(line)

            if line.find("main()") != -1:
                canWrite = True
