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
        self.reader.ResetReader()
        for line in self.reader.CleanRead():
            if len(line) > 0:
                if ';' in line and '(' not in line and line[0] != '\t' and line[0] != ' ':
                    for type in robotCTypes:
                        if type in line:
                            yield line
                            break;

        self.reader.ResetReader()

    def Convert(self):
        for line in self.GetGlobalVariableLines():
            # Append a declaration of a variable.
            if '=' in line:
                line = line[:line.index("=")] + ";"
            ExternPlugin.variables.append("extern " + line);

        return []
