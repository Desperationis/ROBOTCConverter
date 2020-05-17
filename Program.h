#pragma once
#include "../ROBOTCtoC++/RobotC.h"
#include "CLibrary.h"



MotorPort leftMotor;
MotorPort rightMotor;
void SetUp() {
	config("leftMotor", leftMotor, port1, false);
	config("rightMotor", rightMotor, port2, true);
}

task test1();
int test2();
bool test3;
double test4();
float h();
task programMain() {
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
