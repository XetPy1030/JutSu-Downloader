import logging
import urllib.request

import requests
from bs4 import BeautifulSoup

from jutsu_downloader.consts import JUTSU_URL
from jutsu_downloader.data_parser.interface import IDataParser
from jutsu_downloader.utils import to_urllib_headers

__all__ = ["downloader"]
__version__ = "0.1.0"

logger = logging.getLogger(__name__)


def downloader(url: str, data_parser: IDataParser, limit: int = 10) -> None:
    """
    Утилита для скачивания серий аниме с сайта jut.su.

    :param url: Ссылка на первую серию аниме.
    :param data_parser: Парсер данных для получения заголовков и куки.
    :param limit: Количество серий для скачивания.
    """
    headers = data_parser.get_headers()
    cookies = data_parser.get_cookies()

    anime_site_response = requests.get(url, headers=headers, cookies=cookies)
    for _ in range(limit):
        logger.info(f"Downloading episode url: {anime_site_response.url}")

        soup = BeautifulSoup(anime_site_response.text, "lxml")
        quotes = soup.find_all('source')[-1]
        episode_link = quotes.get("src")

        quotes1 = soup.find_all('a', class_="short-btn green video vnright the_hildi there_is_link_to_next_episode")[-1]
        next_episode = quotes1.get("href")
        url = JUTSU_URL + next_episode

        *_, video_filename = next_episode.split("/")
        video_filename += ".mp4"
        save_video(episode_link, video_filename, headers)

        anime_site_response = requests.get(url, headers=headers, cookies=cookies)


def save_video(video_link: str, video_filename: str, headers: dict) -> None:
    opener = urllib.request.build_opener()
    opener.addheaders = to_urllib_headers(headers)
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(video_link, video_filename)
