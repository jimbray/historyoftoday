#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: jimbray
@contact: jimbray16@gmail.com
@site: 
@software: PyCharm
@file: gethistory.py
@time: 2015/10/16 9:54
"""

import urllib2
from bs4 import BeautifulSoup
import json
import sys

header = {'User-Agent': 'your agent string',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

base_url = 'http://www.lssdjt.com/'

# class History:
#
#     def __init__(self, title=None, url=None, content=None):
#         self.title = title
#         self.url = url
#         self.content = content
#
#     def history2dict(self, history):
#         return {
#             'title':history.title,
#             'url':history.url,
#             'content':history.content
#         }

def startContent(content_url):
    req = urllib2.Request(content_url, headers=header)

    response = urllib2.urlopen(req)

    soup = BeautifulSoup(response.read(), "html.parser")

    content = soup.select('.view .post_public')
    # print type(content[0])
    # print content[0].get('post_public').encode('utf-8')

    return str(content[0])
    # print type(str(content[0]))

def start():
    rep = urllib2.Request(base_url, headers=header)
    response = urllib2.urlopen(rep)

    soup = BeautifulSoup(response.read(), "html.parser")

    history_list = []

    items = soup.select('.list li a')

    for item in items:
        history_dict = {}
        history_dict['title'] = item.get('title')
        history_dict['url'] = item.get('href')
        history_dict['content'] = startContent(history_dict['url'])
        # history.content = ''.join(startContent(history.url))
        # history.content = json.dumps(startContent(history.url), ensure_ascii=False)
        history_list.append(history_dict)

    print('读取完成')
    print('-----------------')

    # print type(history_list)
    # print json.dumps(history_list,ensure_ascii=False)
    return json.dumps(history_list,ensure_ascii=False)


##测试
    # str = startContent(history_list[2].url)
    # print type(str.contents[0].string)
    # history_list[2].content = str
    # print history_list[2].content
    # print '--------------------------'
    # str = json.dumps(history_list[2], default=history_list[2].history2dict, ensure_ascii=False)
    # print str

    # print history_list[2].content
    # print '------------------'
    # str = json.dumps(history_list[2], default=history_list[2].history2dict, ensure_ascii=False)
    # print(str)

    # content = startContent(history_list[2].url)
    # print content
    # print '--------------'
    # str = json.dumps(content, ensure_ascii=False)
    # print str

def change_encode():##str默认编码为(3以下) ascii把 str 编码由 ascii 改为 utf8 (或 gb18030)
    reload(sys)
    sys.setdefaultencoding('utf-8')


change_encode()
if __name__ == '__main__':
    change_encode()
    print json.dumps(start().encode('utf-8'),ensure_ascii=False)