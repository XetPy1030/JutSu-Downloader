import requests, urllib.request
from har import a
from harvideo import b
from bs4 import BeautifulSoup

def convert(val):
    ret = {}
    for i in val:
        ret[i["name"]] = i["value"]
    return ret

def save_video(src, i):
	print(i)
	opener = urllib.request.build_opener()
	opener.addheaders = [
		('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64; rv:96.0) Gecko/20100101 Firefox/96.0'),
		("Accept", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"),
		("Accept-Language", "ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3"),
		("Accept-Encoding", "Accept-Encoding"),
		("Connection", "keep-alive"),
		("Upgrade-Insecure-Requests", "1"),
		("Sec-Fetch-Dest", "document"),
		("Sec-Fetch-Mode", "navigate"),
		("Sec-Fetch-Site", "cross-site")
	]
	urllib.request.install_opener(opener)
	#urllib.request.urlretrieve("type URL here", "path/file_name")
	urllib.request.urlretrieve(src, i.split("/")[-1]+".mp4")

#save_video(
#	"https://r330108.kujo-jotaro.com/fairytail/2/217.360.e69410b6f0155b38.mp4?hash1=eb12bc56fa0073f40f69b9159063e399", 
#	"a.mp4"
#	)

headers = convert(a["log"]["entries"][0]["request"]["headers"])
cookies = convert(a["log"]["entries"][0]["request"]["cookies"])

req = requests.get("https://jut.su/faairytail/season-2/episode-217.html", headers=headers, cookies=cookies)
i = 0
while i<20:
	soup = BeautifulSoup(req.text, "lxml")
	quotes = soup.find_all('source')[-1]
	quotes1 = soup.find_all('a', class_="short-btn green video vnright the_hildi there_is_link_to_next_episode")[-1]
	
	save_video(quotes.get("src"), quotes1.get("href"))

	req = requests.get("https://jut.su"+quotes1.get("href"), headers=headers, cookies=cookies)