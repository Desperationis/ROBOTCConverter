from PythonFileLibrary.Reader import *
from PythonFileLibrary.HelperFunctions import *

"""
    FileConverter.py

    Converts a RobotC file into a .cpp file.
"""

class FileConverter(Reader):
    def __init__(self, fileName):
        super().__init__(fileName)

        try:
            self.Convert()
        except AssertionError as error:
            print(error)

    def GetPragma(self):
        for line in self.CleanRead():
            if '#pragma' in line:
                yield line.strip('\n')

        self.ResetReader()

    def Convert(self):
        assert self.canParse, "FileConverter.py: Could not read \"%s\"" % (self.fileName)

        for pragma in self.GetPragma():
            pragma = RemoveElements(['#pragma', '(', ')'], pragma)

            if 'config' in pragma:
                pragma = pragma.replace('config', "")
                args = pragma.split(',')

                for i in range(len(args)):
                    args[i] = args[i].replace(" ", "")

                print(args)
