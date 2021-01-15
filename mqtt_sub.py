import paho.mqtt.client as mqtt


def subscribe(host, topic, on_message, forever=True):
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code", rc)
        if rc == 0:
            client.subscribe("iot/#")  # 연결 성공시 토픽 구독 신청 #은 하위항목을 다 보는 와일드 카드
        else:
            print('연결 실패: ', rc)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message 
    client.connect(host)
    if forever:
        client.loop_forever()
    else: 
        client.loop_start()