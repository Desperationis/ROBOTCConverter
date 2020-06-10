from PythonFileLibrary.Reader import *
from MainConverter import *
from LibraryConverter import *

class SettingParser(Reader):
    def __init__(self, setupFileName):
        super().__init__(setupFileName)
        self.currentSetting = 0

        self.sourceFolder = "SourceFolderNotSet"
        self.destinationFolder = "DestinationFolderNotSet"
        self.converters = []

    # Parses the file. This is where the magic happens
    def ParseFile(self):
        if self.canParse:
            currentLine = self.GetCurrentLine()

            while not self.ReachedEnd():
                # '>' indicates the start of a setting
                if '>' in currentLine:
                    self.currentSetting += 1
                    currentLine = self.GetNextLine()

                if self.currentSetting == 1:
                    self.GetFolders()

                if self.currentSetting == 2:
                    self.GetMain()

                if self.currentSetting > 2:
                    self.GetLibrary()

                # Proceed to the next line
                currentLine = self.GetNextLine()


        else:
            print ("%s could not be parsed as it doesn't exist." % self.fileName)

    def GetFolders(self):
        self.sourceFolder = self.GetCurrentLine()
        self.destinationFolder = self.GetNextLine()

    def GetMain(self):
        fileName = self.GetCurrentLine()
        convertedName = self.GetNextLine()

        includes = []
        line = self.GetNextLine()
        while '*' not in self.GetCurrentLine():
            includes.append(line + "\n")
            line = self.GetNextLine()

        MainFile = MainConverter(os.path.join(self.sourceFolder, fileName), os.path.join(self.destinationFolder,convertedName))
        MainFile.Convert(includes)

    def GetLibrary(self):
        fileName = self.GetCurrentLine()
        convertedName = self.GetNextLine()

        includes = []
        line = self.GetNextLine()
        while '*' not in self.GetCurrentLine():
            includes.append(line + "\n")
            line = self.GetNextLine()


        libraryFile = LibraryConverter(os.path.join(self.sourceFolder, fileName), os.path.join(self.destinationFolder,convertedName))
        libraryFile.Convert(includes)