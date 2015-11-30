/*
 * Firmware tester for the Gilroy Lab Linear Robot.
 * This module only sends strings back and forth with 
 * the host computer to verify that everything is 
 * connected and working. 
 */

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0){
    for(int i=0; i<100; i++){
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
}

void call_response(){
  for(int i=0; i<100; i++){
    Serial.print("Polo!\n");
  }
}

void move_bot(String input){
  for(int i=0; i<100; i++){
    Serial.print("done\n");
  }
}

void go_home(){
  for(int i=0; i<100; i++){
    Serial.print("home\n");
  }
}
