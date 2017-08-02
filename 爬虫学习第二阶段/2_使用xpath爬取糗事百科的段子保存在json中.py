# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:12:26 2017

@author: win8
"""
import requests 
from lxml import etree
import json

url = "http://www.qiushibaike.com/8hr/page/1"
headers = {"User-Agent" : "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"}

html = requests.get(url, headers=headers, verify=False).text

text = etree.HTML(html)

duanzi_list = text.xpath("//div[contains(@id, 'qiushi_tag')]")

for item in duanzi_list:
    
    username_ele = item.xpath(".//div[contains(@class, 'author')]/a/h2")
    if username_ele:
        username = username_ele[0].text.strip()
    else:
        username = '匿名用户'.strip()
      
    
    content = item.xpath(".//div[@class='content']/span")[0].text
    
    zan = item.xpath('.//i[@class="number"]')[0].text
    
    comment = item.xpath('.//i[@class="number"]')[1].text
    #print(username, '>>',content, '>>', type(zan), type(comment))  
    item = {
        'username': username,
        'content': content,
        'zan': zan,
        'comment': comment,        
    }
    with open('qiushi.json', 'a') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
