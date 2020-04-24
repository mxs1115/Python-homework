#!/usr/bin/python
# -*- coding: UTF-8 -*-


#2 给定100个企业网站首页链接地址（用1中给出的URL地址）；请爬取每个页面上，企业介绍的链接地址；
  #  说明，满足企业介绍网址的条件是， 标题包含：企业介绍，关于我们，企业发展，发展历史，企业概况等关键字的URL地址；
  #  提示：要用到requests库，BeautifulSoup库

import re,os
from urllib import request
from bs4 import BeautifulSoup

def html_get(url):
    response=request.Request(url)
    page=request.urlopen(response)
    html=page.read()
    return html


html_list=list(map(html_get,['http://www.erguotou.cn','http://www.chrtc.cn','http://www.cttp.net.cn']))
for html in html_list:
    soup=BeautifulSoup(html.decode('utf-8'),'html.parser')
    a=soup.find_all('a')
    for b in a:
      c=b.get('href')
      print(c)