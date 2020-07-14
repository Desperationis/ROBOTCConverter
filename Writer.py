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
        fileName = directory.split('\\')[-1] # Includes '.xxx'
        fileType = fileName.split('.')[-1]
        fileName = directory.split('\\')[-1].split('.')[0] # Doesn't includes '.xxx'

        # Step 2: Convert any .c files into .cpp
        if fileType == 'c':
            fileType = 'cpp'
        fileName += '.' + fileType

        # Step 3: If the file is 'main.cpp', change it to 'Program.h'
        if 'main.cpp' == fileName:
            fileName = 'Program.h'

        # Step 4: Write the contents of fileConverter into output folder.
        outputFile = open(os.path.join(self.outputFolder, fileName), 'w+')

        for line in fileConverter.convertedFile:
            outputFile.write(line)


        print(fileName)
