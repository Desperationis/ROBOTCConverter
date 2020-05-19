import os
from LibraryConverter import *
from MainConverter import *
from UI import *

"""
    main.py

    Converts ROBOT C files to RobotCSimulator compatible ones.
"""


ui = UI()
ui.GetFolders()

CLibrary_D = LibraryConverter(ui.sourceFolder + r"\CLibrary.h", ui.destinationFolder + r"\CLibraryDeclarations.h")
includes = [
    "#pragma once\n"
    "#include \"../ROBOTCtoC++/RobotC.h\"\n"

]
CLibrary_D.Convert(includes)


CLibrary = LibraryConverter(ui.sourceFolder + r"\CLibrary.c", ui.destinationFolder + r"\CLibrary.h")
includes = [
    "#pragma once\n"
    "#include \"../ROBOTCtoC++/RobotC.h\"\n"
    "#include \"CLibraryDeclarations.h\"\n"
]
CLibrary.Convert(includes)


MainFile = MainConverter(ui.sourceFolder + r"\main.c", ui.destinationFolder + r"\Program.h")
includes = [
    "#include \"../ROBOTCtoC++/RobotC.h\"\n",
    "#include \"CLibrary.h\"\n\n"
]
MainFile.Convert(includes)




