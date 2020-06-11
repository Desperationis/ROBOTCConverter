# RobotCConverter (WIP)
RobotCConveter is a script designed to run RobotC code in RobotCSimulator.

## How does it work?
RobotCConverter acts as a linker by including the right include directories neccesary for each header and source file in a RobotC library. It also automatically detects and converts `#pragma config` sensors / motors into variables for RobotCSimulator to run.

## How to use it
To use RobotCConverter, you have to edit `setup.txt` to declare the following:


    > Input / Output Folders
    [Library Directory]
    [\Program Directory of RobotCSimulator]

    > Main File
    main.c
    Program.h
    [Includes]
    *end
    
    # OPTIONAL ---------------
    > Header File
    [Input Relative Directory]
    [Output Relative Directory]
    [Includes]
    *end

    > Source File
    [Input Relative Directory]
    [Output Relative Directory]
    [Includes]
    *end

Here's a short example:

    > Input / Output Folders
    C:\Users\user\Desktop\RobotCLibrary
    C:\Users\user\Desktop\RobotCSimulator\RobotCSimulator\Source\ROBOTC\Program

    > Main File
    main.c
    Program.h
    #include "../ROBOTCtoC++/RobotC.h"
    #include "Controllers.h"
    #include "Globals.h"
    #include "Helpers.h"
    #include "Slew.h"
    #include "PID.h"
    #include "Setup.h"
    #include <iostream>
    *end

    > Header File
    Setup/Setup.h
    Setup.h
    *end


    > Source File
    Helpers/Helpers.c
    Helpers.cpp
    #include "../ROBOTCtoC++/RobotC.h"
    #include "Globals.h"
    #include "Helpers.h"
    #include <iostream>
    *end
