#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266HTTPClient.h>

#define  MOISTURE_THRESHOLD     55  
const char* wifi_ssid = "SSID"; // SSID
const char* wifi_password = "WIFI_PASSWORD"; // WIFI_PASSWORD 
const char* serverIP = "SERVER_IP"; //SERVER_IP    
const unsigned int writeInterval = 5000; // defines how often updates are sent to the server. 1000 = 1 second
const char* apiKeyIn = "moisturedata";

String host = "http://";

ESP8266WiFiMulti WiFiMulti;

int moisture_Pin= 0; 
int moisture_value= 0, moisture_state = 0xFF;

void setup() {

    Serial.begin(115200);
    Serial.println("*****************************************************");
    Serial.println("********** Program Start : Soil Moisture monitoring using ESP8266");
    Serial.println("Wait for WiFi... ");
    Serial.print("********** connecting to WIFI : ");
    Serial.println(wifi_ssid);

    // Start the Wifi connection
    WiFi.begin(wifi_ssid, wifi_password);
    // Wait until the client is connected to the Wifi
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.println("-> WiFi connected");
    // Print the IP addrss of the ESP
    Serial.println("-> IP address: "); 
    Serial.println(WiFi.localIP());
    
    // Finishng the host IP for updates
    host += serverIP;
    host += ":5000";

}

void loop() {
    // Read the Moisture Value from the PIN and Print it
    Serial.print("MOISTURE LEVEL : ");
    moisture_value = analogRead(moisture_Pin);
    moisture_value = moisture_value/10;
    Serial.println(moisture_value);

    // Change the Moisture state if a Threshhold is reached
    // Moisture state is currently not implemented in the Server and therefore not send
    if(moisture_value > MOISTURE_THRESHOLD) moisture_state = 0;
    else moisture_state = 1;
   
    // Check if the ESP has a valid Wifi connection
    if (WiFi.status() == WL_CONNECTED){

        HTTPClient http;
        WiFiClient client;

        Serial.print("[HTTP] begin...\n");
        
        // Construct the URL for the request
        String url = "";
        url += host;
        url += "/api/";
        url += apiKeyIn;
        url += "?moisture=";
        url += moisture_value;
        
        Serial.print("********** requesting URL: ");
        Serial.println(url);
        
        // Sending the Request to the Server
        http.begin(client, url);

        Serial.println("> Soil moisture level and state were sent to the Server");

        Serial.print("[HTTP] GET...\n");
        
        // Get the returning HTTP Code
        int httpCode = http.GET();

        // Check if its a valid Code
        if(httpCode > 0) {
            
            Serial.printf("[HTTP] GET... code: %d\n", httpCode);

            if(httpCode == HTTP_CODE_OK) {
                String payload = http.getString();
                Serial.println(payload);
            }
        } else {
            // Output the HTTP Error when the request Fails
            Serial.printf("[HTTP] GET... failed, error: %s\n", http.errorToString(httpCode).c_str());
        }

        http.end();

        Serial.println("********** End ");
        Serial.println("*****************************************************");
    }
    // Delay the next Call of the Loop
    delay(writeInterval);
}