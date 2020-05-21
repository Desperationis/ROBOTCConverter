import os
from MainConverter import *
from LibraryConverter import *

"""
    Parser.py

    Parses a setup file and converts its contents.
"""
class Parser:
    def __init__(self):
        self.sourceFolder = ""
        self.destinationFolder = ""
        self.currentSetting = 0
        self.lines = open("setup.txt", "r").readlines()
        self.currentLine = 0
        self.called = False

        self.converters = []

    def ReachedEnd(self):
        return self.currentLine == len(self.lines) - 1

    def GetCurrentLine(self):
        return self.lines[self.currentLine].strip()

    def GetNextLine(self):
        # Read next non-null lines
        self.currentLine += 1

        while len(self.GetCurrentLine()) == 0 and not self.ReachedEnd():
            self.currentLine += 1

        return self.GetCurrentLine()

    def ParseFile(self):
        while not self.ReachedEnd():
            self.GetFolders()
            self.GetMain()
            self.GetLibrary()

            if ">" in self.GetCurrentLine():
                self.currentSetting += 1
                self.called = False

            if not self.ReachedEnd():
                self.GetNextLine()

    def GetFolders(self):
        if self.currentSetting == 1 and not self.called:
            self.sourceFolder = self.GetCurrentLine()
            self.destinationFolder = self.GetNextLine()
            self.called = True

    def GetMain(self):
        if self.currentSetting == 2 and not self.called:
            fileName = self.GetCurrentLine()
            convertedName = self.GetNextLine()

            includes = []
            line = self.GetNextLine()
            while '*' not in self.GetCurrentLine():
                includes.append(line + "\n")
                line = self.GetNextLine()


            MainFile = MainConverter(os.path.join(self.sourceFolder, fileName), os.path.join(self.destinationFolder,convertedName))
            MainFile.Convert(includes)

            self.called = True

    def GetLibrary(self):
        if self.currentSetting > 2 and not self.called:
            fileName = self.GetCurrentLine()
            convertedName = self.GetNextLine()

            includes = []
            line = self.GetNextLine()
            while '*' not in self.GetCurrentLine():
                includes.append(line + "\n")
                line = self.GetNextLine()


            libraryFile = LibraryConverter(os.path.join(self.sourceFolder, fileName), os.path.join(self.destinationFolder,convertedName))
            libraryFile.Convert(includes)

            self.called = True