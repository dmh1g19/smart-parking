import dash
from dash import html, dcc, Input, Output
import paho.mqtt.client as mqtt
import threading
import json
import base64

app = dash.Dash(__name__)

square_colors = ['green'] * 12
lock = threading.Lock()

# MQTT Subscriber Thread
def mqtt_subscriber():
    def on_connect(client, userdata, flags, reason_code, properties):
        print(f"Connected with result code {reason_code}")
        client.subscribe("v3/ecs@ttn/devices/eui-a8610a32374d7808/up")

    def on_message(client, userdata, msg):
        print(msg.topic)
        payload_json = json.loads(msg.payload)
        if 'uplink_message' in payload_json and 'frm_payload' in payload_json['uplink_message']:
            encoded_payload = payload_json['uplink_message']['frm_payload']
            decoded_payload = base64.b64decode(encoded_payload).decode("utf-8")
            print(f"App server received payload: {decoded_payload}")
            try:
                bay = json.loads(decoded_payload)['name'][-1]
                square_number = int(bay)
                with lock:
                    current_color = square_colors[square_number - 1]
                    square_colors[square_number - 1] = 'red' if current_color == 'green' else 'green'
            except (ValueError, KeyError):
                print("Error processing payload data.")
        else:
            print("Received message does not contain expected payload.")

    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("ecs@ttn", "NNSXS.6EJ25ZBQOUZ2IDTRINVI4EJZTES5LGBDPFRA5OI.4RR6F22GW7LFLTG3KBVLXQGUFDPB47PBTEWXJKUV5ZIMWA6BTCSQ")
    client.connect("eu1.cloud.thethings.network", 1883, 60)
    client.loop_forever()

# Start MQTT subscriber in a background thread
threading.Thread(target=mqtt_subscriber, daemon=True).start()

# Dash layout
app.layout = html.Div([
    dcc.Interval(id='interval-component', interval=1000, n_intervals=0),
    html.Div(id='squares-container', style={
        'display': 'flex',
        'flexWrap': 'wrap',
        'justifyContent': 'center',  # Center the squares horizontally
        'alignItems': 'center',  # Center the squares vertically
        'maxWidth': '500px',  # Maximum width of the grid
        'margin': '0 auto'  # Center the grid itself
    })
])

@app.callback(
    Output('squares-container', 'children'),
    Input('interval-component', 'n_intervals')
)
def update_layout(n):
    with lock:
        squares = [
            html.Div(children=[
                html.H1(str(i + 1), style={'color': 'white', 'margin': '0 auto', 'display': 'flex', 'alignItems': 'center', 'justifyContent': 'center'}),
            ],
            style={
                'height': '100px',
                'width': '100px',
                'backgroundColor': square_colors[i],
                'margin': '10px',
                'display': 'flex',
                'alignItems': 'center',  # Center the number vertically
                'justifyContent': 'center',  # Center the number horizontally
                'flex': '0 0 23%'  # Ensure that only 4 squares are on one row
            }) for i in range(12)
        ]
    return squares

if __name__ == '__main__':
    app.run_server(debug=True)

