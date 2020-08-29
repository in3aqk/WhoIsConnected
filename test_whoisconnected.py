import unittest
from libs.grabber import Grabber
from libs.database import Database
import libs.log

class Whoisconnected(unittest.TestCase):


    def setUp(self):
        self.grabber = Grabber()
        self.db = Database()


    def test_grabberInfoPage(self):
        page = self.grabber.getInfoPage()
        self.assertTrue(page != True, "Info Page not present")
        self.assertTrue(page.status_code == 200, "Response is not 200")

    def test_getHeadInfo(self):
        headInfo = self.grabber.getHeadInfo()
        self.assertTrue(len(headInfo) > 0, "Head Info not present")

    def test_db(self):
        result = self.db.insertHead('1.1.1.1','aa:bb:cc:dd:ee:ff','testHead')
        self.assertTrue(result, "DB Error on insert head")
        result = self.db.updateHeadByMac('1.1.1.1','aa:bb:cc:dd:ee:ff','NEW')
        self.assertTrue(result, "DB Error on update head")
        result = self.db.deleteHeadByMac('aa:bb:cc:dd:ee:ff')
        self.assertTrue(result, "DB Error on delete head")


if __name__ == '__main__':
    unittest.main()