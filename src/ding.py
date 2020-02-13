import json
import os
from datetime import datetime
try:
    import requests
except Exception as err:
    value = os.system("pip3 install requests")
    if value == 0:
        import requests
    else:
        print("错误信息：{0}，返回码：{1}".format(err, value))


class Ding(object):
    tag = '钉钉机器人,内容要有hui 字段'

    def __init__(self, url, text, action):
        self.url = url
        self.text = text
        self.action = action

    def Info(self):
        ''' 机器人发送信息内容 '''
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        now = datetime.now()
        json_text= {
        "msgtype": "text",
            "at": {
                "atMobiles": [
                    "需要@人的手机号"
                ],
                "isAtAll": self.action
            },
            "text": {
                "content": self.text
            }
        }
        api_url = requests.post(self.url, json.dumps(json_text), headers=headers).content
        print ("{time}: {info}".format(time=now, info=api_url))


# 机器人实例化
def ding(url, text, action=True):
    robot = Ding(url, text, action)
    robot.Info()
