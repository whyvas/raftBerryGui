#include <Arduino.h>

void setup();
void loop();
#line 1 "src/sketch.ino"
void setup() {  
    Serial.begin(115200);
    delay(2000);
    while (!Serial.available()) {
      Serial.write(0x01);
      delay(3000);
}
    // read the byte that Python will send over
    Serial.read();

}
void loop(){
int fart=0;
while(1){
Serial.print(fart++);
delay(10);
}
}
