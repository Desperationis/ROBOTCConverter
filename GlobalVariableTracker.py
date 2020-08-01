from PythonFileLibrary.HelperFunctions import *
from RobotCTypes import *
import os

"""
    GlobalVariableTracker.py

    Tracks down global variables and writes a file with
    externs to them.
"""
class GlobalVariableTracker:

    def __init__(self, outputDirectory, globalIncludes):
        # Make file.
        self.outputFile = OpenFileSafely(os.path.join(outputDirectory, "Externs.h"), "w+", True)
        self.outputFile.writelines(globalIncludes)
        self.outputFile.write("\n\n\n\n")

    def ScanConverter(self, fileConverter):
        for line in fileConverter.convertedFile:

            if ';' in line and line[0] not in '\t ':

                if '=' in line:
                    line = line[:line.index("=")] + ";"

                for type in robotCTypes:
                    if type in line:
                        self.outputFile.write('extern ' + line)
                        break
