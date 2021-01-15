# 가상의 센서 4개 운영 
# 값은 센서마다 범위를 주고, 랜덤하게
#  
# 온도 센서 5초 간격으로 측정값 발행(iot/user1/temp)
# 습도 센서 7초 간격으로 측정값 발행(iot/user1/humi)
# 조도 센서 10초 간격으로 측정값 발행(iot/user1/illu)
# 미세먼지 센서 12초 간격으로 측정값 발행(iot/user1/dust)

from threading import Thread
import time
import random
import paho.mqtt.client as mqtt

HOST = "localhost"
class Sensor(Thread):
    def __init__(self, interval, range, topic):
        super().__init__()
        self.interval = interval    # 전송 간격
        self.range = range          # 값의 범위 튜플
        self.topic = topic          # 튜플
        self.client = mqtt.Client()

    def run(self):
        self.client.connect(HOST)
        while True:
            time.sleep(self.interval)
            value = random.uniform(*self.range)
            # 토픽 발행
            print(self.topic, value)
            self.client.publish(self.topic, value)
            self.client.loop(2)

if __name__ == "__main__":
    temp_sensor = Sensor(5, (3, 10), 'iot/user1/temp')
    temp_sensor.start()

