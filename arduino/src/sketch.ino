//GPIO connections

#define AUTOMAN 42
#define PORTDIR 9
#define PORTLOW 6
#define PORTMED 7
#define PORTHIGH 8
#define STARDIR 13
#define STARLOW 10
#define STARMED 11
#define STARHIGH 12
#define JOYUP 52
#define JOYDOWN 48
#define JOYLEFT 46
#define JOYRIGHT 50
#define SHUTDOWN 44

//Global Variables
int leftspeed = 0;
int rightspeed = 0;


void setup() {  
  Serial.begin(115200);

//Setup GPIO pins    
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
  Serial.print("Emergency stop button pressed");
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
    digitalWrite(STARDIR,LOW);
    Serial.print(String("Set Right:") + rightspeed);
  }
  else if (rightspeed==2){
    digitalWrite(STARHIGH,HIGH);
    digitalWrite(STARMED,LOW);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,LOW);
    Serial.print(String("Set Right:") +rightspeed);
  }
  else if (rightspeed==1){
    digitalWrite(STARHIGH,HIGH);
    digitalWrite(STARMED,HIGH);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,LOW);
    Serial.print(String("Set Right:") +rightspeed);
  }
  else if (rightspeed==0){
    digitalWrite(STARHIGH,HIGH);
    digitalWrite(STARMED,HIGH);
    digitalWrite(STARLOW,HIGH);
    digitalWrite(STARDIR,HIGH);
    Serial.print(String("Set Right:") +rightspeed);
  }
  else if (rightspeed==-1){
    digitalWrite(STARHIGH,1);
    digitalWrite(STARMED,1);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,1);
    Serial.print(String("Set Right:") + rightspeed);
  }
  else if (rightspeed==-2){
    digitalWrite(STARHIGH,HIGH);
    digitalWrite(STARMED,LOW);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,HIGH);
    Serial.print(String("Set Right:")+ rightspeed);
  }
  else if (rightspeed==-3){
    digitalWrite(STARHIGH,LOW);
    digitalWrite(STARMED,LOW);
    digitalWrite(STARLOW,LOW);
    digitalWrite(STARDIR,HIGH);
    Serial.print(String("Set Right:") + rightspeed);
  }
  if (leftspeed==3){
    digitalWrite(PORTHIGH,LOW);
    digitalWrite(PORTMED,LOW);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,LOW);
    Serial.print(String("Set Left:") +leftspeed);
  }
else if (leftspeed==2){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,LOW);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,LOW);
    Serial.print(String("Set Left:") +leftspeed);
}
else if (leftspeed==1){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,HIGH);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,LOW);
    Serial.print(String("Set Left:") +leftspeed);
}
else if (leftspeed==0){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,HIGH);
    digitalWrite(PORTLOW,HIGH);
    digitalWrite(PORTDIR,HIGH);
    Serial.print(String("Set Left:") +leftspeed);
}
  else if (leftspeed==-1){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,HIGH);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,HIGH);
    Serial.print(String("Set Left:") +leftspeed);
  }
  else if (leftspeed==-2){
    digitalWrite(PORTHIGH,HIGH);
    digitalWrite(PORTMED,LOW);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,HIGH);
    Serial.print(String("Set Left:") +leftspeed);
  }
  else if (leftspeed==-3){
    digitalWrite(PORTHIGH,LOW);
    digitalWrite(PORTMED,LOW);
    digitalWrite(PORTLOW,LOW);
    digitalWrite(PORTDIR,HIGH);
    Serial.print(String("Set Left:") +leftspeed);
  }
}


//increase left by 1, if left = 7 and right doesn't = 0, decrease right by 1
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
  Serial.print("Joystick up");
  if (leftspeed < 3){
    leftspeed+=1;
  }
  if (rightspeed < 3){
      rightspeed+=1;
  }
  Serial.print(String("Left:") + leftspeed + String("Right:") +rightspeed);
  setSpeed();
}
void joyDown(){
  Serial.print("Joystick down");
  if (leftspeed > -3){
    leftspeed-=1;
  }
  if (rightspeed > -3){
    rightspeed-=1;
  }
  Serial.print(String("Left:") + leftspeed + String("Right:") +rightspeed);
  setSpeed();
  }
void joyLeft(){
  Serial.print("Joystick left");
  incRight();
  Serial.print(String("Left:") + leftspeed + String("Right:") +rightspeed);
  setSpeed();
}
void joyRight(){
  Serial.print("Joystick right");
  incLeft();
  Serial.print(String("Left:") + leftspeed + String("Right:") +rightspeed);
  setSpeed();
}


// CHECK ME              Function that returns the angle remaining to get to desired bearing. Negative for left, positive for right.
int turnOffset(int chead,int dhead){
  if (chead > dhead){
    if ((chead-dhead) >= 180){
      return(360-chead+dhead);
      }
  }
  else{
    return((chead-dhead)*-1);
    }
  if (chead < dhead){
      if ((dhead-chead) >= 180){
        return((360-dhead+chead)*-1);
        }
      else{
        return(dhead-chead);
        }
    }
}

//CHECK ME               Find arduino function to read current bearing, using khalman filter.
int getBearing(){
  return 69;
}
 
//CHECK ME               Haversine function to return distance between two coordinates
float haversine(float lat1, float lon1, float lat2, float lon2){
  float R = 6372.8; // Earth radius in kilometers
  float dLat = radians(lat2 - lat1);
  float dLon = radians(lon2 - lon1);
  lat1 = radians(lat1);
  lat2 = radians(lat2);
  float a = pow(sin(dLat/2),2) + cos(lat1)*cos(lat2)*pow(sin(dLon/2),2);
  float c = 2*asin(sqrt(a));
  return R * c * 1000;
}
  
//Function to calculate the bearing between two waypoints.
int bearing(float lat1, float lon1, float lat2, float lon2){
  float rlat1 = radians(lat1);
  float rlat2 = radians(lat2);
  float rlon1 = radians(lon1);
  float rlon2 = radians(lon2);
  float dlon = radians(lon2-lon1);
  float b = atan2(sin(dlon)*cos(rlat2),cos(rlat1)*sin(rlat2)-sin(rlat1)*cos(rlat2)*cos(dlon)); // bearing calc
  float bd = degrees(b);
  float bn = (bd+360 % 360); // the bearing remainder and final bearing
  return bn;
}
  
//CHECK ME                Function to return the closest waypoint to current position
int findClosest(){
        return 1;
}
//CHECK ME                 Set the speed and direction based on turn offset
void autoSpeed(){
  
  }
  















void loop(){
      if (digitalRead(AUTOMAN)==LOW){
        motorsOff();
        Serial.print("raftBerry manual mode");
        leftspeed = 0;
        rightspeed = 0;
        setSpeed();
        while(digitalRead(AUTOMAN)==LOW){
          if(digitalRead(SHUTDOWN)==LOW){
            emergencyStop();
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
          delay(500);
        }
}
}


