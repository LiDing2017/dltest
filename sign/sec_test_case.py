#coding=utf-8
import requests
import unittest
class GetEventListTest(unittest.TestCase):
    '''查询发布会信息（带用户认证）'''
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/api/sec_get_event_list/'
    def test_get_event_list_auth_null(self):
        '''auth为空'''
        r=requests.get(self.base_url,params={'eid':1})
        result=r.json()
        self.assertEqual(result['status'],10011)
        self.assertEqual(result['message'],'user auth null')
    def test_get_event_list_auth_error(self):
        '''auth错误'''
        auth_user=('abc','123')
        r=requests.get(self.base_url,auth=auth_user,params={'eid':1})
        result=r.json()
        self.assertEqual(result['status'],10012)
        self.assertEqual(result['message'],'user auth fail')
    def test_get_event_list_eid_null(self):
        '发布会id为空'''
        auth_user = ('admin', 'admin123321')
        r=requests.get(self.base_url,auth=auth_user,params={'eid':''})
        result=r.json()
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],'parameter error')
    def test_get_event_list_eid_success(self):
        '''发布会id为1，查询成功'''
        auth_user = ('admin', 'admin123321')
        r=requests.get(self.base_url,auth=auth_user,params={'eid':'1'})
        result=r.json()
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'],'success')
        self.assertEqual(result['data']['name'],'红米MAX发布会')
        self.assertEqual(result['data']['address'],'北京会展中心')
        #self.assertEqual(result['data']['start_time'],'success')
if __name__=='__main__':
    unittest.main()