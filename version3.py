#!/usr/bin/env python
# coding=utf-8

import requests
import re
from bs4 import BeautifulSoup

def parser(text):
        l = []
        soup = BeautifulSoup(text,'html.parser')
        for i in soup.find_all('a'):
            if i.get('class')==[u'lib-item']:
                libc = i.text.split()
                l.append(libc[0])
        if l == []:
            return None
        print l
        return l,len(l)

def require(libc):
    url = "https://publicki.top/d/"
    url += libc
    url += '.symbols'
    print url
    ret = requests.get(url)
    while (ret.status_code!=200):
        ret = requests.get(url)
    return ret.text.split('\n')

def get_libc_version(func_name, offset):
    url = 'https://publicki.top/libc/?q='
    url += func_name
    url += '%3A'
    url += hex(offset)
    r = requests.get(url)
    if r.status_code == 200:
        ret,count = parser(r.text)
        if count == 0 :
            print "not found"
            return None
        elif count == 1:
            print 'libc : ' + str(ret[0])
            return require(ret[0])
        else:
            number = input('select a database:\n')
            while( number>count-1 or number<0 ):
                number = input('select a database:\n')
            return require(ret[number])

def dic_equip(text)
    dic  = {}
    for i in text:
        if func_name in i:
            l = i.split(' ')
            dic[l[0]]=int(('0x'+l[1]),16)
    print dic

def elect(func_name, dic):
    try:
        return dic[func_name]
    except KeyError as ke:
        func_name = input('please input the func_name:\n')
        return find(func_name,text)

def find(func_name,text):
    pass

if __name__ == "__main__":
    text = get_libc_version('_IO_2_1_stdin_',0x5c0)
    ret = find('exec',text)
