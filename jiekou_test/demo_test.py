# coding=utf-8
import HTMLTestRunner
import requests
import unittest

import time

import dic2

class CalTest(unittest.TestCase):
    def setUp(self):
        self.url = 'http://127.0.0.1:5000/plus?'
        self.url1='http://127.0.0.1:5000/sub?'
    def zqtest(self):
        dic=dic2.dic1()

        r = requests.get(self.url, params={'x':dic[0][0], 'y':dic[0][1]})
        print 'lllllll'
        self.assertEqual(r.text, '3')
    def subtest(self):
        dic = dic2.dic1()

        r = requests.get(self.url, params={'x': dic[0][0], 'y': dic[0][1]})
        r1=requests.get(self.url1,params={'x':r.text,'y':1})
        self.assertEqual(r1.text,'2')
if __name__ == '__main__':
    #unittest.main()
    testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    testunit.addTest(CalTest("zqtest"))
    testunit.addTest(CalTest("zqtest"))
    testunit.addTest(CalTest("zqtest"))
    testunit.addTest(CalTest('subtest'))
    # 获取当前时间，这样便于下面的使用。
    now = time.strftime("%y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    # 打开一个文件，将result写入此file中
    fp = open("result" + now + ".html", 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='test result', description=u'result:')
    runner.run(testunit)
    fp.close()