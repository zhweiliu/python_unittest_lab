import unittest
from unittest.mock import patch, MagicMock
from my_project.scrapers.web_scraper import ImageScraper


class TestImageScraper(unittest.TestCase):
    def setUp(self) -> None:
        self.service = ImageScraper()

    def tearDown(self) -> None:
        self.service = None

    @patch('my_project.scrapers.web_scraper.urlopen')
    @patch('my_project.scrapers.web_scraper.Request.__new__')
    def test_download_image_with_exception(self, mock_request, mock_urlopen):
        # Setup
        url = 'http://my.site.com/a.png'
        urlopen_return_mock = MagicMock()
        webfile_mock = MagicMock()
        mock_urlopen.return_value = urlopen_return_mock

        # The __enter__ method can be a return value of mock due to the MagicMock already achieved dunder methods
        urlopen_return_mock.__enter__.return_value = webfile_mock
        webfile_mock.read.return_value = None

        # Action
        with self.assertRaises(Exception):
            self.service.download_image(url)

    @patch('builtins.open')
    @patch('os.path.basename')
    @patch('my_project.scrapers.web_scraper.urlopen')
    @patch('my_project.scrapers.web_scraper.Request.__new__')
    def test_download_image_with_success(self, request_mock, urlopen_mock, basename_mock, open_mock):
        # Setup
        url = 'http://my.site.com/a.png'
        urlopen_return_mock = MagicMock()
        webfile_mock = MagicMock()
        urlopen_mock.return_value = urlopen_return_mock

        # The __enter__ method can be a return value of mock due to the MagicMock already achieved dunder methods
        urlopen_return_mock.__enter__.return_value = webfile_mock
        webfile_mock.read.return_value = 'data'

        basename_mock.return_value = 'filename'

        # Action
        result = self.service.download_image(url)

        # Assert
        self.assertEqual(f'Download image successfully, filename', result)
