int led_vermelho = 13;
void setup()
{
pinMode(led_vermelho, OUTPUT);
}

void loop()
{
  //Ponto
  for (int x=0;x<3;x++){
    digitalWrite(led_vermelho, HIGH);
  delay(1000);
  digitalWrite(led_vermelho, LOW);
  delay(1000);
    
  }
  //Traço
  for (int x=0;x<3;x++){
    digitalWrite(led_vermelho, HIGH);
  delay(2000);
  digitalWrite(led_vermelho, LOW);
  delay(1000);
  }
  //Ponto
    for (int x=0;x<3;x++){
    digitalWrite(led_vermelho, HIGH);
  delay(1000);
  digitalWrite(led_vermelho, LOW);
  delay(1000);
    
  }


delay(3000);
  
}
