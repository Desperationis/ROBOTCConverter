import os
from Converter import *

"""
    MainConverter.py

    Converts a RobotC file using main conversion.

    You should use this conversion if:
        File has task main
        Uses #pragma config to set up motors

    Main files are basically the file that runs the program and includes
    any external libraries.
"""
class MainConverter(Converter):
    def __init__(self, rawFileName, outputFileName):
        super().__init__(rawFileName, outputFileName)

    def Convert(self, includeStatements):
        pass
