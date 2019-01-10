# itchat
# 先用 pip install itchat   (cmd)
# itchat基本用法   https://itchat.readthedocs.io/zh/latest/
# http://ai.baidu.com/tech/ocr/general

import itchat
import requests
import json
import re
import cv2

citys = ['郑州', '北京', '上海', '深圳']


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    text = msg.text
    name = msg['User']            #获取用户可见信息
    Name = name.get('RemarkName')
    print(f"{Name} : {text}")


    pattern = re.compile(r"^1[35678]\d{9}$")
    is_phone = pattern.findall(text)
    print(text)
    if text in citys:
        url = f"http://api.map.baidu.com/telematics/v3/weather?location={text}&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?"
        content = requests.get(url).text
        data = json.loads(content)
        print("查询城市:", data['results'][0]['currentCity'])
        print("pm2.5指数:", data['results'][0]['pm25'])
        a = data['results'][0]['weather_data'][0]
        return f"日期{a['date']}天气{a['weather']}风力{a['wind']}温度{a['temperature']}"
    elif is_phone:
        return "中国移动"
    elif text == '打开摄像头':
        # 获取一帧
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        k = cv2.waitKey(1)
        cv2.imwrite('video.jpg', frame)
        cap.release()
        cv2.destroyAllWindows()

        itchat.send_image('video.jpg', toUserName=msg['FromUserName'])






@itchat.msg_register([itchat.content.PICTURE])
def download_files(msg):
    print(msg.fileName)
    msg.download(msg.fileName)
    return 'hello world'


itchat.auto_login(hotReload=True)
itchat.run()
