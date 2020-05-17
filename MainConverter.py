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
            self.ImportIncludeStatements(includeStatements)
            self.ConvertPragmaStatements()
            self.WriteDownFunctions()
            self.ConvertMainFunction()
            self.ConvertRest()

    """
    Converts compiler-specific pragma statements into my own functions from RobotCSimulator 
    https://github.com/Desperationis/RobotCSimulator
    """
    def ConvertPragmaStatements(self):
        pragmas = []

        # Search for pragmas
        self.RefreshRead()
        for line in self.rawFile.readlines():

            if "pragma" in line:
                line = line.strip("()\n\t")
                for i in range(10):
                    # Normalize long empty spaces.
                    line = line.replace("  ", " ")
                args = line.split(", ")

                if "Motor" in line:
                    args[0] = "Motor"
                    pragmas.append(args)

        # Write down variables of ports.
        for args in pragmas:
            variableString = "MotorPort {0};\n"
            self.outputFile.write(variableString.format(args[2]))

        # Write down SetUp() function.
        self.outputFile.write("void SetUp() {\n")
        for args in pragmas:
            isReversed = "false"
            if "reversed" in args:
                isReversed = "true"

            funcString = "\tconfig(\"{0}\", {1}, {2}, {3});\n"
            self.outputFile.write(funcString.format(args[2], args[2], args[1], isReversed))
        self.outputFile.write("}\n\n")

    """
        Renames main function into programMain(). This is done so my program doesn't get confused
        as to which main() to use.
        
        
    """
    def ConvertMainFunction(self):
        self.RefreshRead()
        for line in self.rawFile.readlines():
            if line.find("main()") != -1:
                self.outputFile.write("task programMain() {\n")
                break

    """
        This writes down any instantiations of functions writen before the main function.
    """
    def WriteDownFunctions(self):
        self.RefreshRead()
        for line in self.rawFile.readlines():
            if "main" in line:
                break

            elif "task" in line or "void" in line or "int" in line or "bool" in line or "float" in line or "double" in line:
                self.outputFile.write(line)


    """ 
        Writes down the rest of the file after the main function.
    """
    def ConvertRest(self):
        canWrite = False

        self.RefreshRead()
        for line in self.rawFile.readlines():
            if canWrite:
                self.outputFile.write(line)

            if line.find("main()") != -1:
                canWrite = True
