class MyService:
    def download_image(self, url: str):
        if url:
            return True

        raise Exception('url is not valid')
