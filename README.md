# KaindorfThings
IoT-Schaustück für Bildungsmesse

Autoren:
+ [Daniel Brinar](https://github.com/Shadow174)
+ [Peter Gottlieb](https://github.com/gotped17)

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
  
## Known Issues

+ Sollte der Webserver/die API um Funktionen erweitert werden, darauf achten, dass nicht zu schnell zu viele coap Requests an das Ikea Gateway verschickt, das verschluckt sich sonst.
+ Bei einem Aufbau auf SBIM/BEST3 oder sonstigem großen Event --> Beim Router WLAN Channel auf 13 setzen, um Überschneidungen mit anderen Hotspots auszuweichen. Channel 14 auf 
  jeden Fall vermeiden, der Raspberry PI kann keinen Channel 14.
