import unittest
from uadetect import browser


class Test(unittest.TestCase):

    def test_ie(self):
        self.assertEqual(browser('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'), 'ie')

    def test_sogou(self):
        self.assertEqual(browser('User-Agent:Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)'), 'sogou')

    def test_baidu(self):
        self.assertEqual(browser('Mozilla/5.0 (Windows; U; Windows NT 6.1; zh_CN) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/18.0 BIDUBrowser/2.6 Safari/534.7'), 'baidu')

    def test_2345(self):
        self.assertEqual(browser('Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/31.0.1650.69 Safari/537.36 2345chrome v2.5.0.3895'), '2345')

    def test_liebao(self):
        self.assertEqual(browser('Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; LBBROWSER)'), 'liebao')

    def test_wechat(self):
        self.assertEqual(browser('Mozilla/5.0 (iPhone; CPU iPhone OS 6_1_3 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Mobile/10B329 MicroMessenger/5.0.1'), 'wechat')

    def test_qqbrowser(self):
        self.assertEqual(browser('Mozilla/5.0 (Linux; U; Android 6.0.1; zh-cn; ONE A2001 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/37.0.0.0 MQQBrowser/6.0 Mobile Safari/537.36'), 'qqbrowser')

    def test_uc(self):
        self.assertEqual(browser('Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 UBrowser/3.1.1644.29 Safari/537.36'), 'uc')

    def test_juzi(self):
        self.assertEqual(browser('Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0; JuziBrowser)'), 'juzi')

# TODO: More test


if __name__ == '__main__':
    unittest.main()
