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

        # Ignores these when copying
        self.blacklist = [
            "#include",
            "#pragma"
        ]

    def Convert(self, includeStatements):
        if self.canConvert:
            self.RefreshRead()

            # Include import statements
            self.ImportIncludeStatements(includeStatements)


            self.ResetReader()
            # Copy paste the entire file.
            for line in self.CleanRead():
                skip = False
                for item in self.blacklist:
                    if item in line:
                        skip = True
                        break

                if not skip:
                    self.outputFile.write(line)
        else:
            print("Library Conversion could not happen; File not opened.")