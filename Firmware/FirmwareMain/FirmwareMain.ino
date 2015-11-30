/*
 * Firmware for the Gilroy Lab Linear Robot.
 */
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_PWMServoDriver.h"

Adafruit_MotorShield AFMS = Adafruit_MotorShield(); 
Adafruit_StepperMotor *myMotor = AFMS.getStepper(200, 2);

double steps_per_cm = 1300;
const int switch_pin = 8;

void setup() {
  Serial.begin(9600);
  AFMS.begin();
  myMotor->setSpeed(150);
  pinMode(switch_pin, INPUT);
}

void loop() {
  if (Serial.available() > 0){
    for(int i=0; i<10; i++){
      Serial.print("Received\n");
    }
    String incoming_string = Serial.readString();
    //if statement to handle all of the commands
    if(incoming_string.equals("Marco!"))
      call_response();
    else if(incoming_string.charAt(0) == 'm')
      move_bot(incoming_string);
    else if(incoming_string.equals("home"))
      go_home();
  } 
  myMotor->release();
}

void call_response(){
  for(int i=0; i<100; i++){
    Serial.print("Polo!\n");
  }
}

void move_bot(String input){
  String len = input.substring(1, input.length());
  Serial.println(len);
  double move_len = (double)len.toInt();
  Serial.println(move_len);
  Serial.println(move_len*steps_per_cm);
  double move_length = move_len*steps_per_cm;
  Serial.println(move_length);
  if (move_length > 0){
    while(move_length > 0){
      myMotor->step(1, BACKWARD, SINGLE);
      move_length--;
    }
  }else{
    move_length = abs(move_length);
    while(digitalRead(switch_pin) != LOW && move_length > 0){
      myMotor->step(1, FORWARD, SINGLE); 
      move_length--;
    } 
  }
  if(digitalRead(switch_pin) == LOW)
    for(int i=0; i<100; i++){
      Serial.print("home\n");
    }
  else 
    for(int i=0; i<100; i++){
      Serial.print("done\n");
    }
}

void go_home(){
  while(digitalRead(switch_pin) != LOW){
    myMotor->step(10, FORWARD, SINGLE);
  }
  for(int i=0; i<100; i++){
    Serial.print("home\n");
  }
}
