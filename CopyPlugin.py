from Plugin import *

"""
    CopyPlugin.py

    A plugin that deals with copying content.
"""
class CopyPlugin(Plugin):
    def __init__(self, reader):
        super().__init__(reader)

    def Convert(self):
        # Copy the entire file from the current file position.
        converted = []
        for line in self.reader.CleanRead():

            # Skip #pragma's and #include's. They are never guaranteed to work.
            if '#pragma' not in line and '#include' not in line:
                converted.append(line)


        return converted
