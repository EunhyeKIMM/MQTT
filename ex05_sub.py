# 모니터 운영 v1
# 토픽 수신시
# 시간, 토픽, 값을 sensorvalues.csv 파일에 추가 
# 메세지 수신시에만 file open, 단일 메시지 기록 후 close

# 모니터 운영 v2)
# 0)온도 1)습고 2)조도 3)미세먼지 4)종료

# 해당 메뉴를 선택한 경우, 현재까지의 평균값 출력 

from mqtt_sub import subscribe 
from datetime import datetime
from app_base import Application 

class MonitorApp(Application):
    def __init__(self):
        super().__init__()
        subscribe('localhost', "iot/#", self.on_message, forever=False)
        self.sensors = {
            'temp': [],
            'humi': [],
            'illu': [],
            'dust': [],
        }

    def create_menu(self, menu):
        menu.add('온도', self.pirnt_temp)
        menu.add('습도', self.pirnt_humi)
        menu.add('조도', self.pirnt_illu)
        menu.add('미세먼지', self.pirnt_dust)
        menu.add('종료', self.exit)

    def on_message(self, client, userdata, msg):
        with open(self.config.fname, 'at') as f:
            value = float(msg.payload)
            f.write(f'{datetime.now()},{msg.topic},{value}\n')
            key = msg.topic.split('/')[-1]
            self.sensors[key].append(value)



    def get_avg(self, key):
        total = sum(self.sensors[key])
        avg = total/len(self.sensors[key])
        return avg

    def print_temp(self):
        avg = self.get_avg('temp')
        print("온도: ", avg)

    def print_humi(self):
        avg = self.get_avg('humi')
        print("습도: ", avg)

    def print_illu(self):
        avg = self.get_avg('illu')
        print("조도: ", avg)

    def print_dust(self):
        avg = self.get_avg('dust')
        print("미세먼지: ", avg)


if __name__== "__main__":
    app = MonitorApp()
    app.run()


# FILE_NAME = 'sensorvalues.csv'

# def on_message(client, userdata, msg):
#     with open(FILE_NAME, 'at') as f:
#         f.write(f'{datetime.now()},{msg.topic},{float(msg.payload)}\n')

# subscribe('localhost', 'iot/#', on_message) 
