//This is the Arduino portion of the raftBerry project. It can be directly uploaded to an arduino mega from the pi by using
//the command ino upload. (Install arduino on the pi)

//Pin Definitions
//PORT* are for motor on left side, one pin controlling each of the low, medium, high speed and direction (h-bridge) relays.
//STAR* are the same as PORT* but for the righthand motor.
//JOY is for the 4 joystick input switches
//SHUTDOWN is for the emergency shutdown button
//AUTOMAN is for the automatic/manual navigation selection switch.

#define PORTDIR 8
#define PORTLOW 9
#define PORTMED 10
#define PORTHIGH 7
#define STARDIR 6
#define STARLOW 12
#define STARMED 13
#define STARHIGH 11
#define JOYUP 52
#define JOYDOWN 50
#define JOYLEFT 48
#define JOYRIGHT 46
#define SHUTDOWN 42
#define AUTOMAN 44

//Global Variables
int leftspeed = 0;
int rightspeed = 0;
char receivedChar;


void setup() {  
  Serial.begin(115200);

//Setup pins    
pinMode(AUTOMAN, INPUT_PULLUP);
pinMode(PORTDIR, OUTPUT);
pinMode(PORTLOW, OUTPUT);
pinMode(PORTMED, OUTPUT);
pinMode(PORTHIGH, OUTPUT);
pinMode(STARDIR, OUTPUT);
pinMode(STARLOW, OUTPUT);
pinMode(STARMED, OUTPUT);
pinMode(STARHIGH, OUTPUT);
pinMode(JOYUP, INPUT_PULLUP);
pinMode(JOYDOWN, INPUT_PULLUP);
pinMode(JOYLEFT, INPUT_PULLUP);
pinMode(JOYRIGHT, INPUT_PULLUP);
pinMode(SHUTDOWN, INPUT_PULLUP);
}

//Main program loop, if manual mode is selected, scan user controls and control relays accordingly, otherwise go
//into automatic mode and await navigation input from the pi via serial characters.
void loop(){
      if (digitalRead(AUTOMAN)==LOW){
        motorsOff();
        Serial.print("raftBerry manual mode\n");
        leftspeed = 0;
        rightspeed = 0;
        setSpeed();
        while(digitalRead(AUTOMAN)==LOW){
          if(digitalRead(SHUTDOWN)==LOW){
            emergencyStop();
            Serial.print("Emerg\n");
          }
          if(digitalRead(JOYUP) ==LOW){
            joyUp();
          }
          if(digitalRead(JOYDOWN) ==LOW){
            joyDown();
          }
          if(digitalRead(JOYLEFT) ==LOW){
            joyLeft();
          }
          if(digitalRead(JOYRIGHT) ==LOW){
            joyRight();
          }
          execCmd();
          delay(500);
        }
}
	
	if (digitalRead(AUTOMAN)==HIGH){
		Serial.print("Auto Mode\n");
		while(digitalRead(AUTOMAN)==HIGH{
				execCmd();
			}
	}
	
}


//Function to turn off all motors
void motorsOff(){
  digitalWrite(STARHIGH, HIGH);
  digitalWrite(STARMED, HIGH);
  digitalWrite(STARLOW, HIGH);
  digitalWrite(STARDIR, HIGH);
  digitalWrite(PORTHIGH, HIGH);
  digitalWrite(PORTMED, HIGH);
  digitalWrite(PORTLOW, HIGH);
  digitalWrite(PORTDIR, HIGH);
  Serial.print("Motors off");
}

//Turn off motors, cleanup GPIO and shutdown.
void emergencyStop(){
  Serial.print("Emergency stop button pressed\n");
  leftspeed=0;
  rightspeed=0;
  motorsOff();
  exit(0);
}
//Set relays for direction and speed.
void setSpeed(){
  if (rightspeed==3){
    digitalWrite(STARHIGH,LOW);
    digitalWrite(STARMED,LOW);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,HIGH);
    //Serial.print(String("\nSet Right:") + rightspeed);
  }
  else if (rightspeed==2){
    digitalWrite(STARHIGH,HIGH);
    digitalWrite(STARMED,LOW);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,HIGH);
    //Serial.print(String("\nSet Right:") +rightspeed);
  }
  else if (rightspeed==1){
    digitalWrite(STARHIGH,HIGH);
    digitalWrite(STARMED,HIGH);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,HIGH);
    //Serial.print(String("\nSet Right:") +rightspeed);
  }
  else if (rightspeed==0){
    digitalWrite(STARHIGH,HIGH);
    digitalWrite(STARMED,HIGH);
    digitalWrite(STARLOW,HIGH);
    digitalWrite(STARDIR,HIGH);
    //Serial.print(String("\nSet Right:") +rightspeed);
  }
  else if (rightspeed==-1){
    digitalWrite(STARHIGH,HIGH);
    digitalWrite(STARMED,HIGH);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,LOW);
    //Serial.print(String("\nSet Right:") + rightspeed);
  }
  else if (rightspeed==-2){
    digitalWrite(STARHIGH,HIGH);
    digitalWrite(STARMED,LOW);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,LOW);
    //Serial.print(String("\nSet Right:")+ rightspeed);
  }
  else if (rightspeed==-3){
    digitalWrite(STARHIGH,LOW);
    digitalWrite(STARMED,LOW);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,LOW);
    //Serial.print(String("\nSet Right:") + rightspeed);
  }
  if (leftspeed==3){
    digitalWrite(PORTHIGH,LOW);
    digitalWrite(PORTMED,LOW);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,HIGH);
    //Serial.print(String("\nSet Left:") +leftspeed);
  }
