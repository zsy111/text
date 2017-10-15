# text
#the first i write a part of a crawler

# -*- coding: utf-8 -*-
import urllib.request
import urllib

url = "http://www.qiushibaike.com/imgrank/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
#user_agent--种向访问网站提供你所使用的浏览器类型、操作系统及版本、CPU 类型、浏览器渲染引擎、浏览器语言、浏览器插件等信息的标识
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
#urllib2可以接受一个Request类的实例来设置URL请求的headers
response = urllib.request.urlopen(req)#网络请求操作
content = response.read().decode('utf-8')#.read() 每次读取整个文件，它通常用于将文件内容放到一个字符串变量中
print(content)
