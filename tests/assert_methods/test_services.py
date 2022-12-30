import unittest
from my_project.assert_methods.services import MyService


class TestMyServices(unittest.TestCase):

    def test_download_img_success(self):
        # Setup
        my_service = MyService()

        # Action
        result = my_service.download_img('http://my.site.com/a.png')

        # Assert
        # self.assertEqual(True, result)
        self.assertTrue(result)

    def test_download_img_with_exception(self):
        # Setup
        my_service = MyService()

        # Assert
        with self.assertRaises(Exception):
            # Action
            my_service.download_img("")