else if (leftspeed==2){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,LOW);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,HIGH);
    //Serial.print(String("\nSet Left:") +leftspeed);
}
else if (leftspeed==1){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,HIGH);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,HIGH);
    //Serial.print(String("\nSet Left:") +leftspeed);
}
else if (leftspeed==0){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,HIGH);
    digitalWrite(PORTLOW,HIGH);
    digitalWrite(PORTDIR,LOW);
    //Serial.print(String("\nSet Left:") +leftspeed);
}
  else if (leftspeed==-1){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,HIGH);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,LOW);
    //Serial.print(String("\nSet Left:") +leftspeed);
  }
  else if (leftspeed==-2){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,LOW);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,LOW);
    //Serial.print(String("\nSet Left:") +leftspeed);
  }
  else if (leftspeed==-3){
    digitalWrite(PORTHIGH,LOW);
    digitalWrite(PORTMED,LOW);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,LOW);
    //Serial.print(String("\nSet Left:") +leftspeed);
  }
}

void decLeft(){
   if (leftspeed > -3){
    leftspeed-=1;
   }
}
void incLeft(){
  if (leftspeed < 3){
    leftspeed+=1;
    }
  else if (rightspeed > -3){
    rightspeed-=1;
  }
}
void incRight(){
  if (rightspeed < 3){
    rightspeed+=1;
  }
  else if (leftspeed > -3){
    leftspeed-=1;
  }
}
void decRight(){
  if (rightspeed > -3){
    rightspeed-=1;
  }
}

//Read joystick inputs  
void joyUp(){
//  Serial.print("\nJoystick up");
  if (leftspeed < 3){
    leftspeed+=1;
  }
  if (rightspeed < 3){
      rightspeed+=1;
  }
//  Serial.print(String("Left:") + leftspeed + String("Right:") +rightspeed);
  setSpeed();
}
void joyDown(){
 // Serial.print("\nJoystick down");
  if (leftspeed > -3){
    leftspeed-=1;
  }
  if (rightspeed > -3){
    rightspeed-=1;
  }
  //Serial.print(String("Left:") + leftspeed + String("Right:") +rightspeed);
  setSpeed();
  }
void joyLeft(){
  //Serial.print("\nJoystick left");
  incRight();
  //Serial.print(String("Left:") + leftspeed + String("Right:") +rightspeed);
  setSpeed();
}
void joyRight(){
  //Serial.print("\nJoystick right");
  incLeft();
  //Serial.print(String("Left:") + leftspeed + String("Right:") +rightspeed);
  setSpeed();
}

//The following function reads single characters from the serial port and reacts accoding to the following table:
//A = set PORT to high forward
//B = set PORT to medium forward
//C = set PORT to low forward
//D = set PORT to OFF
//E = set PORT to low reverse
//F = set PORT to medium reverse
//G = set PORT to high reverse
//H = set STAR to high forward
//I = set STAR to medium forward
//J = set STAR to low forward
//K = set STAR to OFF
//L = set STAR to low reverse
//M = set STAR to medium reverse
//N = set STAR to high reverse
//O = Fire missile launcher

void execCmd() {
	if (Serial.available() > 0) {
		receivedChar = Serial.read();
		//Check if in manual mode before doing motor adjustments.
		if (digitalRead(AUTOMAN)==HIGH){
			if (receivedChar=="A"){
			leftspeed=3;
			setSpeed();
			}
		
			
		}
	}
}
