from flask import Flask, redirect, request
from flask import render_template
import random

from coap_handler import coap_handler
app = Flask(__name__)
app.config["DEBUG"] = True

value = 0
coap = coap_handler('cisco', '1vB3D29hz7Uja2wS', '192.168.1.10')
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

app.add_url_rule("/", "index", home)

@app.route('/api/off', methods=['PUT', 'GET'])
def lamp_off():
    coap.turn_off()
    return redirect("http://localhost:5000/")

@app.route('/api/on', methods=['PUT', 'GET'])
def lamp_on():
    coap.turn_on()
    return redirect("http://localhost:5000/")
@app.route('/api/on/level')
def lamp_light_change():
    try:
        level = int(request.args['lightlevel'])
        coap.change_level(level)
    except:
        print('Not a number between 1 and 254')
    print("deja vu")
    return redirect("http://localhost:5000/")

@app.route('/api/moisturedata', methods=['PUT', 'GET'])
def get_moisture():
    value = int(request.args['moisture'])
    if value <= 60:
        coap.turn_on()
    return '{"result": "success"}'

@app.route('/api/moistureout')
def return_moisture():
    return '{"moisture": "' + str(random.randint(0,10)) + '"}'

@app.route('/api/ciscodisco/on', methods=['PUT', 'GET'])
def disco_on():
    print('corehello')
    coap.ciscodisco()
    return 'Success'


app.run(host = "0.0.0.0")

