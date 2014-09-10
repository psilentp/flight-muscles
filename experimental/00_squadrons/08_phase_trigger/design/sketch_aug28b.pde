int camPin = 0;
int delayPin = 3;
int delayTime = 20;
int exposeTime = 1;
int wbSyncPin = 5; //5v pin
int timeoutMicros = 13888; //72Hz
float maxDelayVal = 1910;
HardwareTimer timer(3);

///volatile int wbPeriods[10];
volatile long lastTrigger;
volatile long wbPeriod;
volatile int WBtrigState = false;
float avePeriod;
const int LMSIZE = 10;
const int LMSIZE_PER = 10;
int microseconds_per_millisecond = 1000;
float delayPeriodFraction = 0.1;
int count = 0;
int lastCamTrigger;

void setup() {
    // Set up the built-in LED pin as an output:
    pinMode(BOARD_LED_PIN, OUTPUT);
    pinMode(camPin,OUTPUT);
    pinMode(delayPin,INPUT_ANALOG);
    attachInterrupt(wbSyncPin, getWBtime, FALLING);
    SerialUSB.begin();
        // Have the timer repeat every 20 milliseconds
    //
    //#timer.setPeriod(20 * microseconds_per_millisecond);
}

void loop() {
    
    if(WBtrigState){
      avePeriod = runningAverageWB(wbPeriod);
      delayTime = delayPeriodFraction*avePeriod;
      //SerialUSB.println(delayTime);
      WBtrigState = false;
      delayMicroseconds(delayTime);
      lastCamTrigger = micros();
      digitalWrite(camPin,HIGH);
      digitalWrite(BOARD_LED_PIN,HIGH);
      delayMicroseconds(100);
      digitalWrite(camPin,LOW);
      digitalWrite(BOARD_LED_PIN,LOW);
    }

    if (count > 1000){
      int delayVal = analogRead(delayPin);
      delayVal = runningAveragePER(delayVal);
      delayPeriodFraction = delayVal/maxDelayVal;
      //SerialUSB.println(delayTime);
      count = 0;
    }
    count += 1;
    
    int timeoutStatus = micros()-lastCamTrigger;
    if (timeoutStatus > timeoutMicros){
      lastCamTrigger = micros();
      digitalWrite(camPin,HIGH);
      digitalWrite(BOARD_LED_PIN,HIGH);
      delayMicroseconds(100);
      digitalWrite(camPin,LOW);
      digitalWrite(BOARD_LED_PIN,LOW);
  }
}

void getWBtime(){
  long currentTrigger = micros();
  wbPeriod = currentTrigger-lastTrigger;
  lastTrigger = currentTrigger;
  WBtrigState = true;
}
  
float runningAverageWB(int M)
{
  static int LM_WB[LMSIZE];
  static byte index = 0;
  static float sum = 0;
  LM_WB[index] = M;
  sum = 0;
  for (int i=0;i<LMSIZE;i++){
    sum += LM_WB[i];
  }
  index += 1;
  if (index >= LMSIZE) index = 0;
  return sum / LMSIZE;
}

float runningAveragePER(int M)
{
  static int LM_PER[LMSIZE_PER];
  static byte index_PER = 0;
  static float sum_PER = 0;
  LM_PER[index_PER] = M;
  sum_PER = 0;
  for (int i=0;i<LMSIZE_PER;i++){
    sum_PER += LM_PER[i];
  }
  index_PER += 1;
  if (index_PER >= LMSIZE_PER) index_PER = 0;
  return sum_PER / LMSIZE_PER;
}
