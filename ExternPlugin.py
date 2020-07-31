from PythonFileLibrary.HelperFunctions import *
from RobotCTypes import *
from Plugin import *

"""
    ExternPlugin.py

    A plugin responsible externing global RobotC variables.
"""
class ExternPlugin(Plugin):
    variables = []

    def __init__(self, reader):
        super().__init__(reader)

    # Get lines that have variables in them.
    def GetGlobalVariableLines(self):
        for line in self.reader.CleanRead():
            if ';' in line and '(' not in line and '\t' not in line:
                for type in robotCTypes:
                    if type in line:
                        yield line

        self.reader.ResetReader()

    def Convert(self):
        for line in self.GetGlobalVariableLines():
            ExternPlugin.variables.append("extern " + line);

        return []
