//#include <DueTimer.h>

/*
  Blink
  Turns on an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the Uno and
  Leonardo, it is attached to digital pin 13. If you're unsure what
  pin the on-board LED is connected to on your Arduino model, check
  the documentation at http://arduino.cc

  This example code is in the public domain.

  modified 8 May 2014
  by Scott Fitzgerald
 */

const bool TRIGGERED = true;
const bool UNTRIGGERED = false;

const bool TIMEOUT = true;
const bool READY = false;

const int READOUTMICROS = 2000;//camera won't be ready for 2ms untill after pulse

const int TIMEOUTMICROS = 8000; //wait 6ms for wingbeat if not freetrigger at 50Hz
const int PULSEDURATION = 500; //10 ms exposure
const int PULSEDURATION = 100; //10 ms exposure
const int CAMPIN = 24;
const int LEDPIN = 22;
const int TRIGGERPIN = 52;
const float PULSEPHASE = 0.4;
const int TIMEBUFFERSIZE = 5;
const int MICROSPERSEC = 1000*1000;
//const int MAXPERIOD = 6150; //160 Htz
const int MAXPERIOD = 7500; //160 Htz

int timeout_in = 0;
int framestart = 0;
int trigger_wb_in = 0;
int current_time = 0;
volatile bool wbstate = UNTRIGGERED;
volatile bool timeoutstate = READY;
volatile int pulsecount = 0;
long timequeue [TIMEBUFFERSIZE];
int pulsedelay = 0;
float wbperiod = 5000;

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin 13 as an output.
  pinMode(CAMPIN, OUTPUT); //led_pin
  pinMode(LEDPIN, OUTPUT); //camera pin
  attachInterrupt(TRIGGERPIN,wbtrigger,FALLING);
}

void loop() {  
    framestart = micros();
    digitalWrite(CAMPIN, HIGH);
    delayMicroseconds(500);
    digitalWrite(CAMPIN, LOW);
    timeout_in = micros() + (18000 - PULSEDURATION);
    
    pulsedelay = (int) wbperiod*PULSEPHASE;
    trigger_wb_in = micros() + 6000; //micros() + (MAXPERIOD-(pulsedelay+PULSEDURATION));
    //trigger_wb_in = micros() + MAXPERIOD;
    wbstate = UNTRIGGERED;
    while(pulsecount <3)
    {
      if (micros() > timeout_in)
      {
        digitalWrite(LEDPIN, HIGH);
        delayMicroseconds(PULSEDURATION);
        digitalWrite(LEDPIN, LOW);
        break;
      }
      if((wbstate) | (micros()>trigger_wb_in))
      {
        
        //detachInterrupt(TRIGGERPIN);
        wbperiod = ((float)( (timequeue[4] - timequeue[3]) +(timequeue[3] - timequeue[2])+ (timequeue[2] - timequeue[1]) + (timequeue[1] - timequeue[0])))/3.0;
        if ((wbperiod > MAXPERIOD) | (wbperiod <= 0 ))
        {
          wbperiod = MAXPERIOD;
        }
        pulsedelay = (int) wbperiod*PULSEPHASE;
        //pulsedelay = MINPERIOD*PULSEPHASE;
        wbstate = UNTRIGGERED;
        delayMicroseconds(pulsedelay);

        digitalWrite(LEDPIN, HIGH);
        delayMicroseconds(PULSEDURATION);
        digitalWrite(LEDPIN, LOW);
          
        pulsecount++;
        trigger_wb_in = micros() + (MAXPERIOD-(pulsedelay+PULSEDURATION));
        //attachInterrupt(TRIGGERPIN,wbtrigger,FALLING);
      }
    }
    pulsecount = 0;
    current_time = micros();
    if ((22000 - (current_time-framestart)) > 0)
    {
      delayMicroseconds(22000 - (current_time-framestart));
    }
}

void wbtrigger()
{
  wbstate = TRIGGERED;
  logtime();
}

void logtime()
{
  long tmp;
  int i;
  for(i=TIMEBUFFERSIZE-1;i>0;i--)
  {
    tmp = timequeue[i];
    timequeue[i+1] = tmp;
  }
  timequeue[0] = micros();
}

