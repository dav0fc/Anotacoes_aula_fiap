int led_vermelho = 13;
void setup()
{
pinMode(led_vermelho, OUTPUT);
}

void loop()
{
  //B
traco();
for (int x=0;x<3;x++){
  ponto();
}
  //R
ponto();
traco();
ponto();

  //U
for (int x=0;x<2;x++){
  ponto();
}
traco();

  //N
  traco();
  ponto();

  //O
  for (int x=0;x<3;x++){
  traco();
}
delay(3000);
  
}

void traco(){
  digitalWrite(led_vermelho, HIGH);
  delay(2000);
  digitalWrite(led_vermelho, LOW);
  delay(1000);
}

void ponto(){
  digitalWrite(led_vermelho, HIGH);
  delay(1000);
  digitalWrite(led_vermelho, LOW);
  delay(1000);
}
