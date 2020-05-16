import os

class LibraryConverter:
    def __init__(self, rawFile, outputFile):
        self.rawFileName = rawFile
        self.rawOutputName = outputFile
        self.rawFile = open(rawFile, "r")
        self.outputFile = open(outputFile, "w+")

    def Convert(self, includeStatements):
        self.outputFile.write("#pragma once\n")

        for line in includeStatements:
            self.outputFile.write(line)

        self.outputFile.write("\n\n")

        for line in self.rawFile:
            self.outputFile.write(line)