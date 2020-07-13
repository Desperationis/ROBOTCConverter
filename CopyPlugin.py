from Plugin import *

"""
    CopyPlugin.py

    A plugin that deals with copying content without conversion.

"""
class CopyPlugin(Plugin):
    def __init__(self, reader):
        super().__init__(reader)

    def Convert(self):
        # Copy the entire file from the current file position.
        converted = []
        for line in self.reader.CleanRead():
            converted.append(line)

        return converted
