# -*- coding: utf-8 -*-
"""
Created on Wed Aug 02 18:43:24 2017

@author: win8
"""

from bs4 import BeautifulSoup
import requests
import time 



def zhihu_login():
    
    login_session = requests.Session()
    
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}  
    login_url = "https://www.zhihu.com/#signin"
    
    html = login_session.get(login_url, headers=headers, verify = False).text
    
    bs = BeautifulSoup(html, 'lxml')
    
    #获取跨域攻击ide字符串
    _xsrf = bs.select('input[name="_xsrf"]')[0].get('value')
    #post地址
    post_url = "https://www.zhihu.com/login/phone_num"
    
    #获取验证码的地址，验证码保存到本地, 这个url貌似现在登陆网页已经找不到了
    captcha_url = "https://www.zhihu.com/captcha.gif?r=%d&type=login" % (time.time() * 1000)
    #获取验证码数据
    captcha_data = login_session.get(captcha_url, headers=headers).content
    
    text = captcha(captcha_data)
    #captcha_url = 
    #print(type(_xsrf))
    #print(_xsrf)
    post_data = {
        '_xsrf': _xsrf,
        'phone_num': '18656592099',
        'password': 'qq7730958123',
        'captcha': text,        
    }
    response = login_session.post(post_url, data=post_data, headers=headers)
    #print '>>>\n', response.text
    
    #可以查看用户的主页了
    response = login_session.get("https://www.zhihu.com/people/bian-cheng-xiao-bai-29/activities", headers=headers)
    with open('my.html', 'w') as f:
        f.write(response.text.encode('utf-8'))
    
def captcha(captcha_data):
    with open('captcha.jpg', 'wb') as f:
        f.write(captcha_data)
    text = raw_input('please input captcha>>')
    return text

zhihu_login()