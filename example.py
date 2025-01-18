import json

import jutsu_downloader
from jutsu_downloader.data_parser.browser_parser import BrowserParser
from jutsu_downloader.data_parser.curl_parser import CurlParser

url = "https://jut.su/jojo-bizarre-adventure/season-1/episode-2.html"

# with open("example.json", "r") as f:
#     data = json.load(f)
#     browser_headers = data["headers"]
#     browser_cookies = data["cookies"]
# data_parser = BrowserParser(browser_headers, browser_cookies)

with open("example.curl", "r") as f:
    data = f.read()
    data_parser = CurlParser(data)

downloader = jutsu_downloader.downloader(url, data_parser)
