import os
from Plugin import *
from PythonFileLibrary.HelperFunctions import *

"""
    IncludePlugin.py

    Includes global headers into each file, as well as
    make their '#include's relative to the directory of RobotCSimulator.
"""
class IncludePlugin(Plugin):
    def __init__(self, reader):
        super().__init__(reader)
        self.globalIncludes = []

    # Sets an array of strings as a list of '#include's
    def SetGlobalIncludes(self, includes):
        self.globalIncludes = includes

    # Only get lines with '#include'
    def GetIncludes(self):
        self.reader.ResetReader()
        for line in self.reader.CleanRead():
            if '#include' in line and line[0] in '#':
                yield line.strip('\n')

        self.reader.ResetReader()

    def Convert(self):
        converted = []

        # In RobotCSimulator, all files are located in a single folder.
        # This will convert all '#include's to only include header files and
        # strip away relative folder includes.
        for line in self.GetIncludes():
            # Get the relative directory of the file.
            line = RemoveElements(line, ['#include', ' ', '\"'])

            # Get the file name and type of each directory.
            line = os.path.basename(line)
            type = os.path.splitext(line)[-1]

            # Ignore .c files. You can't / shouldn't include them in C++.
            # Use headers instead!
            if type != '.c':
                converted.append("#include \"%s\"\n" % line)
            else:
                print("IncludePlugin: \"%s\" was skipped in %s as it\'s a .cpp file." % (line, self.reader.fileName))

        # Include global includes last
        converted.extend(self.globalIncludes)

        return converted
