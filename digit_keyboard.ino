#include <CapacitiveSensor.h>
CapacitiveSensor dig0 = CapacitiveSensor(3,2);
CapacitiveSensor dig1 = CapacitiveSensor(5,4);
CapacitiveSensor dig2 = CapacitiveSensor(7,6);
CapacitiveSensor dig3 = CapacitiveSensor(9,8);
CapacitiveSensor dig4 = CapacitiveSensor(11,10);

int thresholds[5] = {450,450,450,450,450};
int nsamples = 20;
long sensor[5];
boolean state[5];
boolean pressed = false;
long current_time;
int interval = 750;
String output = "";
int counter = 0;

// ------ AUXILIARY FUNCTIONS ------------- // 

// read the sensor values, returns an array
long read_sensors( ) 
{
  sensor[0] = dig0.capacitiveSensor(nsamples);
  sensor[1] = dig1.capacitiveSensor(nsamples);
  sensor[2] = dig2.capacitiveSensor(nsamples);
  sensor[3] = dig3.capacitiveSensor(nsamples);
  sensor[4] = dig4.capacitiveSensor(nsamples);
  delay(10);
  return sensor;
}

void print_states() 
{
  Serial.println("state :");
  Serial.print(state[0]);
  Serial.print(state[1]);
  Serial.print(state[2]);
  Serial.print(state[3]);
  Serial.print(state[4]);
}
// convert the boolean state array into a string (for serial output)
String tostring() 
{
  for (int i=0;i<=4;i++)
  {
    if (state[i])
    {
      output+='1';
    }
    else 
    {
      output+='0';
    }
  }
  return output;
}

// ------ MAIN CODE ------------- // 

void setup() 
{
  Serial.begin(9600);
  pinMode(13,OUTPUT);

}

void loop() 
{
  // read sensor values and store into sensors array (see function)
  read_sensors();

  // for every sensor, check if above threshold
  for (int i=0;i<=4;i++)
  {
    state[i]=sensor[i]>thresholds[i];
    // if any one of them is above threshold set pressed to true
    if (state[i])
      {
      pressed=true;
      }
    // if by the end of the loop, a button has been pressed, start time window
    if (pressed && i==4)
    {
      current_time = millis();
      /*Serial.print("[In ");
      Serial.print(counter);
      Serial.println("]: ");*/

    }
  }
  if (pressed)
  
  {
  digitalWrite(13,HIGH);
  //Serial.println("time window is open!");    
  // while [interval], check if any other button is pressed
  while(millis()-current_time < interval)
  {    
    read_sensors();
    for (int i=0;i<=4;i++)
    {
      if (sensor[i]>thresholds[i]) 
      {
        state[i]=true; // if the button is pressed, set its state to true
      }
      
    }
  }
  
  //Serial.println("time window is closed!");
  
    // convert to string and send via serial
    tostring(); 
    //Serial.println("The output is: ");
    Serial.print(output.c_str());
    //Serial.write(output.c_str());
    Serial.flush();
    pressed = false;
    current_time = 0;
    output = "";
    counter++;
    Serial.println("");
    digitalWrite(13,LOW);
  }
}





