#define LDR 34
#define LED 26
#define LED2 25


void setup() {
  Serial.begin(9600);
  pinMode(LED,OUTPUT);
  pinMode(LED2,OUTPUT);
}

void loop() {
  int analogValue = analogRead(LDR);
  
  Serial.print("Analog Value = ");
  Serial.println(analogValue);
  
  if(analogValue >= 600){
    digitalWrite(LED,HIGH);
    digitalWrite(LED2,LOW);
  }
  else {
    digitalWrite(LED,LOW);
    digitalWrite(LED2,HIGH); 
  }
  delay(500);
}
