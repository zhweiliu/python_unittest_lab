from urllib.request import urlopen, Request
import os.path


class ImageScraper:

    def __init__(self):
        self.__headers = {
            'User-Agent': 'Mozilla/5.0'
        }

    @property
    def headers(self):
        return self.__headers

    def put_header(self, header_name: str, header_value: str):
        if not header_value:
            raise ValueError('header name cannot be empty')

        if not header_value:
            raise ValueError('header value cannot be empty')

        self.__headers[header_name] = header_value

    def download_image(self, url: str):
        site_url = Request(url, headers=self.headers)
        with urlopen(site_url) as web_file:
            img_data = web_file.read()

        if not img_data:
            raise Exception(f'Error: cannot load the image from {url}')

        file_name = os.path.basename(url)
        with open(file_name, 'wb') as file:
            file.write(img_data)

        return f'Download image successfully, {file_name}'
