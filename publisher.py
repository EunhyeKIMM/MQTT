import paho.mqtt.client as mqtt

# 1. MATT 클라이언트 객체 인스턴스화 
client = mqtt.Client()

try: 
    # 2. 브로커 연결
    client.connect("localhost")

    # 3. 토픽 메시지 발행
    client.publish("iot/greeting", "Hello World!")
    client.loop(2)
except Exception as err:
    print("에러: %s"%err)