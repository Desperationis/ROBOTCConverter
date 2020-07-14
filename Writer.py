from PythonFileLibrary.HelperFunctions import *
import os

"""
    Writer.py

    Writes down converted files into the output folder.
"""

class Writer:
    def __init__(self, outputFolder):
        self.outputFolder = outputFolder

    def WriteFile(self, fileConverter):
        # Step 1: Get file name and type from directory.
        directory = fileConverter.fileName
        fileName = os.path.basename(directory)
        fileType = os.path.splitext(directory)[-1]

        # Step 2: Convert any .c files into .cpp
        if '.c'== fileType:
            fileName = fileName.replace('.c', '.cpp')

        # Step 3: If the file is 'main.cpp', change it to 'Program.h'
        # This is done so RobotCSimulator's main.cpp gets run.
        if 'main.cpp' == fileName:
            fileName = 'Program.h'

        # Step 4: Write the contents of fileConverter into output folder.
        outputFile = OpenFileSafely(os.path.join(self.outputFolder, fileName), 'w+', False)
        outputFile.writelines(fileConverter.convertedFile)

        print("Writer.py: Converted \"%s\" in %s" % (fileName, self.outputFolder))
