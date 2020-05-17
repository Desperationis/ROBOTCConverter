import os

"""
    Converter.py

    Base class for converters.
"""
class Converter:
    def __init__(self, rawFileName, outputFileName):
        self.canConvert = True
        self.rawFileName = rawFileName
        self.rawOutputName = outputFileName
        self.rawFile = self.OpenFile(rawFileName, "r")
        self.outputFile = self.OpenFile(outputFileName, "w+")

    # Opens a file safely.
    def OpenFile(self, fileName, mode):
        try:
            return open(fileName, mode)
        except:
            print(fileName + " wasn't found. Cancelling conversion...")
            self.canConvert = False
            return None

    # "Refreshes" read file for reuse.
    def RefreshRead(self):
        if self.canConvert:
            self.rawFile.close()
            self.rawFile = self.OpenFile(self.rawFileName, "r")

    # Converts a file.
    def Convert(self, includeStatements):
        pass

    # Imports include statements into writer file.
    def ImportIncludeStatements(self, includeStatements):
        if self.canConvert:
            for line in includeStatements:
                self.outputFile.write(line)

            self.outputFile.write("\n\n")

