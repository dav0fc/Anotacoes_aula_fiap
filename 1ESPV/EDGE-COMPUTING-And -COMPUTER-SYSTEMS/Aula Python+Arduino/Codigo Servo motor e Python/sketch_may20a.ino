#include <Servo.h>
int servoPin = 9;
Servo servoMotor;
void setup() {
pinMode(servoPin, OUTPUT);
Serial.begin(9600);
servoMotor.attach (servoPin);
}

void loop() {
  if(Serial.available() > 0){
    char letra = Serial.read();
    if (letra == 'a'){
      servoMotor.write(0);
    }
    else if (letra == 'b'){
      servoMotor.write(45);
    }
    else if (letra == 'c'){
      servoMotor.write(90);
    }
    else if (letra == 'd'){
      servoMotor.write(180);
    }
} 
}
