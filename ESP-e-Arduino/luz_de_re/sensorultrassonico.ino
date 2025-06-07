
#define trig 4
#define echo 5
#define LEDVERM 11
#define LEDVERD 10
#define LEDAZUL 7
#define buz 8

void vermelhoFuncao(){
  digitalWrite(LEDAZUL, LOW);
  digitalWrite(LEDVERD, LOW);
  digitalWrite(LEDVERM, HIGH);
}

void verdeFuncao(){
  digitalWrite(LEDAZUL, LOW);
  digitalWrite(LEDVERD, HIGH);
  digitalWrite(LEDVERM, LOW);
}

void amareloFuncao(){
  analogWrite(LEDAZUL, 0);
  analogWrite(LEDVERD, 200);
  analogWrite(LEDVERM, 255);
}

void desligaLED(){
  digitalWrite(LEDAZUL,LOW);
  digitalWrite(LEDVERM,LOW);
  digitalWrite(LEDVERD,LOW);
}

void setup() {
  Serial.begin(9600);
  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);
  pinMode(LEDVERM,OUTPUT);
  pinMode(LEDVERD,OUTPUT);
  pinMode(LEDAZUL,OUTPUT);
  pinMode(buz,OUTPUT);
}

void loop() {
  int i;
  digitalWrite(trig,LOW);
  delay(2);
  digitalWrite(trig,HIGH);
  delay(10);
  digitalWrite(trig,LOW);

  long duracao = pulseIn(echo,HIGH);
  float distancia = (duracao * 0.0343) / 2;

  if(distancia > 15 && distancia <=20) {
    verdeFuncao();
    digitalWrite(buz,HIGH);
    delay(500);
    digitalWrite(buz,LOW);
    delay(500);
  }
  else if(distancia<=15 && distancia>10) {
    amareloFuncao();
    digitalWrite(buz,HIGH);
    delay(250);
    digitalWrite(buz,LOW);
    delay(250);
    
  }
  else if(distancia<10) {
    vermelhoFuncao();
    digitalWrite(buz,HIGH);
      delay(100);
      digitalWrite(buz,LOW);
      delay(100);
  }
  else desligaLED();

  Serial.print("Distância: ");
  Serial.print(distancia);
  Serial.println(" cm");

}
