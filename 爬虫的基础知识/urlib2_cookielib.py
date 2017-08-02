# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 11:16:12 2017

@author: win8
"""

import urllib
import http.cookiejar as cookielib

cookiejar = cookielib.CookieJar()

handler = urllib.request.HTTPCookieProcessor(cookiejar)

opener = urllib.request.build_opener(handler)

opener.open("http://www.baidu.com")

cookieStr = ""
for item in cookiejar:
    cookieStr = cookieStr + item.name + "=" + item.value + ';'

print(cookieStr)