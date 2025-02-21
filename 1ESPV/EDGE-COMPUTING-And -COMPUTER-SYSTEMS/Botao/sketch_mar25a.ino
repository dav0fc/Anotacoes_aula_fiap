int led1 = 13;
int led2 = 11;
int led3 = 10;
int led4 = 9;
int led5 = 8;
int botao = 2;
int estado = 0;
void setup()
{
 pinMode(led1, OUTPUT);
 pinMode(led2, OUTPUT);
 pinMode(led3, OUTPUT);
 pinMode(led4, OUTPUT);
 pinMode(led5, OUTPUT);
 pinMode(botao, INPUT);
 digitalWrite(botao, HIGH);
}

void loop()
{
  estado = digitalRead(botao);
  if (estado == HIGH){
  digitalWrite(led1, HIGH);
    digitalWrite(led2, HIGH);
    digitalWrite(led3, HIGH);
    digitalWrite(led4, LOW);
    digitalWrite(led5, LOW);
      }
  else{
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    digitalWrite(led4, HIGH);
    digitalWrite(led5, HIGH);
  }
}
