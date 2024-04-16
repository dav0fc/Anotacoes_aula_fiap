#include <Servo.h>
int  servoPin = 11;
int ledPin = 12;
int trigger = 7;
int echo = 8;
float dist = 0;
Servo servoMotor;

void setup(){
  pinMode(servoPin, OUTPUT);
  Serial.begin (9600);
  servoMotor.attach (servoPin);
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop(){
  digitalWrite(trigger, LOW);
  delayMicroseconds(5);
  digitalWrite(trigger, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigger, LOW);
  dist = pulseIn(echo, HIGH);
  dist = dist/58;
  Serial.print("Distancia = ");
  Serial.print(dist);
  Serial.println("cm");
  if ( dist > 30 ) {
    servoMotor.write(0);
    digitalWrite(ledPin, LOW);
    delay(1000);
    Serial.println("Angulo e: " + String(servoMotor.read()));
  }
  else {
    digitalWrite(ledPin,HIGH);
    servoMotor.write(180);
    delay(1000);
    Serial.println("Angulo e: " + String(servoMotor.read()));
    }

}
