# RobotCConverter 
RobotCConverter is a file parser meant to convert code written in RobotC into RobotCSimulator code. 

## Setting it up
The only parameters necessary to use this converter is to specify the directory of the files you want to scan, as well as the output directory, which would be wherever `RobotCSimulator/RobotCProgram` is located in inside your computer. Both of these requirements are found in `setup.txt`. Here's an example:

    > Input / Output Folders
    C:\Users\smart\Desktop\RobotCLibrary
    C:\Users\smart\Desktop\RobotCSimulator\RobotCProgram
   
## Caveats

This converter was made with the intent of converting RobotCLibrary code into RobotCSimaultor. As such, RobotCConverter / RobotCSimulator does not support the following RobotC functionalities:
* Automatic function capitalization.
* Automatic semicolon insertion.
* `#include` of files not in the same root directory (could be in folders).
* `while` loops with conditions spanning more than one line.
* Integrated Functions other than:
  * `startTask()`
  * `stopAllTasks()`
  * `delay()`
  * All `Math` commands.
* Integrated Variables other than:
  * `motor[]`
  * `SensorValue[]`
  * `vexRT[]`
  
  Using RobotCSimulator and RobotCConverter assumes you are making a program / library that:
   * Uses raw `motor[], SensorValue[], vexRT[]` values.
   * Could possibly be multi-tasked.
   * Could include other files.
