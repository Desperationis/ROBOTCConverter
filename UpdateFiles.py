import os
from LibraryConverter import *
from MainConverter import *

"""
    Converts ROBOT C files to compatible ones.
"""


CLibrary = LibraryConverter("CLibraryRAW.c", "CLibrary.h")
includes = [
    "#include \"../ROBOTCtoC++/RobotC.h\"\n"
]
CLibrary.Convert(includes)


MainFile = MainConverter("mainRAW.c", "Program.h")
includes = [
    "#include \"../ROBOTCtoC++/RobotC.h\"\n",
    "#include \"CLibrary.h\"\n\n"

]
MainFile.Convert(includes)




