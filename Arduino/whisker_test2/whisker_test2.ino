#include <Servo.h>
 Servo servoRight;
 Servo servoLeft; 

void moveForward(int len){
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1700);
  delay(len);
}

void moveBackwards(int len) {
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1300);
  delay(len);
}

void moveLeft(int len) {
  servoRight.writeMicroseconds(1300);
  servoLeft.writeMicroseconds(1300); 
  delay(len);
}

void moveRight(int len){
  servoRight.writeMicroseconds(1700);
  servoLeft.writeMicroseconds(1700);
  delay(len);
}

void setup()                                 
{            
  servoLeft.attach(13);
  servoRight.attach(12);                                        
  pinMode(7, INPUT);                         
  pinMode(5, INPUT);                          
  Serial.begin(9600);                       
}
 
void loop() {                                                                       
  int Left = digitalRead(5);               
  int Right = digitalRead(7); 
  if ((Left == 1) && (Right == 0)){
    moveBackwards(500);
    moveLeft(500);
  }
  else if ((Left == 0) && (Right == 1)){
    moveBackwards(500);
    moveRight(500);
  }
  else if ((Left == 0) && (Right == 0)){
    moveBackwards(500);
    moveRight(500);
  }
  else {
    moveBackwards(500);
  }
  
  
  
}
