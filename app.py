from flask import Flask, request, jsonify, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Variable global para almacenar las coordenadas
last_coordinates = None

@app.route('/sms', methods=['POST'])
def sms_reply():
    global last_coordinates
    # Obtener el mensaje entrante
    incoming_msg = request.form.get('Body')
    
    # Parsear las coordenadas del mensaje
    if 'lat:' in incoming_msg and 'lon:' in incoming_msg:
        lat_lon = incoming_msg.split(', ')
        lat = lat_lon[0].split(': ')[1]
        lon = lat_lon[1].split(': ')[1]
        last_coordinates = (lat, lon)
        
        # Crear una respuesta
        resp = MessagingResponse()
        resp.message("Coordenadas recibidas")
        return str(resp)

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    return jsonify(last_coordinates)

@app.route('/')
def index():
    return render_template('index.html', coordinates=last_coordinates)

if __name__ == "__main__":
    app.run(debug=True)
