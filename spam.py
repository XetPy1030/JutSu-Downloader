from cgitb import text
from log import a
import requests, json, time
from random import randint, choice

log = a["log"]["entries"][0]["request"]

def convert(val):
    ret = {}
    for i in val:
        ret[i["name"]] = i["value"]
    return ret

headers = convert(log["headers"])
cookies = convert(log["cookies"])
postData = json.loads(log["postData"]["text"])

"""
1 - @верифицированный | :A_dogecoin:100 every 1 hour
2 - @👤Мемчанин | :A_dogecoin:250 every 1 hour
3 - @мишк фреде | :A_dogecoin:300 every 1 hour
4 - @aboba | :A_dogecoin:600 every 1 hour
5 - @Особый Мемчанин | :A_dogecoin:800 every 1 hour
6 - @хаги ваги | :A_dogecoin:1,200 every 1 hour
7 - @документ мемов | :A_dogecoin:3,000 every 1 hour
8 - @бешеный банкомат | :A_dogecoin:10,000 every 1 hour
9 - @настоящий бебрик | :A_dogecoin:25,000 every 1 hour
10 - @doge miner | :A_dogecoin:75,000 every 1 hour
11 - @cumposter | :A_dogecoin:150,000 every 1 hour
12 - @мемный бизнесскамер | :A_dogecoin:350,000 every 1 hour
13 - @король мемчан | :A_dogecoin:500,000 every 1 hour
14 - @мемный президент🤴🏽 | :A_dogecoin:1,200,000 every 2 hours
15 - @Помощник президента | :A_dogecoin:200,000 every 2 hours

@верифицированный - бысплатно.                                  100 в час
@👤Мемчанин  - стоимость            250. Заработок              100 в час
@мишк фреде   - стоимость           1500.                       250 в час.
@aboba  - стоимость                 5000.                       600 в час.
@Особый Мемчанин   - стоимость      8500.                       800 в час 
@хаги ваги  - стоимость             18000.                      1200 в час 
@документ мемов   -                 65000.                      3000 в час. 
@бешеный банкомат   -               200000 стоимость.           10000 в час.
@настоящий бебрик  - стоимость      650000.                     25000 в час.
@doge miner  - стоимость            1200000.                    75000 в час.
@cumposter  - стоимость             2000000.                    150000 в час.
@мемный бизнесскамер -              7000000.                    350000 в час
@король мемчан  -                   15000000.                   500000 в час
"""
roles = { # role: coin, duration(min)
    "938025773879660564": [10, 60], # Helper
    "938025927294713886": [20, 60], # MlModerator
    "938026123080634388": [200, 60], # Helper
    "938026329666891806": [600, 60], # Moderator
    "938026494188453888": [1000, 60], # Administrator
    "938026600040128512": [2500, 60], # GlAdministrator
    "938026707707916288": [5000, 60], # Car Memchan
    "938026774774808577": [7000, 60], # Boss Memchan
    "938027038424596510": [10000, 60], # Pomochnik presidenta
    "938027098122113034": [50000, 60], # Memniy president
    "938027296311345153": [200000, 180], # Bog Memchan
    "938027557117362186": [70000, 120], # car memchan
}

texts = ["!slut"]
i = 0
while True:
    i += 1

    text_req = requests.get("https://fish-text.ru/get")
    text_req.encoding = "utf-8"
    text_read = json.loads(text_req.text)["text"]

    postData["nonce"] = str(randint(10**18, 10**19)) # 18 symbols
    postData["content"] = "Я НЕ УСПОКОЮСЬ пока не попаду в рейтинг. \n"+text_read+" @noteveryone"
    requests.post(
        "https://discord.com/api/v9/channels/841372176761749524/messages", 
        headers=headers, 
        cookies=cookies,
        data=json.dumps(postData)
    )

    print(i)
    time.sleep(2)