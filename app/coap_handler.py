import os
from sys import stdout
import time

class coap_handler:
    name = ''
    key = ''
    ip = ''
    

    def __init__(self, name, key, ip):
        self.name = name
        self.key = key
        self.ip = ip
        pass

    def turn_on(self):
        print('on')
        order = '{"5850": 1 }'
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order}\' "coaps://{self.ip}:5684/15004/131073"'
        stream = os.popen(command)
        print(stream)
        pass

    def change_level(self, level):
        print('change level')
        lightlevel = f'"5851": {level}'
        order = '{"5850": 1, <place>}'
        order = order.replace('<place>', lightlevel)
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order}\' "coaps://{self.ip}:5684/15004/131073"'
        stream = os.popen(command)
        print(stream)
        pass
    
    def turn_off(self):
        print('off')
        order = '{"5850": 0}'
        command = f'coap-client -m put -u "{self.name}" -k {self.key} -e \'{order}\' "coaps://{self.ip}:5684/15004/131073"'
        stream = os.popen(command)
        print(stream)
        pass

        