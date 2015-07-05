/*
 * Firmware for the Gilroy Lab Linear Robot.
 */

void setup() {
  Serial.begin(9600);
  Serial.println("Marco!");
}

void loop() {
  int i = 0;
  Serial.println(i);
  i++;
}
