# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 16:41:01 2017

@author: win8
"""

import requests
import lxml
import os


#https://tieba.baidu.com/f?kw=%E7%BE%8E%E5%A5%B3&pn=0

class Spider:
    def __init__(self):
        self.url = "https://tieba.baidu.com/f?"
        
        #注意这个user-agent， 一旦添加上就无法读取到数据
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        self.headers2 = {}
        
    def loadPage(self, tieba_name, kw):
        '''
            作用：获取某贴吧的主页
        '''
        
        
        #如果添加了headers参数，xpath就无法读取到数据，不知道为什么
        response = requests.get(self.url, params=kw)

        #用xpath获取每个帖子的链接        
        content = lxml.etree.HTML(response.content)
        #print(type(response.content))
        link_list = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        #link_title = content.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@title')
        #print(link_list)
        for link in link_list:
            full_link = "http://tieba.baidu.com" + link
            self.loadlink(full_link)
    
    def loadlink(self, link):
        response = requests.get(link)
        content = lxml.etree.HTML(response.text)
        image_list = content.xpath("//img[@class='BDE_Image']/@src")
        for image in image_list:
            self.writeImage(image)
        print('已经成功下载%s的帖子图片' % link[:30])
    
    def writeImage(self, image_src):
        image = requests.get(image_src)
        
        currnet_dir = os.path.abspath('.')
        #image_path = os.path.join(currnet_dir, '\\baidu_image\\第%s页' % self.page)
        image_path = currnet_dir + '\\baidu_image\\第%s页' % self.page
        #print(currnet_dir, image_path)
        if not os.path.exists(image_path):
            os.makedirs(image_path)
            
        with open('baidu_image/第%s页/' % self.page + image_src[-10:], 'wb') as f:
            f.write(image.content)
        
    def startwork(self):
        tieba_name = input('请输入贴吧名称>>>')
        start_index = input('请输入起始页>>>')
        end_index = input('请输入结束页>>>')
        
        if not tieba_name:
            tieba_name ='美女'
        for page in range(int(start_index), int(end_index)+1):
            self.page = page
            pn = (page - 1) * 50
            kw = {'kw': tieba_name,'pn':pn}
            print('正在下载第%s页的图片...' % page)
            self.loadPage(tieba_name, kw)
        
baidu_spider = Spider()
baidu_spider.startwork()
        
        