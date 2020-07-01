from PythonFileLibrary.HelperFunctions import *
from Converter import *

"""
    MainConverter.py

    Converts the main file. (The file that runs the program)
"""
class MainConverter(Converter):
    def __init__(self, fileName, outputFileName):
        super().__init__(fileName, outputFileName)

        self.continueAt = 0

        # Ignores these when parsing pragmas
        self.blacklist = [
            "#",
            "(",
            ")",
            "\n",
            "\t",
            "pragma",
            "config",
            " "
        ]

    def Convert(self, includeStatements):
        if self.canConvert:
            self.ImportIncludeStatements(includeStatements)
            self.ConvertPragmaStatements()
            self.ConvertRest()

    # Converts compiler-specific #pragma statements into my own functions from RobotCSimulator
    # https://github.com/Desperationis/RobotCSimulator
    def ConvertPragmaStatements(self):
        pragmas = []

        # Search for pragmas
        self.RefreshRead()
        for line in self.CleanRead():
            if "pragma" in line:
                if "config" in line:
                    # Get arguments from #pragma config
                    line = RemoveElements(self.blacklist, line)
                    args = line.split(",")
                    pragmas.append(args)

            # Marks the spot where pragmas end.
            elif "// start" in line:
                self.continueAt = self.currentLine
                break

        # Write down variables of ports; SensorPort && MotorPort
        for args in pragmas:
            variable = "{0}Port {1};".format(args[0], args[2])
            self.outputFile.write(variable + "\n")


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

    # Writes down the rest of the file. main() will also be replaced by
    # programMain().
    def ConvertRest(self):

        self.RefreshRead()
        self.SkipLine(self.continueAt)
        for line in self.CleanRead():
            if "main()" in line:
                line = line.replace("main()", "programMain()")

            # Absolutely ignores anything with #
            if "#" not in line:
                self.outputFile.write(line)
