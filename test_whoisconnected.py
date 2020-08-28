import unittest
from libs.grabber import Grabber
import libs.log

class Whoisconnected(unittest.TestCase):


    def setUp(self):
        self.grabber = Grabber()


    def test_grabberInfoPage(self):
        page = self.grabber.getInfoPage()
        self.assertTrue(page != True, "Info Page not present")


if __name__ == '__main__':
    unittest.main()