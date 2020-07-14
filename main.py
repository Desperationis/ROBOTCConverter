from SettingParser import *
from Writer import *
from FileConverter import *
from ConfigPlugin import *
from MainPlugin import *
from CopyPlugin import *
from IncludePlugin import *
from PythonFileLibrary.RecursiveScanner import *


settingParser = SettingParser()
recursiveScanner = RecursiveScanner(settingParser.inputFolder, ['.c', '.h'])
writer = Writer(settingParser.outputFolder)

for file in recursiveScanner.files:

    fileConverter = FileConverter(file)
    fileConverter.AddPlugin(IncludePlugin)

    includePlugin = fileConverter.AccessPlugin(IncludePlugin)
    includePlugin.SetGlobalIncludes(settingParser.globalIncludes)



    if 'main.c' in file:
        fileConverter.AddPlugin(ConfigPlugin)
        fileConverter.AddPlugin(MainPlugin)
    fileConverter.AddPlugin(CopyPlugin)

    fileConverter.Convert()

    writer.WriteFile(fileConverter)
