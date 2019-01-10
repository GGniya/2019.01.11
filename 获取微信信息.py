import itchat
import requests
import json
import re

# itchat.auto_login()
# itchat.send('Hello, filehelper', toUserName='filehelper')

citys =['北京','上海','深圳','郑州']
#文本消息回复
@itchat.msg_register(itchat.content.TEXT)   #接收微信消息    默认支持个人消息
def text_reply(msg):
    text =msg.text

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
        import cv2
        cap = cv2.VideoCapture(0)
        frame = cap.read()
        cv2.imshow("capture", frame)
        cv2.imwrite("video.jpg", frame)
        cap.release()
        cv2.destroyAllWindows()

    # if text == '郑州':
    #     return "天气晴朗"
    # else:
    #     pass

@itchat.msg_register([itchat.content.PICTURE])
def download_files(msg):
    msg.download(msg.fileName)
    return 'HHH'

itchat.auto_login(hotReload=True)
itchat.run()
