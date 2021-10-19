#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>

#define  MOISTURE_THRESHOLD     55  
const char* wifi_ssid = "IoTTest";             // SSID
const char* wifi_password = "IoTTest123";         // WIFI
const char* apiKeyIn = "moisturedata";     
const unsigned int writeInterval = 5000; 

String host = "http://192.168.1.27:5000";

ESP8266WiFiMulti WiFiMulti;

int moisture_Pin= 0; 
int moisture_value= 0, moisture_state = 0xFF;

void setup() {

  Serial.begin(115200);
  Serial.println("*****************************************************");
  Serial.println("********** Program Start : Soil Moisture monitoring using ESP8266 and AskSensors IoT cloud");
  Serial.println("Wait for WiFi... ");
  Serial.print("********** connecting to WIFI : ");
  Serial.println(wifi_ssid);
  WiFi.begin(wifi_ssid, wifi_password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("-> WiFi connected");
  Serial.println("-> IP address: ");
  Serial.println(WiFi.localIP());
 
}

void loop() {

    Serial.print("MOISTURE LEVEL : ");
    moisture_value= analogRead(moisture_Pin);
    moisture_value= moisture_value/10;
    Serial.println(moisture_value);
   if(moisture_value > MOISTURE_THRESHOLD) moisture_state = 0;
   else moisture_state = 1;
   

  if (WiFi.status() == WL_CONNECTED){

        HTTPClient http;
        WiFiClient client;

        Serial.print("[HTTP] begin...\n");
        
        String url = "";
        url += host;
        url += "/api/";
        url += apiKeyIn;
        url += "?moisture=";
        url += moisture_value;
        
        Serial.print("********** requesting URL: ");
        Serial.println(url);
        
        http.begin(client, url);

        Serial.println("> Soil moisture level and state were sent to Peter");

        Serial.print("[HTTP] GET...\n");
        
        int httpCode = http.GET();

        if(httpCode > 0) {
            
            Serial.printf("[HTTP] GET... code: %d\n", httpCode);

            if(httpCode == HTTP_CODE_OK) {
                String payload = http.getString();
                Serial.println(payload);
            }
        } else {
            Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
        }

        http.end();

        Serial.println("********** End ");
        Serial.println("*****************************************************");
    }

    delay(writeInterval);
}