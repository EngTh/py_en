import os
import urllib.request

import playsound


class word(object):
    en_us = ""
    zh_cn = ""
    path = ""

    def __init__(self, en_us: str, zh_cn: str):
        self.en_us = en_us
        self.zh_cn = zh_cn
        self.path = r'http://dict.youdao.com/dictvoice?type=1&audio=' + en_us.lower()
        pass

    def PlayOral(self):
        try:
            urllib.request.urlretrieve(self.path, filename="temp.mp3")
            playsound.playsound("temp.mp3")
            os.remove("temp.mp3")
        except:
            return
        return

    pass
