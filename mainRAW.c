#pragma systemFile            // eliminates warning for "unreferenced" functions
#pragma config(Motor,  port1,           leftMotor,     tmotorVex393_HBridge, openLoop)
#pragma config(Motor,  port2,           rightMotor,    tmotorVex393_MC29, openLoop, reversed)

#include "CLibrary.h"

// Notes:
//		90 degree turns aren't possible.
//		Partner joytsicks ARE discontinued.
//		This is meant for non gear train robots

task test1();
int test2();
bool test3;
double test4();
float h();

task main() {
	SetAverageDelay(20);
	SetLeftMotor(port1);
	SetRightMotor(port2);
	SetControllerSpeed(2);
	startTask(LeftArcadeControl);

	while(true) {
		// Keep program alive.
		delay(20);
	}
}
