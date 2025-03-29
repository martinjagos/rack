---
title: Modul pro kontrolu teploty a vlhkosti
layout: default
nav_order: 5
---

# Modul pro kontrolu teploty a vlhkosti

---

## **Příprava**

- Budete potřebovat modely:
    - *modul_fan_front*
    - 2x *assets_module_mount*
{: .step}

- Dále budete potřebovat materiály:
    - lepidlo
    - 12x závitové vložky M3x3
    - 5x závitové vložky M2,5x4
    - 5x šrouby M2,5x7
    - 4x šrouby M3x20
    - 8x šrouby M3x8 se zkosenou hlavou
    - 47g filamentu
{: .step}

- Použitá elektronika:
    - [ESP6866 NoceMCU V3 WiFi](https://www.amazon.com/YEJMKJ-Wireless-Development-Compatible-Micropython/dp/B0CDRMPHPW)
    - [SHT40 Senzor teploty a vlhkosti](https://www.amazon.com/5MNG0Y8-Temperature-Humidity-Sensor-Interface/dp/B0DV3M6NTT)
    - [Větrák Noctua NF-A4x10 5V PWM](https://www.amazon.com/Noctua-NF-A4x10-5V-PWM-Premium/dp/B07DXS86G7)
    - 4x Propojovací kabel 10cm samice-samice
    - 3x Propojovací kabel 10cm samec-samice

- Použité nástroje:
    - pájecí stanice
    - šroubovák
{: .step}

---

## **Krok 1:** Tisk
![alt](/images/fan_print1.png){: .col}
- Položte modely na tiskovou podložku tak, jak je ukázané na obrázku.
{: .col}
<br style="clear: left;" />

---

## **Krok 2:** Závitové vložky
![alt](/images/P1470459.JPG){: .col}
- Přidejte 5 závitových vložek M2,5x4 (na obrázku vpravo)
- Přidejte 4 závitové vložky M3x3 na místo větráku (na obrázku vlevo)
{: .col}
<br style="clear: left;" />

![alt](/images/P1470460.JPG){: .col}
- Zaveďte 4 závitové vložky na stranu modelu 
- Stejně zopakujte i na druhé straně
{: .col}
<br style="clear: left;" />

---

## **Krok 3:** Instalace elektroniky
![alt](/images/P1470462.JPG){: .col}
- Přidělejte větrák čtyřmi šrouby M3x20, dejte si pozor, na polohu větráku
- Přidělejte senzor teploty sřrouby M2,5x7 podle obrázku
- Přidělejte mikrokotroler pomocí tří šroubů M2,5x7, aby konektor směřoval od senzoru
{: .col}
<br style="clear: left;" />

---

## **Krok 4:** Zapojení
![alt](/images/P1470465.JPG){: .col}
- Propojte piny senzoru následovně (číslování je na obrázku od horního pinu):
    - 1 -> 3v3
    - 2 -> GND
    - 3 -> D1
    - 4 > D2
- Propojte piny větráku následovně (barvy kabelu vidíte před konektorem větráku):
    - Černý kabel -> GND
    - Žlutý kabel -> VUSB
    - Modrý kabel -> D5
- Volné kabely připevněte pomocí stahovacích pásků podle, jak na obrázku
{: .col}
<br style="clear: left;" />

---

## **Krok 5:** Zprovoznění
![alt](/images/fan_thingspeak.png){: .col}
- Doporučuji použít platformu ThingSpeak, pro kterou je napsaný skript, plaftorma je bezplatná
- Vytvořte si účet na ThingSpeaku a vytvořte váš kanál přes kliknutím na tlačítko New Channel na stránce https://thingspeak.mathworks.com/channels
- Pojmenujte si váš kanál, do kolonky Field 1 napište např. Teplota a do kolonky Field 2 napiště např. Vlhkost
{: .col}
<br style="clear: left;" />

Nahrajte na mikrokontroler následující skript:
{: .step}

```c++

#include "ThingSpeak.h"
#include <ESP8266WiFi.h>
#include "Adafruit_SHT4x.h"

#define SECRET_SSID "<SSID VAŠÍ BEZDRÁTOVÉ SÍTĚ>"
#define SECRET_PASS "<HESLO VAŠÍ BEZDRÁTOVÉ SÍTĚ>"

#define SECRET_CH_ID <ID KANÁLU>
#define SECRET_WRITE_APIKEY "<API KLÍČ>"

char ssid[] = SECRET_SSID;
char pass[] = SECRET_PASS;
WiFiClient  client;

unsigned long myChannelNumber = SECRET_CH_ID;
const char * myWriteAPIKey = SECRET_WRITE_APIKEY;

const int pwmPin = D5;
const int pwmFrequency = 1000;
const int pwmResolution = 8;

Adafruit_SHT4x sht4 = Adafruit_SHT4x();

void setup() {
  delay(10000);
  Serial.begin(115200);
  Serial.println("Adafruit SHT4x test");
  if (! sht4.begin()) {
    Serial.println("Couldn't find SHT4x");
    while (1) delay(1);
  }
  sht4.setPrecision(SHT4X_HIGH_PRECISION);
  sht4.setHeater(SHT4X_NO_HEATER);

  pinMode(pwmPin, OUTPUT);
  analogWriteFreq(pwmFrequency);

  WiFi.mode(WIFI_STA); 

  ThingSpeak.begin(client);
}

void loop() {

  if(!WiFi.isConnected()){
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(SECRET_SSID);
    while(!WiFi.isConnected()){
      WiFi.begin(ssid, pass);
      Serial.print(".");
      delay(10000);     
    } 
    Serial.println("\nConnected.");
  }

  sensors_event_t humidity, temp;

  uint32_t timestamp = millis();
  sht4.getEvent(&humidity, &temp);
  timestamp = millis() - timestamp;

  float t = temp.temperature;
  float h = humidity.relative_humidity;

  ThingSpeak.setField(1, t);
  ThingSpeak.setField(2, h);

 int x = ThingSpeak.writeFields(myChannelNumber, myWriteAPIKey);

  if(x == 200){
    Serial.println("Channel update successful.");
    Serial.print(F("Humidity: "));Serial.print(h);Serial.print(F("%  Temperature: "));Serial.print(t);Serial.print(F("°C "));
  }
  else{
    Serial.println("Problem updating channel. HTTP error code " + String(x));
  }

  if(t < 25){
    analogWrite(pwmPin, 0);
    Serial.print(" Fan speed: 0%");
  }
  if((t >= 25 ) && (t < 30)){
    analogWrite(pwmPin, 128);
    Serial.print(" Fan speed: 50%");
  }
  if((t >= 30 ) && (t < 40)){
    analogWrite(pwmPin, 190);
    Serial.print(" Fan speed: 75%");
  }
  if((t >= 40)){
    analogWrite(pwmPin, 255);
    Serial.print(" Fan speed: 100%");
  }

  delay(15000);
}

```

- Změňte proměnnou *SECRET_SSID* na SSID vaší bezdrátové sítě, *SECRET_PASS* na heslo vaší bezdrátové sítě, *SECRET_CH_ID* na ID vašeho kanálu na ThingSpeak
- V nastavení vašeho kanálu na ThingSpeak přejděte do kolonky API Keys a zkopírujte Write API Key, ten poté přidejte do proměnné *SECRET_WRITE_APIKEY*
{: .step}


