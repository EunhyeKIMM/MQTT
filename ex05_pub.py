# 가상의 센서 4개 운영 
# 값은 센서마다 범위를 주고, 랜덤하게
#  
# 온도 센서 5초 간격으로 측정값 발행(iot/user1/temp)
# 습도 센서 7초 간격으로 측정값 발행(iot/user1/humi)
# 조도 센서 10초 간격으로 측정값 발행(iot/user1/illu)
# 미세먼지 센서 12초 간격으로 측정값 발행(iot/user1/dust)

from sensor import Sensor


sensors = [
    Sensor(5, (3, 10), 'iot/user1/temp'),
    Sensor(7, (20, 60), 'iot/user1/humi'),
    Sensor(10, (20, 80), 'iot/user1/illu'),
    Sensor(12, (0, 1), 'iot/user1/dust'),
]

for sensor in sensors:
    sensor.start() 