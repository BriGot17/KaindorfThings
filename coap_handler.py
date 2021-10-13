import os
from sys import stdout

class coap_handler:
    name = ''
    key = ''
    ip = ''

    def __init__(self, name, key, ip):
        self.name = name
        self.key = key
        self.ip = ip

    def turn_on(self):
        order = '{"5850": 1, "5851": 1}'
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order}\' "coaps://{self.ip}:5684/15004/131076"'
        stream = os.popen(command)

    def change_level(self, level):
        lightlevel = f'"5851": {level}'
        order = '{"5850": 1, <place>}'
        order = order.replace('<place>', lightlevel)
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order}\' "coaps://{self.ip}:5684/15004/131076"'
        stream = os.popen(command)
        print(stream)
    
    def turn_off(self):
        print('hello')
        order = '{"5850": 0}'
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order}\' "coaps://{self.ip}:5684/15004/131076"'
        stream = os.popen(command)
        print(stream)

        