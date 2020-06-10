from PythonFileLibrary.Reader import *
from MainConverter import *
from LibraryConverter import *

class SettingParser(Reader):
    def __init__(self, setupFileName):
        super().__init__(setupFileName)
        self.currentSetting = 0

        self.sourceFolder = "SourceFolderNotSet"
        self.destinationFolder = "DestinationFolderNotSet"

    # Parses the file. This is where the magic happens
    def ParseFile(self):
        if self.canParse:
            self.ResetReader()

            for line in self.CleanRead():
                currentLine = line.strip()

                # '>' indicates the start of a setting
                if '> ' in currentLine:
                    self.currentSetting += 1
                    self.SkipLine()

                if self.currentSetting == 1:
                    self.GetFolders()
                    self.ToNextSetting()

                if self.currentSetting == 2:
                    self.ConvertFile(MainConverter)
                    self.ToNextSetting()

                if self.currentSetting > 2:
                    self.ConvertFile(LibraryConverter)
                    self.ToNextSetting()
        else:
            print ("%s could not be parsed as it doesn't exist." % self.fileName)

    def ToNextSetting(self):
        # Move the cursor 1 line before the next setting
        while not self.ReachedEnd():
            currentLine = self.GetCurrentLine()
            if '> ' in currentLine:
                self.SkipLine(-1)
                break
            else:
                self.SkipLine()

    def GetFolders(self):
        self.sourceFolder = self.GetCurrentLine().strip()
        self.destinationFolder = self.GetNextLine().strip()

    def ConvertFile(self, Converter):
        fileName = self.GetCurrentLine().strip().replace('/', '\\')
        convertedName = self.GetNextLine().strip().replace('/', '\\')

        includes = []
        while not self.ReachedEnd():
            line = self.GetNextLine()
            if '*' not in line:
                includes.append(line)
            else:
                break

        converter = Converter(os.path.join(self.sourceFolder, fileName), os.path.join(self.destinationFolder, convertedName))

        converter.Convert(includes)
