# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 12:10:10 2017

@author: win8
"""

import urllib
import http.cookiejar as cookielib

cookiejar = cookielib.MozillaCookieJar()

cookiejar.load("cookie.txt")

handler = urllib.request.HTTPCookieProcessor(cookiejar)

opener = urllib.request.build_opener(handler)

response = opener.open("http://www.baidu.com")

print(response.headers)
print(dir(opener))
print(cookiejar)