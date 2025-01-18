from jutsu_downloader import IDataParser


class CurlParser(IDataParser):
    def __init__(self, curl_data: str):
        self.headers = {}
        self.cookies = {}

        for line in curl_data.split("\n"):
            line = line.strip()

            if not line.startswith("-H"):
                continue

            line = line.removeprefix("-H ")
            line = line.removesuffix("\\").strip()
            line = line.removeprefix("'").removesuffix("'")

            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()

            if key.lower() == "cookie":
                self.cookies = {cookie.split("=")[0]: cookie.split("=")[1] for cookie in value.split("; ")}
            else:
                self.headers[key] = value

    def get_headers(self):
        return self.headers

    def get_cookies(self):
        return self.cookies
