import os
from Converter import *

"""
    MainConverter.py

    Converts the main file. (The file that runs the program)
"""
class MainConverter(Converter):
    def __init__(self, fileName, outputFileName):
        super().__init__(fileName, outputFileName)

    def Convert(self, includeStatements):
        if self.canConvert:
            self.ImportIncludeStatements(includeStatements)

            self.ConvertPragmaStatements()
            self.WriteDownFunctions()
            self.ConvertMainFunction()
            self.ConvertRest()

    # Converts compiler-specific pragma statements into my own functions from RobotCSimulator
    # https://github.com/Desperationis/RobotCSimulator
    def ConvertPragmaStatements(self):
        pragmas = []

        # Search for pragmas
        self.RefreshRead()
        currentLine = self.GetCurrentLine()
        while not self.ReachedEnd():

            if "pragma" in currentLine:
                currentLine = currentLine.strip("()\n\t")
                for i in range(10):
                    # Normalize long empty spaces.
                    currentLine = currentLine.replace("  ", " ")
                args = currentLine.split(", ")

                if "Motor" in currentLine:
                    args[0] = "Motor"
                    pragmas.append(args)

                if "Sensor" in currentLine:
                    args[0] = "Sensor"
                    pragmas.append(args)

            currentLine = self.GetNextLine()

        # Write down variables of ports.
        for args in pragmas:
            if args[0] == "Motor":
                variableString = "MotorPort {0};\n"
                self.outputFile.write(variableString.format(args[2]))
            elif args[0] == "Sensor":
                variableString = "SensorPort {0};\n"
                self.outputFile.write(variableString.format(args[2]))

        # Write down SetUp() function.
        self.outputFile.write("void SetUp() {\n")
        for args in pragmas:
            if args[0] == "Motor":
                isReversed = "false"
                if "reversed" in args:
                    isReversed = "true"

                funcString = "\tconfig(\"{0}\", {1}, {2}, {3});\n"
                self.outputFile.write(funcString.format(args[2], args[2], args[1], isReversed))

            if args[0] == "Sensor":
                funcString = "\tconfig(\"{0}\", {1}, {2});\n"
                self.outputFile.write(funcString.format(args[2], args[2], args[1]))
        self.outputFile.write("}\n\n")

    # Renames main function into programMain(). This is done so my program doesn't get confused
    # as to which main() to use.
    def ConvertMainFunction(self):
        self.RefreshRead()

        currentLine = self.GetCurrentLine()
        while not self.ReachedEnd():
            if currentLine.find("main()") != -1:
                self.outputFile.write("task programMain() {\n")
                break
            currentLine = self.GetNextLine()

    # This writes down any instantiations of functions writen before the main function.
    def WriteDownFunctions(self):
        self.RefreshRead()
        currentLine = self.GetCurrentLine()
        while not self.ReachedEnd():
            line = currentLine
            if "main" in line:
                break

            elif "task" in line or "void" in line or "int" in line or "bool" in line or "float" in line or "double" in line:
                self.outputFile.write(line)
            currentLine = self.GetNextLine()

    # Writes down the rest of the file after the main function.
    def ConvertRest(self):
        canWrite = False

        self.RefreshRead()
        currentLine = self.GetCurrentLine()
        while not self.ReachedEnd():
            if canWrite:
                self.outputFile.write(currentLine)

            if currentLine.find("main()") != -1:
                canWrite = True
            currentLine = self.GetNextLine()
