from SettingParser import *
from Writer import *
from FileConverter import *
from ConfigPlugin import *
from MainPlugin import *
from CopyPlugin import *
from IncludePlugin import *
from TaskPlugin import *
from PythonFileLibrary.RecursiveScanner import *


settingParser = SettingParser()
recursiveScanner = RecursiveScanner(settingParser.inputFolder, ['.c', '.h'])
writer = Writer(settingParser.outputFolder)

settingParser.globalIncludes.append("#include \"Externs.h\"\n")

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

    # Compile all plugins to an array of strings.
    fileConverter.Convert()

    writer.WriteFile(fileConverter)



    # Turn motor and sensor ports into externs.
    if 'main.c' in file:
        ports = []
        for line in fileConverter.convertedFile:
            if 'MotorPort ' in line or 'SensorPort ' in line:
                ports.append('extern ' + line)

        outputFile = OpenFileSafely(os.path.join(settingParser.outputFolder, "Externs.h"), "w+", True)
        settingParser.globalIncludes.remove("#include \"Externs.h\"\n")
        outputFile.writelines(settingParser.globalIncludes)
        outputFile.writelines(ports)
