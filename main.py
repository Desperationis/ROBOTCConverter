from SettingParser import *
from FileConverter import *
from ConfigPlugin import *
from MainPlugin import *
from CopyPlugin import *
from IncludePlugin import *
from PythonFileLibrary.RecursiveScanner import *


settingParser = SettingParser()
recursiveScanner = RecursiveScanner(settingParser.inputFolder, ['.c', '.h'])

fileConverter = FileConverter('main.c')
fileConverter.AddPlugin(IncludePlugin)
fileConverter.AddPlugin(ConfigPlugin)
fileConverter.AddPlugin(MainPlugin)
fileConverter.AddPlugin(CopyPlugin)

includePlugin = fileConverter.AccessPlugin(IncludePlugin)
includePlugin.SetGlobalIncludes(settingParser.globalIncludes)


fileConverter.Convert()

print("/////////////////////////////////////CurrentFile: %s" % fileConverter.fileName)
for line in fileConverter.convertedFile:
    print(line.strip('\n'))
