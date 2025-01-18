from jutsu_downloader import IDataParser


class BrowserParser(IDataParser):
    def __init__(self, browser_headers: dict, browser_cookies: dict):
        self.headers = browser_headers
        self.cookies = browser_cookies

    def get_headers(self):
        return self.headers

    def get_cookies(self):
        return self.cookies

    @staticmethod
    def convert_browser_data(browser_data: dict) -> dict:
        """
        Преобразование данных браузера в словарь для использования в запросах.
        """
        return {
            browser_header["name"]: browser_header["value"]
            for browser_header in browser_data
            if not browser_header["value"].startswith(":")
            if not browser_header["name"].startswith(":")
        }
