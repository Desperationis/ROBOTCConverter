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

        self.blacklist = [
            "#include",
            "#pragma"
        ]

    def Convert(self, includeStatements):
        self.RefreshRead()

        # Include import statements
        self.ImportIncludeStatements(includeStatements)

        # Copy paste the entire file.
        currentLine = self.GetCurrentLine()
        while not self.ReachedEnd():

            skip = False
            for item in self.blacklist:
                if item in currentLine:
                    skip = True
                    break

            if not skip:
                self.outputFile.write(currentLine + "\n")

            currentLine = self.GetNextLine()