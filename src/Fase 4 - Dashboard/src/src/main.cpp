#include <Arduino.h>
#include <DHT.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);
#define DHTPIN 15
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

#define PH_SENSOR 34
#define POTASSIUM_SENSOR 12
#define PHOSPHORUS_SENSOR 14
#define PUMP 16

#define BUTTON_PIN 4
int currentScreen = 0;
unsigned long lastDebounce = 0;
const unsigned long debounceDelay = 200;

void sensoresRead();
void controlarIrrigacao(); 
void displayLCD();
void checkButton();
void serialPlotter();

float humidity, temperature, phState;
String potassium_value, phosphorus_value;
String pumpStatus = "";

unsigned long lastTime = 0;
const long interval = 500;

void setup() {
  Serial.begin(115200);

  pinMode(PH_SENSOR, INPUT);
  pinMode(POTASSIUM_SENSOR, INPUT);
  pinMode(PHOSPHORUS_SENSOR, INPUT);
  pinMode(PUMP, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  lcd.init();
  lcd.backlight();
  dht.begin();

  lcd.setCursor(0, 0);
  lcd.print("== FARM SOLUTIONS ==");
  delay(2000);
  lcd.clear();
}

void loop() {
  unsigned long currentTime = millis();

  if (currentTime - lastTime >= interval) {
    lastTime = currentTime;

    sensoresRead();
    controlarIrrigacao(); 
    displayLCD();
    checkButton();
    serialPlotter();
  }
}

void sensoresRead() {
  humidity = dht.readHumidity();
  temperature = dht.readTemperature();

  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Erro na leitura do DHT22");
    return;
  }

  int phRaw = analogRead(PH_SENSOR);
  phState = map(phRaw, 0, 4095, 0, 14);

  potassium_value = digitalRead(POTASSIUM_SENSOR) ? "ALTO" : "BAIXO";
  phosphorus_value = digitalRead(PHOSPHORUS_SENSOR) ? "ALTO" : "BAIXO";
}

void controlarIrrigacao() {
  const int threshold = 50;
  if (humidity < threshold) {
    digitalWrite(PUMP, HIGH);
    pumpStatus = "BOMBA ACIONADA";
  } else {
    digitalWrite(PUMP, LOW);
    pumpStatus = "BOMBA DESLIGADA";
  }
}

void displayLCD() {
  lcd.clear();
  switch (currentScreen) {
    case 0:
      lcd.setCursor(0, 0); lcd.print("== FARM SOLUTIONS ==");
      lcd.setCursor(0, 2); lcd.print("Temp: "); lcd.print(temperature); lcd.print(" C");
      lcd.setCursor(0, 3); lcd.print("Umid: "); lcd.print(humidity); lcd.print(" %");
      break;

    case 1: 
      lcd.setCursor(0, 0); lcd.print("== FARM SOLUTIONS ==");
      lcd.setCursor(0, 2); lcd.print("pH: "); lcd.print(phState, 1);
      lcd.setCursor(0, 3); lcd.print(pumpStatus);
      break;

    case 2: 
      lcd.setCursor(0, 0); lcd.print("== FARM SOLUTIONS ==");
      lcd.setCursor(0, 2); lcd.print("POT: "); lcd.print(potassium_value);
      lcd.setCursor(0, 3); lcd.print("FOS: "); lcd.print(phosphorus_value);
      break;
  }
}

void checkButton() {
  static bool lastButtonState = HIGH;
  bool currentButtonState = digitalRead(BUTTON_PIN);

  if (lastButtonState == HIGH && currentButtonState == LOW && millis() - lastDebounce > debounceDelay) {
    currentScreen = (currentScreen + 1) % 3;
    lastDebounce = millis();
  }

  lastButtonState = currentButtonState;
}

void serialPlotter() {
  Serial.print("Temperatura: ");
  Serial.print(temperature);
  Serial.print("  Umidade: ");
  Serial.println(humidity);
}
