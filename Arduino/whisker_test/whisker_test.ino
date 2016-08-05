
void setup() {
  pinMode(7, INPUT);
  pinMode(5, INPUT);
  //INPUT = pinMode();
  Serial.begin(9600);
}

void loop() {
int left = digitalRead(5);
int right = digitalRead(7);
Serial.println(left);
Serial.println(right);
delay(1000);
}
