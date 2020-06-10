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
    def __init__(self, fileName, outputFileName):
        super().__init__(fileName, outputFileName)

    def Convert(self, includeStatements):
        self.RefreshRead()

        # Include import statements
        self.ImportIncludeStatements(includeStatements)

        # Copy paste the entire file.
        currentLine = self.GetCurrentLine()
        while not self.ReachedEnd():

            if "#include" not in currentLine and "#pragma" not in currentLine:
                self.outputFile.write(currentLine)

            currentLine = self.GetNextLine()