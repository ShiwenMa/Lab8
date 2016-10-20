import doomsayer.metadata as metadata
import doomsayer.notify as notify
from doomsayer.config import CONFIG

import time
import requests
import json


if __name__ == '__main__':
    while True:
        if metadata.poll_instance_metadata():
            notify.hipchat_msg(CONFIG["endpoint"],CONFIG["msg"],CONFIG["color"])
            break
        time.sleep(5)
    time.sleep(120)
