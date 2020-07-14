import PythonFileLibrary.SettingParser

"""
    SettingParser.py

    Parses setup.txt for input and output folders, global includes, and more.
"""
class SettingParser(PythonFileLibrary.SettingParser.SettingParser):
    def __init__(self):
        super().__init__()

        # The directory of the folder to be scanned.
        self.inputFolder = ""

        # The directory of the output folder.
        self.outputFolder = ""

        # Global #include's !
        self.globalIncludes = []

        try:
            self.Parse()
        except AssertionError as error:
            print(error)

    # Parse setup.txt. Will throw an AssertionError if the
    # file cannot be read.
    def Parse(self):
        assert self.canParse, "SettingParser.py: Could not parse setup.txt."

        currentSetting = 0
        for line in self.GetSettings():
            currentSetting += 1

            if currentSetting == 1:
                self.inputFolder = self.GetNextLine().strip()
                self.outputFolder = self.GetNextLine().strip()

            if currentSetting == 2:
                while not self.ReachedEnd():
                    currentLine = self.GetNextLine()
                    if '*end' not in currentLine:
                        self.globalIncludes.append(currentLine)
                    else:
                        break

        self.ResetReader()
