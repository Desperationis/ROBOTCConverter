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
        self.ImportIncludeStatements(includeStatements)

        # Copy paste the entire file.
        for line in self.rawFile:
            self.outputFile.write(line)