#!/usr/bin/env python
import requests
import json

def hipchat_msg(url, msg, color):
    data = {
        "message": msg,
        "color": color,
        "notify": False,
        "message_format": "text",
        }
    headers = {"Content-type": "application/json"}
    r = requests.post(url=url, data=json.dumps(data), headers=headers)
    return 0
