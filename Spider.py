# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:18:49 2017

@author: win8
"""

import urllib
import re

class Spider:
    '''
        内涵段子爬虫类
    '''
    def __init__(self):
        self.page = 1
        #控制是否继续爬取
        self.swich = True
        self.url = "http://www.neihan8.com/article/list_5_{}.html".format(self.page)

    
    def loadPage(self, page=1):
        '''
            @brief 定义一个url请求网页的数据
        '''
        print('正在下载页面...')
        self.page = page
        
        self.url = "http://www.neihan8.com/article/list_5_{}.html".format(self.page)
        user_agent = 'Mozilla/5.0 compatible; MSIE 9.0; Windows NT6.1; Trident/5.0'
        headers = {'User-Agent': user_agent}
        
        request = urllib.request.Request(url=self.url, headers=headers)
        
        handler = urllib.request.HTTPHandler()
        opener = urllib.request.build_opener(handler)
        
        urllib.request.install_opener(opener)
        
        response = urllib.request.urlopen(request)
        #print(response.read().decode('gb2312'))
        html = response.read().decode('gbk')
        self.deal_html(html)
        
    def deal_html(self, html):
        pattern = re.compile('<div class="f18 mb20">(.*?)</div>', re.S)
        item_list = pattern.finditer(html)
        
        #去除一些多余的标签
        sub_pattern = re.compile('<br />|<p>|</p>|<br>|\&.*\;|\s')
        sub_item_list = []
        for item in item_list:
            #print('='*40)
            sub_item = sub_pattern.sub("", item.group(1))
            #print(type(sub_item))
            sub_item_list.append(sub_item + '\n')
        self.write_page(text_list=sub_item_list)
            
    def write_page(self, text_list, filename='duanzi.txt'):
        text = ''.join(text_list)
        with open(filename, 'a') as f:
            f.write('-'*20 + '第{}页'.format(self.page) + '-'*20 + '\n')
            f.write(text + '\n')
        print('内容已经保存在{}中'.format(filename))
        
    def startWork(self):
        while self.swich:
            flag = input('是否要爬取%s...的第%s页?(q:退出 y:确定)>>>' % (self.url[:15], self.page))
            if flag == 'y':
                self.loadPage(self.page)
                self.page += 1
            elif flag == 'q':
                self.swich = False
                print('感谢您的使用，新鲜的段子请签收！')
            else:
                flag = print('输入错误，请重新输入!')
            

        
duanzi_spider = Spider()
duanzi_spider.startWork()