# KaindorfThings

IoT-Schaustück für Bildungsmesse

Autoren:

+ Daniel Brinar: [@Shadow17402](https://github.com/Shadow17402)
- Peter Gottlieb: [@gotped17](https://github.com/gotped17)

## Abstract

Wir hatten den Auftrag, ein Internet of Things-Schaustück für die SBIM und BEST3 zu entwickeln. Hardware wurde von der HTBLA Kaindorf bereitgestellt. Aufgrund des Zeitdrucks entschieden wir uns, eine Minimalidee umzusetzen. Da wir vor einigen Jahren bereits eine IKEA Tradfri angesteuert haben, wollten wir dieses Feature auf jeden Fall implementieren. Und weil wir uns nicht mit Rust auskennen, schrieben wir den Server schnell in Python mit Flask nach. Außerdem wollten wir ein weiteres Feature implementieren, um möglicherweise die Lampe über einen anderen Weg anzusteuern. Also implementierten wir einen Feuchtigkeitssensoren, der über einen ESP8266 die Messdaten an den Server auf dem Raspberry PI sendet. Fallen diese Daten unter einen Grenzwert, wird die Lampe aktiviert.

## Hardware

Für den Aufbau des Modells in seiner aktuellen Ausführung (Stand 14.10.2021) wird folgende Hardware benötigt:

+ 1 ESP8266
+ 1 Feuchtigkeitssensor
+ 1 Raspberry PI 4
+ 1 Tradfri Glühbirne
+ 1 Tradfri Fernbedienung
+ 1 Tradfri Gateway
+ 1 Router mit eingebautem Switch (Wir nutzten einen Buffalo)

## Software

Im Ordner [app](https://github.com/BriGot17/KaindorfThings/tree/master/app) befindet sich der Sourcecode für den Webserver, welcher auf dem Raspberry PI ausgeführt wird. Zuvor muss allerdings mit der Python library [pytradfri](https://github.com/home-assistant-libs/pytradfri) ein Nutzername und PSK mit dem Gateway erstellt und in der Datei core.py eingesetzt werden. Danach kann der Server gestartet werden. Auf dem Raspberry PI sollte dann unter *localhost:5000/* das Webinterface erreichbar sein.

Im Ordner [Moisture Sensor](https://github.com/BriGot17/KaindorfThings/tree/master/Moisture_Sensor) befindet sich der Code der auf dem ESP8266 ausgeführt werden soll. Je nach Situation muss zuvor darin die IP des Gateways geändert werden. Das deployen des Codes auf dem ESP funktioniert am einfachsten mit der VS Code Erweiterung platform.io.

## Aufsetzen

Das Aufsetzen wird in drei verschiedene Teile aufgeteilt: Aufsetzen des Gateways samt Lampe, Einrichten des Webinterfaces und Aufsetzen des Sensors.

### Gateway

Für das Aufsetzen des Gateways braucht man die IKEA Home App. Für den normalen Betrieb wird diese aber nicht benötigt.
    1. IKEA Home App installieren
    2. Tradfri Gateway per LAN-Kabel ins Netzwerk hängen
    3. Mit dem Handy ins gleiche Netzwerk verbinden
    4. IKEA Home App öffnen und darin nach Gateway suchen
    5. Den Schritten in der App folgen
    6. Funktionstest mit der IKEA Fernbedienung
  Damit sollte das Gateway samt Lampe einsatzbereit sein.

### Webinterface

Das Webinterface wird auf dem Raspberry PI als Webserver deployed. Der Server dient gleichzeitig als API für den Sensor.

1. Dieses Github Repository klonen

2. Sicher gehen, das `Libtools` und `Autoconf` installiert sind. Falls nicht: `sudo apt insatll libtools autoconf`

3. Die Datei [install-coap-client.sh](https://github.com/BriGot17/KaindorfThings/blob/master/install-coap-client.sh) ausführen

4. Via `coap-client` einen neuen Nutzer und PSK mit dem Gateway ausmachen
   
   `coap-client -m post -u "Client_identity" -k "<Gateway Security Code>" -e "{\"9090\":\"<Nutzername>\"}" "coaps://<Gateway IP>:5684/15011/9063"`

5. Command `coap-client` mit Beispielen aus Datei [coapcommands.txt](https://github.com/BriGot17/KaindorfThings/blob/master/coapcommands.txt) testen. Nicht vergessen den Nutzernamen und den PSK zu tauschen!

6. Fehlende Python dependencies (Im Normalfall nur Flask) installieren: `python3 pip install flask`

7. Die Datei `/app/core.py` starten mit`python3 core.py`

8. `Localhost:5000` im Browser ansurfen. Es sollte nun das Webinterface aufscheinen.

### Sensor

Um den ESP zu benutzen, muss zuerst der Code auf ihm deployed werden. Dies geschieht am Einfachsten mit der VSCode Erweiterung `platform.io`.

1. `platform.`io in VSCode installieren

2. Code für Sensor in VSCode öffnen

3. In der [main.cpp](https://github.com/BriGot17/KaindorfThings/blob/master/Moisture_Sensor/src/main.cpp) müssen Parameter eingegeben werden das er sich zum Wifi verbindet und an   die richtige Server IP schickt.
   
   ```cpp
   const char* wifi_ssid = "SSID"; // SSID
   const char* wifi_password = "WIFI_PASSWORD"; // WIFI_PASSWORD 
   const char* serverIP = "SERVER_IP"; //SERVER_IP    
   const unsigned int writeInterval = 5000; // defines how often updates are sent to the server. 1000 = 1 second 
   ```

4. Mit PlatformIO kann nun der Code auf den ESP geladen werden wenn dieser angesteckt ist.
   
   ![alt text](https://github.com/BriGot17/KaindorfThings/blob/master/Readme_Pics/PIO_Upload.png?raw=true)
   
   Sollte der ESP nicht gefunden werden stellen sie bitte sicher das der ESP auch von PlatformIO erkannt wurde, sollte dies nicht der Fall sein überprüfen Sie ob die richtigen          [Treiber](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) für das Gerät installiert wurden. Sollte es dennoch nicht funktionieren überprüfen sie ob in der          [platformio.ini](https://github.com/BriGot17/KaindorfThings/blob/master/Moisture_Sensor/platformio.ini) der Richtige Upload_Port angegeben wurde.

5. Nach dem Upload sollte der ESP laufen solange er Strom hat. Es reicht den ESP am Raspberry Pi            anzuschließen.
   
   #### Verkabelung
   
   Ganzes Setup
   
   ![alt text](https://github.com/BriGot17/KaindorfThings/blob/master/Readme_Pics/Setup_ESP.jpg?raw=true)
   
   Verkabelung am ESP
   
   ![alt text](https://github.com/BriGot17/KaindorfThings/blob/master/Readme_Pics/Verkabelung_ESP.jpg?raw=true)
   
   Controller => ESP
   
   (GND) => (GND)
   
   (VCC) => (3V3)
   
   (A0) => (A0)

## Endpoints

`/api/on`: Schaltet die Lampe ein

`/api/off`: Schaltet die Lampe aus

`/api/on/level?lightlevel={}`: Setzt Helligkeit auf angegebenen Wert

`/api/moisturedata`: Sensorwerte des Feuchtigkeitssensors hierher senden. Bei Werten unter 60 wird die Lampe eingeschaltet

`/api/moistureout`: Gibt den aktuell gespeicherten Feuchtigkeitswert zurück

## Known Issues

+ Sollte der Webserver/die API um Funktionen erweitert werden, darauf achten, dass nicht zu schnell zu viele coap Requests an das Ikea Gateway verschickt, das verschluckt sich sonst.
+ Bei einem Aufbau auf SBIM/BEST3 oder sonstigem großen Event --> Beim Router WLAN Channel auf 13 setzen, um Überschneidungen mit anderen Hotspots auszuweichen. Channel 14 auf 
  jeden Fall vermeiden, der Raspberry PI kann keinen Channel 14.
+ Nach gewisser Zeit hat die Lampe von selbst angefangen zu blinken. Es könnte hier entweder an der Lampe oder am Gateway liegen. Anscheinend hat sich beim neusynchonisieren eine neue Gruppe gebildet und dabei eine andere group-ID angenommen. Das heißt, dass bei einem Resync die group-ID neu abgefragt und in den Source Code eingetragen werden muss.
+ Der Disco-Modus funktioniert nicht einwandfrei. Es kann dazu kommen, dass sich das Gateway verschluckt oder das generell die Request zu langsam bearbeitet werden.

## TODO

+ Es soll möglich sein, die IKEA device bzw. group-ID automatisch abzufragen und dynamisch zu benutzen, damit im Fall, dass sich alles in eine neue Gruppe verschiebt oder es in einem neuen System eingesetzt wird, nicht jedes mal der Source Code verändert werden muss damit es funktioniert.
+ Die Lampe soll zum Blinken gebracht werden. Der letzte Versuch wurde herausgelöscht, da er das Gateway überfordert hat und die Lampe sich damit selbstständig gemacht hat.

## References und Useful Links

Hier sind einige Links und andere Github repositories, die wir während des Erstellens des Schaustücks benutzt haben

#### Gateway communication

+ [ikea-tradfri-coap-docs](https://github.com/glenndehaan/ikea-tradfri-coap-docs) von [@glenndehaan](https://github.com/glenndehaan/): Eine Sammlung an coap Commands für IKEA Tradfri
+ [pytradfri](https://github.com/home-assistant-libs/pytradfri)-module: Python module für einfachere Interaktion via Pyhon, wurde anfänglich benutzt und gibt einige Denkansätze
+ [pytradfri-rest](https://github.com/fjaderboll/pytradfri-rest): Pytradfri als REST-API. Wurde nicht benutzt, könnte aber viel Arbeit ersparen.
