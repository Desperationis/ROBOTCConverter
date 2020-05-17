import os
from Converter import *

"""
    LibraryConverter.py
    
    Converts a RobotC file using library conversion.
    
    The exact requirements for safe library conversions:
        Mustn't include main function
        Mustn't use #pragma config
        
    RobotC libraries are basically included .c files with no main function.
"""
class LibraryConverter(Converter):
    def __init__(self, rawFileName, outputFileName):
        super().__init__(rawFileName, outputFileName)

    def Convert(self, includeStatements):
        # Includes include statements.
        if self.canConvert:
            self.outputFile.write("#pragma once\n")

            for line in includeStatements:
                self.outputFile.write(line)

            self.outputFile.write("\n\n")

            for line in self.rawFile:
                self.outputFile.write(line)