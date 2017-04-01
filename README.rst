UaDetect
========

A simple User-Agent detect for Chinese UA.

Ref: https://gist.github.com/tjefferson/807106972c71b30ea9c2

Install
-------

.. code:: bash

    pip install git+https://github.com/TylerTemp/uadetect.git

OR

.. code:: bash

    git clone https://github.com/TylerTemp/uadetect.git
    cd uadetect
    python setup.py install

Usage
-----

.. code:: python

    import uadetect

    uastring = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; zh_CN) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/18.0 BIDUBrowser/2.6 Safari/534.7'
    print(uadetect.browser(uastring))  # baidu
    print(uadetect.guess_browser(ua))  # ['baidu', 'uc', 'chrome']
    print(uadetect.supported_browsers)
    # ['sogou', 'explorer2345', 'liebao', 'wechat', 'qqbrowser', 'baidu', 'uc', 'miuibrowser', 'mobileqq', 'shoujibaidu', 'samsungbrowser', 'firefox', 'maxthon', 'se360', 'ee360', 'theworld', 'weibo', 'nokiabrowser', 'opera', 'edge', 'qqlive', 'letv', 'youku', 'androidbrowser', 'ie', 'toutiao', 'chrome', 'safari']

Test
----

.. code:: bash

    git clone https://github.com/TylerTemp/uadetect.git
    cd uadetect
    python setup.py test
