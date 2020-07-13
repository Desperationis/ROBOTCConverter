from SettingParser import *
from FileConverter import *
from PythonFileLibrary.RecursiveScanner import *


settingParser = SettingParser()
recursiveScanner = RecursiveScanner(settingParser.inputFolder, ['.c', '.h'])

fileConverter = FileConverter('main.c')

print("/////////////////////////////////////CurrentFile: %s" % fileConverter.fileName)
for line in fileConverter.convertedFile:
    print(line.strip('\n'))
