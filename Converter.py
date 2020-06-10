from PythonFileLibrary.Reader import *
from PythonFileLibrary.HelperFunctions import *

"""
    Converter.py

    Base class for converters.
"""
class Converter(Reader):
    def __init__(self, fileName, outputFileName):
        super().__init__(fileName)

        self.outputFileName = outputFileName
        self.outputFile = OpenFileSafely(outputFileName, "w+", True)

        self.canConvert = not OneIs((self.file, self.outputFile), None)

    # "Refreshes" read file for reuse.
    def RefreshRead(self):
        if self.canConvert:
            self.currentLine = 0

    # Converts a file.
    def Convert(self, includeStatements):
        pass

    # Imports include statements into writer file.
    def ImportIncludeStatements(self, includeStatements):
        if self.canConvert:
            for line in includeStatements:
                self.outputFile.write(line)

            self.outputFile.write("\n")

