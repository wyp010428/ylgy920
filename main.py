from time import sleep
import requests
from time import sleep

u = "https://cat-match.easygame2021.com/sheep/v1/game/update_user_skin?skin=24"

t = "MODIFY_HERE"

headers = {
    "t": f"{t}", 
    "content-type": "application/json", 
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.27(0x18001b36) NetType/WIFI Language/zh_CN", 
    "Referer": "https://servicewechat.com/wx141bfb9b73c970a9/23/page-frame.html", 
    "Host": "cat-match.easygame2021.com", 
    "Connection": "keep-alive", 
    "Accept-Encoding": "gzip,compress,br,deflate", 
}

while True:
    r = requests.get(url = u, headers = headers)
    print(r.text)
    sleep(0.1)