from mqtt_sub import subscribe
# import paho.mqtt.client as mqtt


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

subscribe('localhost', 'iot/#', on_message)