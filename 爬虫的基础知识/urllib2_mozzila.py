# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 11:16:12 2017

@author: win8
"""

import urllib
#import urlib2_cookielib
import http.cookiejar as cookielib

filename = 'cookie.txt'
#cookiejar = urlib2_cookielib.cookielib.MozillaCookieJar()
cookiejar = cookielib.MozillaCookieJar(filename)

handler = urllib.request.HTTPCookieProcessor(cookiejar)

opener = urllib.request.build_opener(handler)

response = opener.open("http://www.baidu.com")

cookiejar.save()

print("\n>>>",response.url, response.code )
print(response.headers, "\n>>>")