/*
Adafruit Arduino - Lesson 10. Simple Sounds
*/

int speakerPin = 12;

int tones [] = {117, 147, 156, 175, 196, 208, 233, 262};
//              233, 294, 311, 349, 392, 415, 466, 523
//               Bb   D    Eb   F    G    Ab   Bb   C
//               0    1    2    3    4    5    6    7
  
void setup()
{
  // Do you want to build a snowman
    digitalWrite(speakerPin, HIGH);
    tone(speakerPin, tones[2]); 
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[0]);
    delay(250);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[3]);
    delay(500);
    tone(speakerPin, tones[4]);
    delay(1000);
    noTone(speakerPin);
    delay (500);
    
//Come on let's go and play
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[0]);
    delay(250);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[3]);
    delay(1250);
    noTone(speakerPin);
    delay (500);

//I never see you anymore
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[0]);
    delay(250);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[5]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (400);

//Come out the door
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[5]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (400);

//It's like you've gone away
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[0]);
    delay(250);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[6]);
    delay(2250);
    noTone(speakerPin);
    delay (400);

//We used to be best buddies
    tone(speakerPin, tones[6]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[6]);
    delay(250);
    tone(speakerPin, tones[5]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[5]);
    delay(250);
    tone(speakerPin, tones[6]);
    delay(500);
    tone(speakerPin, tones[2]);
    delay(1000);
    noTone(speakerPin);
    delay (250);
    
//And now we're not
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[3]);
    delay(500);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[2]);
    delay(500);
    noTone(speakerPin);
    delay (300);
    
//I wish you would tell me why?
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(500);
    tone(speakerPin, tones[3]);
    delay(250);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[3]);
    delay(500);
    tone(speakerPin, tones[4]);
    delay(500);
    tone(speakerPin, tones[7]);
    delay(2250);
    noTone(speakerPin);
    delay (250);
    
//Do you want to build a snowman?
    tone(speakerPin, tones[2]); 
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[0]);
    delay(250);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[3]);
    delay(500);
    tone(speakerPin, tones[4]);
    delay(1000);
    noTone(speakerPin);
    delay (500);
    
//It doesn't have to be a snowman
    tone(speakerPin, tones[2]); 
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    noTone(speakerPin);
    delay (10);
    tone(speakerPin, tones[2]);
    delay(250);
    tone(speakerPin, tones[4]);
    delay(250);
    tone(speakerPin, tones[3]);
    delay(500);
    tone(speakerPin, tones[2]);
    delay(1000);
    noTone(speakerPin);
    delay (500);
    
//Okay, bye
    tone(speakerPin, tones[2]);
    delay(500);
    tone(speakerPin, tones[1]);
    delay(500);
    tone(speakerPin, tones[2]);
    delay(1500);
    noTone(speakerPin);
    delay (500);
}

void loop()
{
}

