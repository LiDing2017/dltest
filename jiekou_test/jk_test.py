# coding=utf-8
import HTMLTestRunner
import requests
import unittest

import time


class GetTitleNameTest(unittest.TestCase):
    def setUp(self):
        self.baseurl = "http://127.0.0.1:5000/dum?id=103"

    def test_id_exists(self):
        '''id存在'''
        r = requests.get(self.baseurl)
        print r
        result = str(r)
        self.assertEqual(result, u'探险活宝：岛屿')
        # def test_id_null(self):
        #     '''id为空'''
        #     r=requests.get(self.baseurl)
        #     print r
        #     result=r.json()
        #     self.assertEqual(result['message'],None)


if __name__ == '__main__':
    # unittest.main()

    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    testunit.addTest(GetTitleNameTest("test_id_exists"))
    testunit.addTest(GetTitleNameTest("test_id_exists"))
    testunit.addTest(GetTitleNameTest("test_id_exists"))
    # 获取当前时间，这样便于下面的使用。
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # 打开一个文件，将result写入此file中
    fp = open("result" + now + ".html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    runner.run(testunit)
    fp.close()
