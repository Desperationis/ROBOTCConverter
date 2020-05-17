#pragma once
#include "../ROBOTCtoC++/RobotC.h"


// Notes:
//		90 degree turns aren't possible.
//		Partner joytsicks ARE discontinued.


// TODO:
// 		Arcade Control
// 		Tank Control
// 		Gamer Control
//		Slew Control
// 		PID Control
//		Precision Control With Encoder


// Positive Power turns left motor clockwise. + Forward - Backward

// Left Axle Variables
// Ch4: X <- Ch3: Y Positive Down

// Right Axle Variables
// Ch1: X -> Ch2: Y Positive Down

int controllerSpeed = 1;
int maximumMotorValue = 127;
int leftMotorPort = port1;
int rightMotorPort;
int taskDelay = 20;

void SetLeftMotor(int port) {
	leftMotorPort = port;
}

void SetRightMotor(int port) {
	rightMotorPort = port;
}

void SetControllerSpeed(int speed) {
	controllerSpeed = speed;
	maximumMotorValue = 127 / speed;
}

void SetAverageDelay(int delayTime) {
	taskDelay = delayTime;
}

int Clamp(int value) {
	// Clamps integers to maximum motor value
	if (value > maximumMotorValue) {
		return maximumMotorValue;
	}
	if (value < -maximumMotorValue) {
		return -maximumMotorValue;
	}
	return value;
}

task LeftArcadeControl() {
	// Keep thread alive.
	while (true) {
		// Arcade control with left joystick.
		motor[leftMotorPort] = Clamp(-vexRT[Ch3] - vexRT[Ch4] / controllerSpeed);
		motor[rightMotorPort] = Clamp(-vexRT[Ch3] + vexRT[Ch4] / controllerSpeed);

		delay(taskDelay);
	}
}


task RightArcadeControl() {
	// Keep thread alive.
	while (true) {
		// Arcade control with right joystick.
		motor[leftMotorPort] = Clamp(-vexRT[Ch2] + vexRT[Ch1] / controllerSpeed);
		motor[rightMotorPort] = Clamp(-vexRT[Ch2] - vexRT[Ch1] / controllerSpeed);

		delay(taskDelay);
	}
}

task CustomTankControl() {
	// Keep thread alive.
	while (true) {
		// Tank control with both joysticks.
		motor[leftMotorPort] = -vexRT[Ch3] / controllerSpeed;
		motor[rightMotorPort] = -vexRT[Ch2] / controllerSpeed;

		delay(taskDelay);
	}
}

task GamerControl() {
	// Keep thread alive.
	while (true) {
		// Game control (Similar to controls in racing games)
		// Left Axis: up / down
		// Right Axis: right / left
		motor[leftMotorPort] = Clamp(-vexRT[Ch3] + vexRT[Ch1] / controllerSpeed);
		motor[rightMotorPort] = Clamp(-vexRT[Ch3] - vexRT[Ch1] / controllerSpeed);

		delay(taskDelay);
	}
}