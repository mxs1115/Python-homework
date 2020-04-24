#!/usr/bin/python
# -*- coding: UTF-8 -*-

#3  给定一个网址（包含了优质的英语学习音频文件），http://www.listeningexpress.com/studioclassroom/ad/； 
#  请大家写一个爬虫，将里面的英语节目MP3，都下载下来；

import wget
from urllib import request
import os,re
from urllib.parse import quote
import requests
def getHtml(url):
    page = requests.get(url)  
    html = page.text 
    print(html)
    return html

def getMp3Url(html):
    #html="'sc-ad 2020-04-15 Insights on Entertainment.mp3', 'sc-ad 2020-04-14 Insights on Entertainment.mp3', 'sc-ad 2020-04-24 The Benefits of Reading.mp3'"
    src = r"sc-.*?\.mp3"   
    imgre = re.compile(src)     
    print(imgre)
    imglist = imgre.findall(html) 
    print(imglist)   
    return  imglist

def downloadImages(img_url_list,path):
    if not os.path.exists(path):
        os.mkdir(path)
    x=0
    for url in img_url_list:
        url = quote(url)
        imageurl='http://www.listeningexpress.com/studioclassroom/ad/'+url   
        request.urlretrieve(imageurl, path+'\%s.mp3' %x)
        x=x+1
        print('downloading:  https:'+url,'\n')

if __name__=='__main__':
    url="http://www.listeningexpress.com/studioclassroom/ad/" 
    path=r"C:\Users\mac\Downloads\CodeProjects\PythonProjects\opms\homework7\3\downloadimage"   

    html = getHtml(url)
    images_url=getMp3Url(html)

    downloadImages(images_url,path)
    print('download success!')