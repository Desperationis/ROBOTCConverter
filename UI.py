import os

"""
    UI.py

    Lets the user choose source and destination folders as well as library and main files.
"""
class UI:
    def __init__(self):
        self.sourceFolder = ""
        self.destinationFolder = ""

    def GetFolders(self):

        file = open("setup.txt", "r")
        lines = file.readlines()

        self.sourceFolder = lines[0].strip()
        self.destinationFolder = lines[1].strip()
