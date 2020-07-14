from Plugin import *

"""
    MainPlugin.py

    Deals with replacing 'task main()' with 'task programMain'. That's it.
"""
class MainPlugin(Plugin):
    def __init__(self, reader):
        super().__init__(reader)

    def Convert(self):
        # Edit the reader's cached file directly, and replace
        # 'task main' with 'task programMain'
        for index, line in enumerate(self.reader.lines):
            if 'task' in line and 'main' in line:
                self.reader.lines[index] = line.replace('main', "programMain")
                break

        return []
