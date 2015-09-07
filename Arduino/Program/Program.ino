/*
 * SmartBot Arduino Program
 * version : BETA 0.1b-r1
 * developed by Itay Asayag in Israel
 * 
 * under the Gnu GPLv3 license terms.
 * I and Arduino LLC are not responsible for any damage or loss
 * of data made from either correct or wrong use of this code.
 *
 * Gnu GPLv3 License: http://www.gnu.org/licenses/quick-guide-gplv3.html
 *
 */

const int trigPin = 13;
const int echoPin = 12;

const int RM1 = 7;
const int RM2 = 6;
const int LM1 = 5;
const int LM2 = 4;

const int LmotorSpeedPin =  9;
const int RmotorSpeedPin = 10;

int distanceRsl;

long duration, distance;

const int debugging = 1; //Send Serial Debbugging information back in serial?
                         // 1 is YES 0 is NO

void setup() {
  // Prepare arduino for serial communication.

  // Start serial port at max speed:

  Serial.begin(115200); //Start serial.

  while (!Serial) {
    ; // Waiting for leonardo to connect
  }

  //Set up input and outputs

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);


}

void loop() {
  //Command structure is as follows: ---.---- i.e.: 3 letters command all caps and four letters value
  while (Serial.available()) {

    String serialText = Serial.readString();
    String cmd = serialText.substring(0, 3);
    String value = serialText.substring(4, 7);
    String value2 = serialText.substring(8, 15);

    if (debugging) {
      Serial.println("CMD IS '" + cmd + "'\nVALUE1 IS '"+ value+ "'\nVALUE2 IS '" + value2 + "'" );
    }

    if (cmd == "ANV") { // Send Analog value. ---.-
      int pinnum = value.toInt();
      if (value.toInt() < 0) {
        if (debugging) {
          Serial.println("analog pin number too small");
        }
        break;
      } else if (value.toInt() > 5) {
        if (debugging) {
          Serial.println("analog pin number too big");
        }
        break;
      }

      if (debugging) {
        Serial.println("Sampling pin number " + value);
      }
      int analogReading = analogRead(pinnum);
      if (debugging) {
        Serial.println("Sampled analog pin " + String(value) + " with value of " + (String)analogReading + " .");
      }
    }

    if (cmd == "LMS") { // set Left motor Speed. ---.----
      /*
       * Setting a speed of 0 to 255 is forward
       * while a speed of -255 to 0 is backward
       * to drive forward at speed _Lspeed
       */

      int _Lspeed = value.toInt();
      SetLMotorSpeed(_Lspeed);


    }

    if (cmd == "RMS") { // set Right motor speed. ---.----
      int _Rspeed = value.toInt();
      SetRMotorSpeed(_Rspeed);
    }

    if (cmd == "GDM") { // Get distance Measurement
      Serial.println((String)readDistance());
    }

    if (cmd == "SMS") { // Set motor speeds.
      SetRMotorSpeed(value.toInt());
      SetLMotorSpeed(value2.toInt());
    }
  }
}

int SetRMotorSpeed(int _Rspeed) {
  if (_Rspeed == 0) {
    analogWrite(RmotorSpeedPin, 0);
    digitalWrite(RM1, LOW);
    digitalWrite(RM2, HIGH);
  }

  if (_Rspeed > 0 && _Rspeed < 255) {
    //Forward it is
    analogWrite(RmotorSpeedPin, _Rspeed);
    digitalWrite(RM1, LOW);
    digitalWrite(RM2, HIGH);
  }

  if (_Rspeed > -255 && _Rspeed < 0) {
    //Backward it is
    _Rspeed *= -1; //Turn it to positive for the mechanism to work
    analogWrite(RmotorSpeedPin, _Rspeed);
    digitalWrite(RM1, HIGH);
    digitalWrite(RM2, LOW);
  }
}

int SetLMotorSpeed(int _Lspeed) {
  if (_Lspeed == 0) {
    analogWrite(LmotorSpeedPin, 0);
    digitalWrite(LM1, LOW);
    digitalWrite(LM2, HIGH);
  }

  if (_Lspeed > 0 && _Lspeed < 255) {
    //Forward it is
    analogWrite(LmotorSpeedPin, _Lspeed -60); //rEMOVE THIS IF YOUR TWO MOTORS ARE THE SAME MODEL.
    digitalWrite(LM1, LOW);
    digitalWrite(LM2, HIGH);
  }

  if (_Lspeed > -255 && _Lspeed < 0) {
    //Backward it is
    _Lspeed *= -1; //Turn it to positive for the mechanism to work
    analogWrite(LmotorSpeedPin, _Lspeed -60); // HERE TOO.
    digitalWrite(LM1, HIGH);
    digitalWrite(LM2, LOW);
  }
}

int readDistance() {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);

  //Calculate the distance (in cm) based on the speed of sound.
  distance = duration / 58.2;
  return (distance);
}

