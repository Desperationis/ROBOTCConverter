import os
from LibraryConverter import *
from MainConverter import *

"""
    main.py

    Converts ROBOT C files to RobotCSimulator compatible ones.
"""

CLibrary = LibraryConverter("CLibraryRAW.c", "CLibrary.h")
includes = [
    "#pragma once\n"
    "#include \"../ROBOTCtoC++/RobotC.h\"\n"
]
CLibrary.Convert(includes)


MainFile = MainConverter("mainRAW.c", "Program.h")
includes = [
    "#include \"../ROBOTCtoC++/RobotC.h\"\n",
    "#include \"CLibrary.h\"\n\n"
]
MainFile.Convert(includes)




