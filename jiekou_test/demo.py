# coding=utf-8
import requests

# # r = requests.get("http://127.0.0.1:8000/dum?m=103")
#
# print "开始预报呢"
# print r.status_code
import unittest

class CalTest(unittest.TestCase):

    def setUp(self):
        self.url='http://127.0.0.1:5000/plus?'
    def test_zqtest(self):
        r=requests.get(self.url,params={'x':1,'y':2})
        self.assertEqual(3,3)
if __name__=='__main__':
    unittest.main(verbosity=2)


