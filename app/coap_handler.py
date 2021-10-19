import os
from sys import stdout
import time

# Klasse für alle benötigten coap-Requests um mit der Lampe und dem Gateway zu reden
class coap_handler:
    name = ''
    key = ''
    ip = ''

    def __init__(self, name, key, ip):
        self.name = name
        self.key = key
        self.ip = ip

    # Sendet Request zum Lampe einschalten
    def turn_on(self):
        order = '{"5850": 1 }'
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order}\' "coaps://{self.ip}:5684/15004/131076"'
        stream = os.popen(command)

    # Sendet Request zum Ändern der Helligkeit
    def change_level(self, level):
        lightlevel = f'"5851": {level}'
        order = '{"5850": 1, <place>}'
        order = order.replace('<place>', lightlevel)
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order}\' "coaps://{self.ip}:5684/15004/131076"'
        stream = os.popen(command)
        print(stream)
    
    # Sendet Request zum Ausschalten der Lampe
    def turn_off(self):
        print('hello')
        order = '{"5850": 0}'
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order}\' "coaps://{self.ip}:5684/15004/131076"'
        stream = os.popen(command)
        print(stream)

    # Der Disco-Durchlauf
    def ciscodisco(self):
        order1 = '{"5850": 0}'
        order2 = '{"5850": 1, "5851": 254}'
        order3 = '{"5850": 1, "5851": 10}'

        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order1}\' "coaps://{self.ip}:5684/15004/131076"'
        time.sleep(5)
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order2}\' "coaps://{self.ip}:5684/15004/131076"'
        time.sleep(5)
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order3}\' "coaps://{self.ip}:5684/15004/131076"'
        time.sleep(5)