import re

__version__ = '0.0.1'
__author__ = '<TylerTemp> tylertempdev@gmail.com'

# ensure the order, use list instead
ua_re = [
    ('sogou', re.compile(r'SE\s2\.X|SogouMobileBrowser')),
    ('2345', re.compile(r'2345Explorer|2345chrome|Mb2345Browser')),
    ('liebao', re.compile(r'LBBROWSER')),
    ('wechat', re.compile(r'MicroMessenger')),
    ('qqbrowser', re.compile(r'QQBrowser')),
    ('baidu', re.compile(r'BIDUBrowser|baidubrowser|BaiduHD')),
    ('uc', re.compile(r'UBrowser|UCBrowser|UCWEB')),
    ('miuibrowser', re.compile(r'MiuiBrowser')),
    ('mobileqq', re.compile(r'Mobile\/\w{5,}\sQQ\/(\d+[\.\d]+)')),
    ('shoujibaidu', re.compile(r'baiduboxapp')),
    ('samsungbrowser', re.compile(r'samsungbrowser')),
    ('firefox', re.compile(r'Firefox')),
    ('maxthon', re.compile(r'Maxthon')),
    ('se360', re.compile(r'360SE')),
    ('ee360', re.compile(r'360EE')),
    ('theworld', re.compile(r'TheWorld')),
    ('weibo', re.compile(r'__weibo__')),
    ('nokiabrowser', re.compile(r'NokiaBrowser')),
    ('opera', re.compile(r'Opera|OPR\/(\d+[\.\d]+)')),
    ('edge', re.compile(r'Edge')),
    ('qqlive', re.compile(r'QQLive(HD)?Browser')),
    ('letv', re.compile(r'LetvClient')),
    ('youku', re.compile(r'Youku')),
    ('androidbrowser', re.compile(r'Android.*Mobile\sSafari|Android\/(\d[\.\d]+)\sRelease\/(\d[\.\d]+)\sBrowser\/AppleWebKit(\d[\.\d]+)/')),
    ('ie', re.compile(r'Trident|MSIE')),
    ('toutiao', re.compile(r'NewsArticle')),
    ('chrome', re.compile(r'Chrome|CriOS')),
    ('safari', re.compile(r'Version[|\/]([\w.]+)(\s\w.+)?\s?Safari|like\sGecko\)\sMobile\/\w{3,}$')),
]

supported_browsers = [x[0] for x in ua_re]


def browser(ua):
    for name, reg in ua_re:
        if reg.search(ua) is not None:
            return name
    return None


def guess_browser(ua):
    possiblilities = []
    for name, reg in ua_re:
        if reg.search(ua) is not None:
            if name not in possiblilities:
                possiblilities.append(name)
    return possiblilities


if __name__ == '__main__':
    print('supported_browsers: %s' % '\n'.join(supported_browsers))
    ua = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh_CN) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/18.0 BIDUBrowser/2.6 Safari/534.7'
    print('if ua="%s"' % ua)
    print(browser(ua))
    print(guess_browser(ua))
