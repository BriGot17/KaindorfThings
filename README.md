# KaindorfThings
IoT-Schaustück für Bildungsmesse

Autoren:
+ Daniel Brinar: [@Shadow17402](https://github.com/Shadow17402)
- Peter Gottlieb: [@gotped17](https://github.com/gotped17)


## Abstract

Wir hatten den Auftrag ein Internet of Things-Schaustück für die SBIM und BEST3 zu entwickeln. Hardware wurde von der HTBLA Kaindorf bereitgestellt.

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

Im Ordner [app](https://github.com/BriGot17/KaindorfThings/tree/master/app) befindet sich der Sourcecode für den Webserver, welcher auf dem Raspberry PI ausgeführt wird.
Zuvor muss allerdings mit der Python library [pytradfri](https://github.com/home-assistant-libs/pytradfri) ein Nutzername und PSK mit dem Gateway erstellt und in der Datei
core.py eingesetzt werden. Danach kann der Server gestartet werden. Auf dem Raspberry PI sollte dann unter *localhost:5000/* das Webinterface erreichbar sein.

Im Ornder <Sensoren> befindet sich der Code der auf dem ESP8266 ausgeführt werden soll. Je nach Situation muss zuvor darin die IP des Gateways geändert werden. Das deployen
des Codes auf dem ESP funktioniert am einfachsten mit der VS Code Erweiterung platform.io. Sollte es dabei unter Windows zu Problemen kommen: Überprüfen, ob die Treiber 
installiert sind.
  
## Aufsetzen

Das Aufsetzen wird in drei verschiedene Teile aufgeteilt: Aufsetzen des Gateways samt Lampe, Einrichten des Webinterfaces und Aufsetzen des Sensors.
  
### Gateway
  
Für das Aufsetzen des Gateways wird die IKEA Home App benötigt. Für den normalen Betrieb wird diese aber nicht benötigt.
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
  4. Command `coap-client` mit Beispielen aus Datei [coapcommands.txt](https://github.com/BriGot17/KaindorfThings/blob/master/coapcommands.txt) testen
  5. Fehlende Python dependencies (Im Normalfall nur Flask) installieren: `python3 pip install flask`
  6. Die Datei `/app/core.py` starten mit`python3 core.py`
  7. `Localhost:5000` im Browser ansurfen. Es sollte nun das Webinterface aufscheinen.
  
### Sensor
  
Um den ESP zu benutzen, muss zuerst der Code auf ihm deployed werden. Dies geschieht am Einfachsten mit der VSCode Erweiterung `platform.io`.
  1. Platform.io in VSCode installieren
  2. Code für Sensor in VSCode öffnen
  3. Mit PlatformIO kann nun der Code auf den ESP geladen werden wenn dieser angesteckt ist. 
     ![alt text](https://github.com/BriGot17/KaindorfThings/blob/master/Readme_Pics/PIO_Upload.png?raw=true)
    Sollte der ESP nicht gefunden werden stellen sie bitte sicher das der ESP auch von PlatformIO erkannt wurde, sollte dies nicht der Fall sein überprüfen Sie ob die richtigen           [Treiber](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) für das Gerät installiert wurden.
  4. Nach dem Upload sollte der ESP laufen solange er Strom hat.
  
#### Verkabelung
  
## Known Issues

+ Sollte der Webserver/die API um Funktionen erweitert werden, darauf achten, dass nicht zu schnell zu viele coap Requests an das Ikea Gateway verschickt, das verschluckt sich sonst.
+ Bei einem Aufbau auf SBIM/BEST3 oder sonstigem großen Event --> Beim Router WLAN Channel auf 13 setzen, um Überschneidungen mit anderen Hotspots auszuweichen. Channel 14 auf 
  jeden Fall vermeiden, der Raspberry PI kann keinen Channel 14.
