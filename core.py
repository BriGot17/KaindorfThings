from flask import Flask, redirect, request
from flask import render_template

from coap_handler import coap_handler
app = Flask(__name__, template_folder="./src/templates")
app.config["DEBUG"] = True

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
    return redirect("http://localhost:5000/")
    
app.run(host = "0.0.0.0")

