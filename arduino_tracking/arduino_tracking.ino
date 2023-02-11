#define trigPin1 3
#define echoPin1 2
#define trigPin2 4
#define echoPin2 5
#define trigPin3 7
#define echoPin3 8
#define trigPin4 9
#define echoPin4 10
#define inputPin 12
#define trigPin5 11
#define echoPin5 13

long duration, distance, SensorA,SensorB,SensorC,SensorD, SensorE;
int read, prevread;
char input;
String my_name;
String prev;

void setup()
{
Serial.begin (9600);
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT);
pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT);
pinMode(trigPin3, OUTPUT);
pinMode(echoPin3, INPUT);
pinMode(trigPin4, OUTPUT);
pinMode(echoPin4, INPUT);
pinMode(trigPin5, OUTPUT);
pinMode(echoPin5, INPUT);
pinMode(inputPin, INPUT);

}

void loop() {
   if(Serial.available()){
           my_name = Serial.readStringUntil('\n');
           if(my_name != "" && my_name != prev){
             readABCD();
             prev = my_name;
           }
           prev = "";

       }
}

void readABCD(){
  SonarSensor(trigPin1, echoPin1);
  SensorA = distance;
  SonarSensor(trigPin2, echoPin2);
  SensorB = distance;
  SonarSensor(trigPin3, echoPin3);
  SensorC = distance;
  SonarSensor(trigPin4, echoPin4);
  SensorD = distance;
  SonarSensor(trigPin5, echoPin5);
  SensorE = distance;


  Serial.print(SensorA);
  Serial.print(",");
  Serial.print(SensorB);
  Serial.print(",");
  Serial.print(SensorC);
  Serial.print(",");
  Serial.print(SensorD);
  Serial.print(",");
  Serial.println(SensorE);

}

void SonarSensor(int trigPin,int echoPin)
{
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1;

}