#define LEDVERMELHO 15
#define LEDAMARELO 2
#define LEDVERDE 4
#define BOTAO 5

#define pressionado 0

void setup() {
  pinMode(LEDVERMELHO,OUTPUT);
  pinMode(LEDAMARELO,OUTPUT);
  pinMode(LEDVERDE,OUTPUT);
  pinMode(BOTAO,INPUT);
}

void loop() {
  int estado = digitalRead(BOTAO);
  while(estado!=pressionado) {
    digitalWrite(LEDAMARELO,LOW);
    digitalWrite(LEDVERMELHO,LOW);
    digitalWrite(LEDVERDE,HIGH);
    estado = digitalRead(BOTAO);
    if(estado==pressionado) break;
    delay(7000);
    estado = digitalRead(BOTAO);
    if(estado==pressionado) break;
    digitalWrite(LEDAMARELO,HIGH);
    digitalWrite(LEDVERDE,LOW);
    estado = digitalRead(BOTAO);
    if(estado==pressionado) break;
    delay(3000);
    estado = digitalRead(BOTAO);
    if(estado==pressionado) break;
    digitalWrite(LEDAMARELO,LOW);
    digitalWrite(LEDVERMELHO,HIGH);
    estado = digitalRead(BOTAO);
    if(estado==pressionado) break;
    delay(5000);
    estado = digitalRead(BOTAO);
    if(estado==pressionado) break;
  }
  digitalWrite(LEDAMARELO,LOW);
  digitalWrite(LEDVERMELHO,HIGH);
  digitalWrite(LEDVERDE,LOW);
  delay(12000);


  //digitalWrite(nome,HIGH ou LOW) -> ex: digitalWrite(led,HIGH) = ligado
  //digitalRead(nome)
}