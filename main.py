from SettingParser import *
from FileConverter import *
from ConfigPlugin import *
from MainPlugin import *
from CopyPlugin import *
from PythonFileLibrary.RecursiveScanner import *


settingParser = SettingParser()
recursiveScanner = RecursiveScanner(settingParser.inputFolder, ['.c', '.h'])

fileConverter = FileConverter('main.c')
fileConverter.AddPlugin(ConfigPlugin)
fileConverter.AddPlugin(MainPlugin)
fileConverter.AddPlugin(CopyPlugin)
fileConverter.Convert()

print("/////////////////////////////////////CurrentFile: %s" % fileConverter.fileName)
for line in fileConverter.convertedFile:
    print(line.strip('\n'))
