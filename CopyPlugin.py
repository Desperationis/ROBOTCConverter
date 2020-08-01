from Plugin import *

"""
    CopyPlugin.py

    A plugin that deals with copying content.
"""
class CopyPlugin(Plugin):
    def __init__(self, reader):
        super().__init__(reader)

    def Convert(self):
        # C++ and C are pretty similar semantically. As long
        # as RobotC code is written without low-level functionality,
        # such as:

        # int = enum (C++ needs enum to be cast)
        # void* = int* (void* can only be assigned to void* in C++)
        # char[3] = "ABC" (Possible in C, but not in C++, as the array has
        # to be longer than the number of characters to hold \0)

        # And such. Using this tool assumes you had C++ in mind when writing your code.

        converted = []
        for line in self.reader.CleanRead():

            # Skip #pragma's and #include's. RobotC and RobotCSimulator
            # are completely different preprocessor-wise. These can be converted
            # with ConfigPlugin.py and IncludePlugin.py, respectively.
            if '#pragma' not in line and '#include' not in line and '#error' not in line:
                converted.append(line)


        return converted
