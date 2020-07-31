from SettingParser import *
from Writer import *
from FileConverter import *
from ConfigPlugin import *
from MainPlugin import *
from CopyPlugin import *
from IncludePlugin import *
from TaskPlugin import *
from ExternPlugin import *
from PythonFileLibrary.RecursiveScanner import *


settingParser = SettingParser()
recursiveScanner = RecursiveScanner(settingParser.inputFolder, ['.c', '.h'])
writer = Writer(settingParser.outputFolder)

for file in recursiveScanner.files:

    fileConverter = FileConverter(file)

    # Convert the '#include's as well as add the global includes.
    includePlugin = fileConverter.AddPlugin(IncludePlugin)
    includePlugin.SetGlobalIncludes(settingParser.globalIncludes)


    # Make all tasks exitable.
    fileConverter.AddPlugin(TaskPlugin)

    if 'main.c' in file:
        # Only main.c has a task main() and the configuration for the motors and sensors.
        fileConverter.AddPlugin(ConfigPlugin)
        fileConverter.AddPlugin(MainPlugin)


    # Copy the rest of the file.
    fileConverter.AddPlugin(CopyPlugin)

    # Extern all global variables.
    fileConverter.AddPlugin(ExternPlugin)

    # Compile all plugins to an array of strings.
    fileConverter.Convert()

    writer.WriteFile(fileConverter)

# Write down Extern.h. This is an added file for declaring externs.
file = open(os.path.join(settingParser.outputFolder, "Externs.h"), "w+")
file.write("#pragma once\n")

globalIncludes = settingParser.globalIncludes
for include in globalIncludes:
    if os.path.basename(file.name) in include:
        globalIncludes.remove(include)
        break

file.writelines(settingParser.globalIncludes);
file.write("\n\n");
file.writelines(ExternPlugin.variables);
