import paho.mqtt.client as mqtt
import base64
import json

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("v3/ecs@ttn/devices/eui-a8610a32374d7808/up")

def on_message(client, userdata, msg):
    print(msg.topic)
    payload_json = json.loads(msg.payload)
    if 'uplink_message' in payload_json and 'frm_payload' in payload_json['uplink_message']:
        encoded_payload = payload_json['uplink_message']['frm_payload']
        decoded_payload = base64.b64decode(encoded_payload).decode("utf-8")
        print(f"Received payload: {decoded_payload}")
    else:
        print("Received message does not contain expected payload.")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect
mqttc.on_message = on_message

mqttc.username_pw_set("ecs@ttn", "NNSXS.6EJ25ZBQOUZ2IDTRINVI4EJZTES5LGBDPFRA5OI.4RR6F22GW7LFLTG3KBVLXQGUFDPB47PBTEWXJKUV5ZIMWA6BTCSQ")
mqttc.connect("eu1.cloud.thethings.network", 1883, 60)

# To process messages without blocking forever, use loop_start() instead of loop_forever().
mqttc.loop_start()

# Now you can add additional code here to run after the loop has started.
# For example, you can wait for a specific condition or input to stop the loop.
input("Press Enter to stop...\n")
mqttc.loop_stop()

