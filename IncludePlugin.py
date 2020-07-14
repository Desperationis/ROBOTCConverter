from Plugin import *
from PythonFileLibrary.HelperFunctions import *

class IncludePlugin(Plugin):
    def __init__(self, reader):
        super().__init__(reader)
        self.globalIncludes = []

    def SetGlobalIncludes(self, includes):
        self.globalIncludes = includes

    def GetIncludes(self):
        self.reader.ResetReader()
        for line in self.reader.CleanRead():
            if '#include' in line:
                yield line.strip('\n')

        self.reader.ResetReader()

    def Convert(self):
        converted = []

        for line in self.GetIncludes():
            # Get the directory of the file.
            line = RemoveElements(line, ['#include', ' ', '\"'])

            # Only get the file name of the directory.
            line = line.split("/")[-1]

            # Convert.c files into .cpp
            line = line.replace('.c', '.cpp')

            converted.append("#include \"%s\"\n" % line)

        for line in self.globalIncludes:
            converted.append(line)

        return converted
